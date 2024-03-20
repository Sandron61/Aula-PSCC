# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J3cgA-2wPBi1S3Bp37dADeXLkYHRBfa9
"""

import requests

rover = input("Digite o nome do rover (Opportunity, Curiosity, Spirit):").lower()

if rover == "curiosity":
  print("Data de operação: 2012-08-06 até hoje")

elif rover == "opportunity":
  print("Data de operação: 2004-01-25 até 2018-07-10")

elif rover == "spirit":
  print("Data de operação: 2004-02-04 até 2010-03-22")

data = input("Digite a data (YYYY-MM-DD):")
camera = input("Escolha a camera (FHAZ, RHAZ, MAST, CHEMCAM, MAHLI, MARDI, NAVCAM ou PANCAM):").lower()

url= f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={data}&camera={camera}&api_key=qG6kJYM5rHsm2dpoVfAiughadhoqLAd65odDwmse"


resposta = requests.get(url)

print(resposta)

if resposta.status_code == 200:
    dado = resposta.json()
    fotos = dado["photos"]
    for foto in fotos:
      print(foto["img_src"])
    else:
      print(f"Não achei fotos da camera: {camera.upper()}. Na data: {data}")
else:
  print(f"Erro {resposta.status_code}")