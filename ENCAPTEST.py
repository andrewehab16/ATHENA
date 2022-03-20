from fastapi import FastAPI, File, UploadFile
import os
import json
import requests
from pydub import AudioSegment
from fastapi.responses import FileResponse
import io 
import aiofiles

app=FastAPI()
class bufferedReader(io.BufferedReader):
    name="D:\senior_project\semester 2\Samples_before_denoising_8k_Mono\Clear-Ab-1.wav"

    
def speech_recognition(filee):
    url = "http://41.179.247.136:6000/inference"
    #x=AudioSegment.from_wav(filee)
    x=io.BytesIO(filee)
    y=bufferedReader(x)
    
    
    
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
         #sound = AudioSegment.from_wav(file.file)

         #channel_count = sound.duration_seconds  
         
         
         txt=speech_recognition(file)

         #if "<fil> " in txt:
            #txt = txt.replace("<fil> ", "")

         #if "<music> " in txt:
            # txt = txt.replace("<music> ", "")

         #if "<laugh> " in txt:
         #   txt = txt.replace("<laugh> ", "")
    
            
         return txt
@app.get("/transcribe-voice/{file_path}")
def MCIT_api(file_path):
    sound = AudioSegment.from_file(file_path)

    channel_count = sound.channels    
   # txt=speech_recognition(file_path)

    #if "<fil> " in txt:
            #txt = txt.replace("<fil> ", "")

    #if "<music> " in txt:
            #txt = txt.replace("<music> ", "")

    #if "<laugh> " in txt:
            #txt = txt.replace("<laugh> ", "")
    
    return channel_count
