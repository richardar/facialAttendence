from deepface import DeepFace
import os

def recognize(database,imagetofind):
    folders = os.listdir(database)
    
    try:

  
        
        if not len(os.listdir(database)) :
            return False
                
        dfs = DeepFace.find(img_path = imagetofind, db_path = os.path.join(database) ,threshold=0.3,enforce_detection=False)

        # print(dfs)
        # maindf = dfs[0]
        # maindf =  maindf[maindf['distance'] >= 0.75]
        # print(maindf)
        if not dfs[0].empty:
            print(dfs[0].iloc[0][0], 'dataframe is not empty ')


            # print("the dfs contains", dfs)

            directory_path = os.path.dirname(dfs[0].iloc[0][0])
            # print("directory path", directory_path)
            folder_name = os.path.basename(directory_path)
            # print('face identified, returning ', folder_name)
            return folder_name
     
        return False
    except Exception as e:
        print(e)
        return 2