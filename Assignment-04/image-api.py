import cv2
from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from deepface import DeepFace
from deepface.commons.logger import Logger
import numpy as np
app=FastAPI()

@app.get("/")
def read_root():
    return "Hello, welcome to my api In this api there is face analysis is done, such as age, gender and race, just send a photo file and see the result--created by mehdi ghaffari moghaddam"


@app.post("/image_processing/age")
async def image_processing(input_file:UploadFile=File(None)):
        if not input_file.content_type.startswith("image/"):
                 raise HTTPException(status_code=415,detail="unsupported file type")
        contents=await input_file.read()
        np_arry=np.frombuffer(contents,dtype=np.uint8)
        image=cv2.imdecode(np_arry,cv2.IMREAD_UNCHANGED)
        cv2.imwrite("test.jpg",image)
        objs = DeepFace.analyze(img_path = "test.jpg",actions = ['age'])
        data=str(objs)
        i=data.find('age')
        j=data.find('region')
        data=data[i-1:j-3]
        print(data)
        return(data)
@app.post("/image_processing/gender")
async def image_processing(input_file:UploadFile=File(None)):
        if not input_file.content_type.startswith("image/"):
                 raise HTTPException(status_code=415,detail="unsupported file type")
        contents=await input_file.read()
        np_arry=np.frombuffer(contents,dtype=np.uint8)
        image=cv2.imdecode(np_arry,cv2.IMREAD_UNCHANGED)
        cv2.imwrite("test.jpg",image)
        objs = DeepFace.analyze(img_path = "test.jpg",actions = ['gender'])
        data=str(objs)
        i=data.find('dominant_gender')
        j=data.find('region')
        data=data[i-1:j-3]
        print(data)
        return(data)
@app.post("/image_processing/race")
async def image_processing(input_file:UploadFile=File(None)):
        if not input_file.content_type.startswith("image/"):
                 raise HTTPException(status_code=415,detail="unsupported file type")
        contents=await input_file.read()
        np_arry=np.frombuffer(contents,dtype=np.uint8)
        image=cv2.imdecode(np_arry,cv2.IMREAD_UNCHANGED)
        cv2.imwrite("test.jpg",image)
        objs = DeepFace.analyze(img_path = "test.jpg",actions = ['race'])
        data=str(objs)
        i=data.find('dominant_race')
        j=data.find('region')
        data=data[i-1:j-3]
        print(data)
        return(data)




