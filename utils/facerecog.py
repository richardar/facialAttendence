from deepface import DeepFace
import os

def recognize(database, imagetofind):
    """
    Recognizes a face in an image by comparing it with a database of known faces.

    Args:
        database (str): The path to the directory containing the database of known faces.
        imagetofind (str): The path to the image to be recognized.

    Returns:
        str: The name of the recognized face's folder if a match is found.
        False: If no match is found or the database is empty.
        2: If an exception occurs during the recognition process.
    """
    # Get the list of folders in the database directory
    
    folders = os.listdir(database)

    try:
        # Check if the database directory is empty
        if not len(os.listdir(database)):
            return False

        # Perform face recognition using DeepFace library
        dfs = DeepFace.find(img_path=imagetofind, db_path=os.path.join(database), threshold=0.3, enforce_detection=False, model_name="ArcFace", detector_backend="retinaface")

        # Check if the result dataframe is not empty
        if not dfs[0].empty:
            print(dfs[0].iloc[0][0], 'dataframe is not empty ')
            print("the dfs contains", dfs)

            # Extract the directory path and folder name of the recognized face
            directory_path = os.path.dirname(dfs[0].iloc[0][0])
            folder_name = os.path.basename(directory_path)
            return folder_name

        # If no match is found, return False
        return False
    except Exception as e:
        # Handle any exceptions that occur during the recognition process
        print(e)
        return 2