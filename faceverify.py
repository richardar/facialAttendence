from deepface import DeepFace

def compare_images(image1_path, image2_path):
    result = DeepFace.verify(image1_path, image2_path,anti_spoofing=True,enforce_detection=False,model_name="ArcFace",detector_backend="retinaface")
    return result



