import requests
import json

url = "http://127.0.0.1:8000/uploadfile/"
data = {'file': open("D:\senior_project\semester 2\Samples_before_denoising_8k_Mono\Clear-Ab-1.wav", 'rb')}
r = requests.post(url, files=data)
response = json.loads(r.text)
print(response)