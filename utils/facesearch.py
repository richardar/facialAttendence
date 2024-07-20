from deepface import DeepFace
import os

def search(database, imagetofind):
    """
    Search for a given image in a database of images using facial recognition.

    Args:
        database (str): The path to the database directory containing images.
        imagetofind (str): The path to the image to be searched.

    Returns:
        dict or bool or int: If a match is found, returns a dictionary with 'id' and 'score' lists
                             containing the matched identities and corresponding distances.
                             If no match is found, returns False.
                             If an exception occurs, returns 2.
    """
    
    folders = os.listdir(database)
    
    try:
        if not len(os.listdir(database)):
            return False
                
        dfs = DeepFace.find(img_path=imagetofind, db_path=os.path.join(database), threshold=0.0, enforce_detection=False)

        if not dfs[0].empty:
            print(dfs[0].iloc[0][0], 'dataframe is not empty ')

            id = []
            score = []
            
            print("the dfs contains", dfs[0])
            
            dfslength = len(dfs[0]['identity'])
            for i in range(dfslength):
                directory_path = os.path.dirname(dfs[0]['identity'][i])
                folder_name = os.path.basename(directory_path)
                id.append(folder_name)
                score.append(dfs[0]['distance'][i])
            
            print(id, score)
            
            return {'id': id, 'score': score} 
     
        return False
    except Exception as e:
        print("there has been an exception", e)
        return 2