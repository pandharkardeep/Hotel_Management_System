import streamlit as st
import os
import cv2
import supervision as sv
import torch
from groundingdino.util.inference import load_model, load_image, predict, annotate
import matplotlib.pyplot as plt
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
DB_NAME = 'object_detection'
COL_NAME = 'First-try'
MONGO_URI = "mongodb+srv://pandharkardeep35:7762Q0QmsBVhYqLF@deep.pfmz7xz.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COL_NAME]

st.title("Upload Images")
room_number = st.text_input("Enter the Room Number")
# Image upload
image_file_towel = st.file_uploader("Upload image of Bathroom", type=["jpg", "png", "jpeg"])
image_file_minibar = st.file_uploader("Upload image of Minibar", type = ["jpg","png","jpeg"])

# Model loading
if (image_file_towel or image_file_minibar) and room_number is not None:
    # Define model paths
    WEIGHTS_PATH = "D:/Datahackproj/ObjectDetectionProj/Videos/groundingdino_swint_ogc.pth"
    CONFIG_PATH = "D:/Datahackproj/ObjectDetectionProj/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"

    # Load model
    model = load_model(CONFIG_PATH, WEIGHTS_PATH)

    # Image path
    IMAGE_PATH = 'D:/Datahackproj/ObjectDetectionProj/Videos/Towel.jpg'

    # Define parameters
    

    # Load image and predict
    if image_file_towel is not None:
        TEXT_PROMPT = "Single Towel"
        BOX_TRESHOLD = 0.35
        TEXT_TRESHOLD = 0.25
        image_source, image = load_image(image_file_towel)
        boxes_towels, logits_towels, phrases_towels = predict(
            model=model,
            image=image,
            caption=TEXT_PROMPT,
            box_threshold=BOX_TRESHOLD,
            text_threshold=TEXT_TRESHOLD
        )
    if image_file_minibar is not None:
        TEXT_PROMPT = "Mini - Bar items"
        BOX_TRESHOLD = 0.35
        TEXT_TRESHOLD = 0.25
        image_source, image = load_image(image_file_minibar)
        boxes_minibar, logits_minibar, phrases_minibar = predict(
            model=model,
            image=image,
            caption=TEXT_PROMPT,
            box_threshold=BOX_TRESHOLD,
            text_threshold=TEXT_TRESHOLD
        )
    # Annotate with Supervision
    #annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
    if st.button("Inspection Complete"):
        # Plot image with Supervision
        minibar_items, towel_items = 0,0
        if image_file_minibar is not None:
            minibar_items = len(logits_minibar)
            st.text(f"Minibar items:{minibar_items}")
        if image_file_towel is not None:
            towel_items = len(logits_towels)
            st.text(f"Towels:{towel_items}")
        
        collection.update_one(
        {'Room_Number': int(room_number)},
        {'$set': {
            'status': "clean",
            'num_towels': towel_items,  # update the num_towels value
            'num_miniBarObjects': minibar_items # update the num_miniBarObjects value
        }}
        )   
        st.success("Details Updated!")
    
