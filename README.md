# Hotel_Management_System

This Hotel Management System is a web application developed using `Flask, HTML, CSS, TensorFlow, and Computer Vision technologies`. It provides functionalities for both administrators and staff members to efficiently manage hotel operations.

## Features
### Admin Panel
- Room Status: Admins can seamlessly view the status of all hotel rooms to determine whether they are clean or not. This helps in maintaining cleanliness standards and ensuring a pleasant experience for guests.
### Staff Panel
- Cleanliness Check using Computer Vision: Staff members can utilize computer vision to perform cleanliness checks in hotel rooms. This automated process helps in quickly identifying any areas that require attention, improving efficiency in housekeeping operations This has been made possible by Tensorflow Resnet50 Library.
- Inventory Management: Staff members can manage hotel inventory efficiently through the system. This includes tracking supplies, restocking items, and maintaining optimal inventory levels to meet guest needs.This has been made possible by GroundingDINO Algorithm.

## Installation
1. Clone the repository `git clone https://github.com/pandharkardeep/hotel-management-system.git`
2. Install the required dependencies
3. Run the Application - 
  - For Admin panel - 
       Go to AdminSide directory by `cd AdminSide`
       Run the application `python app.py`
  - For Staff panel -
       Go to StaffSide directory `cd GroundingDINO`
       Run the application `python app.py`
4. Access the application in your web browser at http://localhost:5000

## Usage
### Admin Panel:
Log in to the admin panel using your credentials.
Navigate to the room status section to view the cleanliness status of all hotel rooms.
### Staff Panel:
Log in to the staff panel using your credentials.
Perform cleanliness checks using the computer vision feature.
Manage hotel inventory efficiently through the inventory management system.

## Future Applications - 
- Damage Check : Checking the Damage and estimating the cost of repairs 
