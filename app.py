from flask import Flask,request
from PIL import Image
import cv2
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.getcwd(),'FaceDatabase')

@app.route('/',methods=['GET'])
def rspns():
    return "success"

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
    

    
    
        
    
    




@app.route('/findfromdb',methods=['POST'])
def findfromdb():
    pass


@app.route('/verify',methods=['POST'])
def verify():
    pass


@app.route('/spoof',methods=['POST'])
def verfiy():
    pass