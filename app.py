import uvicorn
import requests
from fastapi import File, UploadFile, FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        response = requests.post("http://0.0.0.0:80/v1/vision/detection",files={"image":contents}).json()
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
    return response
    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)