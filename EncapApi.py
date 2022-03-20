from fastapi import FastAPI, File, UploadFile
import os
import json
import requests
from pydub import AudioSegment
from fastapi.responses import FileResponse
import io 
import aiofiles

app=FastAPI()

def speech_recognition(filee):
    url = "http://41.179.247.136:6000/inference"
    #x=io.BytesIO(filee)
    #y=io.BufferedReader(x)
    x=open(filee, 'rb')
    
    print(x)
    data = {'file':x }
    r = requests.post(url, files=data)
    print(r.status_code)
    response = json.loads(r.text)
    return response['transcript'].strip()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
         #sound = AudioSegment.from_wav(file)

         #channel_count = sound.duration_seconds  
         async with aiofiles.open("D:\senior_project\semester 2\Voice-Samples-txts-MCIT_8k_Mono.wav", 'wb') as out_file:
          content = await file.read()  # async read
          await out_file.write(content)  # async write
         
         txt=speech_recognition("D:\senior_project\semester 2\Voice-Samples-txts-MCIT_8k_Mono.wav")

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
