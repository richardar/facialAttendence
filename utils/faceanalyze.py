from deepface import DeepFace


def analyze(imgpath):
    try:
        # This block of code will be executed if there are no exceptions
        return DeepFace.analyze(img_path=imgpath, actions=['age', 'gender', 'race', 'emotion'])
    except Exception as e:
        # This block of code will be executed if an exception occurs
        print("An error occurred:", str(e))
        return None
    # This function analyzes the facial attributes of an image using the DeepFace library.
    # It takes an image path as input and returns the analysis results including age, gender, race, and emotion.

