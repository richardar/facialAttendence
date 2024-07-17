from deepface import DeepFace
import os

def search(database,imagetofind):
    folders = os.listdir(database)
    
    try:

  
        
        if not len(os.listdir(database)) :
            return False
                
        dfs = DeepFace.find(img_path = imagetofind, db_path = os.path.join(database) ,threshold=0.0,enforce_detection=False)

        # print(dfs)
        # maindf = dfs[0]
        # maindf =  maindf[maindf['distance'] >= 0.75]
        # print(maindf)
        if not dfs[0].empty:
            print(dfs[0].iloc[0][0], 'dataframe is not empty ')

            id = []
            score = []
            
            
            print("the dfs contains", dfs[0])
            
            dfslength = len(dfs[0]['identity'])
            for i in range(dfslength):
                
            
                directory_path = os.path.dirname(dfs[0]['identity'][i])
                # print("directory path", directory_path)
                folder_name = os.path.basename(directory_path)
                id.append(folder_name)
                score.append(dfs[0]['distance'][i])
            # print('face identified, returning ', folder_name)
            print(id,score)
            
            return {'id': id,
                    'score':score} 
     
        return False
    except Exception as e:
        print("there has been a exception",e)
        return 2