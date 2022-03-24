from fastapi import FastAPI, File
import json
import requests
from pydub import AudioSegment
import io 

app=FastAPI()
class bufferedReader(io.BufferedReader):
    name="D:\senior_project\semester 2\Samples_before_denoising_8k_Mono\Clear-Ab-1.wav"

    
def speech_recognition(filee):
    url = "http://41.179.247.136:6000/inference"
    
    x=io.BytesIO(filee)
    y=bufferedReader(x)
    print(y)
    
    
    
    data = {'file':y }
    r = requests.post(url, files=data)
    print(r.status_code)
    response = json.loads(r.text)
    return response['transcript'].strip()

@app.post("/uploadfile/")
async def create_upload_file(file: bytes=File(...)):
    if not file:
        return {"message": "No upload file sent"}
    else:
         
          
         audio = AudioSegment(file, sample_width=2, frame_rate=8000, channels=1 )
         
         raw_bytes=audio.raw_data
         
         
         txt=speech_recognition(raw_bytes)

         if "<fil> " in txt:
            txt = txt.replace("<fil> ", "")

         if "<music> " in txt:
             txt = txt.replace("<music> ", "")

         if "<laugh> " in txt:
            txt = txt.replace("<laugh> ", "")
       
         return txt

