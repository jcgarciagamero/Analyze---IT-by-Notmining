# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

from hashlib import md5
from virus_total_apis import PublicApi
import sys

ruta = sys.argv[1]


API_KEY = ""
api = PublicApi(API_KEY)
with open(ruta, "rb") as f:
    file_hash = md5(f.read()).hexdigest()
response = api.get_file_report(file_hash)

if response["response_code"] == 200:
    if response["results"]["positives"] > 0:
        print('Archivo malicioso. <br><strong>URL de Virustotal:</strong><a href="https://www.virustotal.com/gui/search/'+file_hash+'" target="_blank">Ver análisis en Virustotal</a>')
    else:
        print('Archivo seguro. <br><strong>URL de Virustotal:</strong><a href="https://www.virustotal.com/gui/search/'+file_hash+'" target="_blank">Ver análisis en Virustotal</a>')
else:
    print("No ha podido obtenerse el análisis del archivo.")
