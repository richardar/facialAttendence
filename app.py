from flask import Flask,request
from PIL import Image
import cv2
import os
from facerecog import recognize
import numpy as np
from faceverify import compare_images
from facesearch import search

app = Flask(__name__)

DB_PATH = os.path.join(os.getcwd(),'FaceDatabase')

@app.route('/',methods=['GET'])
def rspns():
    return "success"

#enroll a new person
@app.route('/enroll', methods=['POST'])
def enroll():
    if not os.path.isdir(DB_PATH):
        os.makedirs(DB_PATH)
    if not request.files['file']:
        return 'no image sent ', 402
    
    if not request.form.get('face_ref_id'):
        return 'no id sent',402
    
    
    
    face_ref_id = request.form.get('face_ref_id')
    image = request.files['file']
    image = Image.open(image)

    face_ref_path = os.path.join(DB_PATH, str(face_ref_id))
    
    if not os.path.isdir(face_ref_path):
        os.makedirs(face_ref_path,exist_ok=True)
    listdir = len(os.listdir(face_ref_path))
    
    image_path = os.path.join(face_ref_path,'{}.jpeg'.format(listdir) )
    image.save(image_path, format='JPEG')
    
    return f"Saved image for face_ref_id {face_ref_id} at {image_path}"
    
#find from db
@app.route('/findfromdb',methods=['POST'])
def findfromdb():
    image = Image.open(request.files['file'])
    imgarr = np.array(image)
    result = recognize(DB_PATH,imgarr)
    print("the fooking result is :", result)
    if result:
        if result is not None or result is not 2  and result :
            return result,200
    else:
        
        return "false",402 


#verify faces
@app.route('/verify',methods=['POST'])
def verify():
    image1 = request.files['file']
    image1 = Image.open(image1)
    image1 = np.array(image1)
    face_ref_id = request.form.get('face_ref_id')
    
    imagefolder = os.path.join(DB_PATH,str(face_ref_id))
    
    
    if os.path.isdir(imagefolder):
        if len(os.listdir(imagefolder)) >0:
            imagepath = os.path.join(imagefolder,'0.jpeg')
            image2 = Image.open(imagepath)
            image2 = np.array(image2)
            return compare_images(image1,image2)
            
            
            
    
    


@app.route('/facesearch',methods=['POST'])
def facesearch():
    
    
    image = Image.open(request.files['file'])
    imgarr = np.array(image)
    result = search(DB_PATH,imgarr)
    print("the fooking result is :", result)
    if result:
        if result is not None or result is not 2  and result :
            return result,200
    else:
        
        return "false",402 
