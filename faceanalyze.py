import deepface


def analyze(imgpath):
    return deepface.analyze(img_path= imgpath,actions=['age','gender','race','emotion'])