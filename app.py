from flask import Flask,request
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.getcwd(),'FaceDatabase')

@app.route('/',methods=['GET'])
def rspns():
    return "success"


@app.route('/enroll', methods=['POST'])
def enroll():
    if not os.path.isdir(DB_PATH):
        os.mkdir(DB_PATH)
        
    face_ref_id  = request.form.get('face_ref_id')

    if os.path.isdir(os.path.join(DB_PATH,str(face_ref_id))):
        
    
    image = request.files['file']
    
    
        
    
    
    pass



@app.route('/findfromdb',methods=['POST'])
def findfromdb():
    pass


@app.route('verify',methods=['POST'])
def verify():
    pass


@app.route('spoof',methods=['POST'])
def verfiy():
    pass