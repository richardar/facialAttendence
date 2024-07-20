from deepface import DeepFace


def analyze(imgpath):
    # This function analyzes the facial attributes of an image using the DeepFace library.
    # It takes an image path as input and returns the analysis results including age, gender, race, and emotion.

    return DeepFace.analyze(img_path= imgpath,actions=['age','gender','race','emotion'])