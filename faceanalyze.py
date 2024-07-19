from deepface import DeepFace


def analyze(imgpath):
    return DeepFace.analyze(img_path= imgpath,actions=['age','gender','race','emotion'])