from flask import Flask, request
from PIL import Image
import cv2
import os

#include utils in sys.path
import sys
sys.path.append(os.path.join(os.getcwd(),'utils'))
from facerecog import recognize
import numpy as np
from faceverify import compare_images
from facesearch import search
from faceanalyze import analyze


# Create Flask app
app = Flask(__name__)

# Define the path to the FaceDatabase directory
DB_PATH = os.path.join(os.getcwd(), 'FaceDatabase')

# Define the root route
@app.route('/', methods=['GET'])
def rspns():
    """
    This function is a route handler for the root URL ("/") of the application.
    It handles HTTP GET requests to the root URL.

    Input: None

    Output: A string "success"
    """
    
    
    return "success"

# Enroll a new person
@app.route('/enroll', methods=['POST'])
def enroll():
    """
    This function enrolls a new person by saving their face image in the FaceDatabase directory.
    
    Input:
    - A POST request with an image file and a face reference ID
    
    Output:
    - If the enrollment is successful, it returns the face metrics and face reference ID as a JSON object with HTTP status code 200.
    - If the enrollment fails due to missing image file or face reference ID, it returns an error message with HTTP status code 402.
    """
    # Create the FaceDatabase directory if it doesn't exist
    if not os.path.isdir(DB_PATH):
        os.makedirs(DB_PATH)
    
    # Check if an image file is sent
    if not request.files['file']:
        return 'no image sent', 402
    
    # Check if a face reference ID is sent
    if not request.form.get('face_ref_id'):
        return 'no id sent', 402
    
    # Get the face reference ID and image file
    face_ref_id = request.form.get('face_ref_id')
    image = request.files['file']
    image = Image.open(image)
    
    # Create a directory for the face reference ID if it doesn't exist
    face_ref_path = os.path.join(DB_PATH, str(face_ref_id))
    if not os.path.isdir(face_ref_path):
        os.makedirs(face_ref_path, exist_ok=True)
    
    # Get the number of images already enrolled for the face reference ID
    listdir = len(os.listdir(face_ref_path))
    
    # Save the image as a JPEG file in the face reference directory
    image_path = os.path.join(face_ref_path, '{}.jpeg'.format(listdir))
    image.save(image_path, format='JPEG')
    
    # Analyze the image for face metrics
    analyzed_data = analyze(image_path)
    
    # Return the face metrics and face reference ID
    return {
        'face_metrics': analyzed_data,
        'face_ref_id': face_ref_id
    }

# Find a face from the FaceDatabase
@app.route('/findfromdb', methods=['POST'])
def findfromdb():
    """
    This function finds a face from the FaceDatabase by comparing it with the input image.
    
    Input:
    - A POST request with an image file
    
    Output:
    - If a face is found, it returns the result as a string with HTTP status code 200.
    - If no face is found, it returns "false" as a string with HTTP status code 402.
    """
    # Open the image file
    image = Image.open(request.files['file'])
    imgarr = np.array(image)
    
    # Recognize the face from the FaceDatabase
    result = recognize(DB_PATH, imgarr)
    
    # Check if a face is found
    if result:
        if result is not None or result != 2 and result:
            return result, 200
    else:
        return "false", 402

# Verify faces
@app.route('/verify', methods=['POST'])
def verify():
    """
    This function verifies a face by comparing it with a reference face from the FaceDatabase.
    
    Input:
    - A POST request with an image file and a face reference ID
    
    Output:
    - If the face is verified, it returns a string "true" with HTTP status code 200.
    - If the face is not verified, it returns a string "false" with HTTP status code 402.
    """
    # Get the first image file
    image1 = request.files['file']
    image1 = Image.open(image1)
    image1 = np.array(image1)
    
    # Get the face reference ID
    face_ref_id = request.form.get('face_ref_id')
    
    # Get the path to the face reference directory
    imagefolder = os.path.join(DB_PATH, str(face_ref_id))
    
    # Check if the face reference directory exists and has images
    if os.path.isdir(imagefolder):
        if len(os.listdir(imagefolder)) > 0:
            # Get the path to the first image in the face reference directory
            imagepath = os.path.join(imagefolder, '0.jpeg')
            image2 = Image.open(imagepath)
            image2 = np.array(image2)
            
            # Compare the two images for verification
            return compare_images(image1, image2)

# Search for a face in the FaceDatabase
@app.route('/facesearch', methods=['POST'])
def facesearch():
    """
    This function searches for a face in the FaceDatabase.
    
    Input:
    - A POST request with an image file
    
    Output:
    - If a face is found, it returns the result as a string with HTTP status code 200.
    - If no face is found, it returns "false" as a string with HTTP status code 402.
    """
    # Open the image file
    image = Image.open(request.files['file'])
    imgarr = np.array(image)
    
    # Search for the face in the FaceDatabase
    result = search(DB_PATH, imgarr)
    
    # Check if a face is found
    if result:
        if result is not None or result is not 2 and result:
            return result, 200
    else:
        return "false", 402

# Analyze a face
@app.route('/faceanalyze')
def faceanalyze():
    image = Image.open(request.files['file'])
    return analyze(image)