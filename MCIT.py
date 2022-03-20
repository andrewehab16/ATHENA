import os
import json
import requests
import io


def speech_recognition(input_wav_path):
    url = "http://41.179.247.136:6000/inference"
    x=open(input_wav_path, 'rb')
    #x=io.BytesIO(x)
    y=io.BufferedReader(x)
    print(y)
    data = {'file':y }

    r = requests.post(url, files=data)
    response = json.loads(r.text)
    return response['transcript'].strip()
    print(r)



def main():
     cur_path = os.getcwd()
     samples_path = os.path.join(cur_path, "Samples_before_denoising_8k_Mono")
     samples = os.listdir(samples_path)

     #for sample in samples:
         #sample_path = os.path.join(samples_path, sample)
     txt = speech_recognition("D:\senior_project\semester 2\Samples_before_denoising_8k_Mono\Clear-Ab-1.wav")

    # txtfile = .replace(".wav", ".txt")
     #txtfile_path = os.path.join(
     #cur_path, "Voice-Samples-txts-MCIT_8k_Mono", txtfile)

     #if "<fil> " in txt:
     #        txt = txt.replace("<fil> ", "")

     #if "<music> " in txt:
     #        txt = txt.replace("<music> ", "")

     #if "<laugh> " in txt:
     #        txt = txt.replace("<laugh> ", "")

     print(txt, ":", txt, "\n")


if __name__ == "__main__":
     main()
