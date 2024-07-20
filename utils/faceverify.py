from deepface import DeepFace

def compare_images(image1_path, image2_path):
    """
    Compare two images using the DeepFace library.

    Args:
        image1_path (str): The file path of the first image.
        image2_path (str): The file path of the second image.

    Returns:
        dict: A dictionary containing the result of the image comparison.
    """
    
    result = DeepFace.verify(image1_path, image2_path,anti_spoofing=True,enforce_detection=False,model_name="ArcFace",detector_backend="retinaface")
    return result



