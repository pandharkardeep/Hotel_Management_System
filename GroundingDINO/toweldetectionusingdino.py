from groundingdino.util.inference import load_model, load_image, predict, annotate
#import streamlit as st
#image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
WEIGHTS_PATH = "D:/Datahackproj/ObjectDetectionProj/Videos/groundingdino_swint_ogc.pth"
CONFIG_PATH = "D:/Datahackproj/ObjectDetectionProj/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
model = load_model(CONFIG_PATH, WEIGHTS_PATH)
import os
import supervision as sv
IMAGE_PATH = "D:\Datahackproj\ObjectDetectionProj\Images\Bathroom.jpg"

TEXT_PROMPT = "Single Towel"
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25

image_source, image = load_image(IMAGE_PATH)

boxes, logits, phrases = predict(
    model=model, 
    image=image, 
    caption=TEXT_PROMPT, 
    box_threshold=BOX_TRESHOLD, 
    text_threshold=TEXT_TRESHOLD
)

annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
import matplotlib.pyplot as plt
#%matplotlib inline  
sv.plot_image(annotated_frame, (16, 16))
print(len(boxes))
print(boxes)
