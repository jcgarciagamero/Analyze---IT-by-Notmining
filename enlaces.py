# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os
import sys       
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import urllib.request, urllib.parse, urllib.error, re
import requests

correo = "ficheros/"+sys.argv[1]+".eml"

ruta = "ficheros/"

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

f = open (correo,"r",encoding="utf-8",errors='ignore')
lines = f.read()
f.close()

enlas = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', lines)


for enlaces in enlas:

        f = open (ruta+'tmp.txt','r',encoding='utf-8',errors='ignore')
        txt = f.read()
        f.close()

        search = txt.find(enlaces)
        os.system("wget -P ficheros '"+enlaces+"'")
        if search == -1:

                f = open(ruta+"tmp.txt","a")
                f.write(enlaces)
                f.close()
                print(enlaces)
                url = "https://api.notmining.es/scan.php"
                post_fields = {'api': "kvzvoDqeVVJvD4ztvdE9EbH67m", "domain": enlaces}
                request = Request(url, urlencode(post_fields).encode())
                json = urlopen(request).read().decode('utf-8')
                f = open(ruta+"result.txt","a")
                f.write(cleanhtml(enlaces)+":"+str(json)+"</br>")
                f.close()
