# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os 
import sys 
import re

path = 'ficheros/'

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext




words = (['Pass:','Password:','archivio:','Archivio','pass:', 'contraseña:','Contraseña:','password:','archivo:','Archivo:','archivage:'])

text = open(path+"textfile1")
lines = text.read()
lines = "'"+cleanhtml(lines)+"'"
if lines:
	for busqueda in words:
					
					search = lines.find(busqueda)	
					
					if search != -1:

						txtStart = busqueda+" "
						txtEnd = " "

						f = open(path+"textfile1")
						content = f.read()
						text = content.split(txtStart)[1].split(txtEnd)[0].strip()
						text = cleanhtml(text)

else:

	text = open(path+"textfile2")
	lines = text.read() 
	lines = "'"+cleanhtml(lines)+"'"				
	for busqueda in words:
					
					search = lines.find(busqueda)	
					
					if search != -1:

						
						txtStart = busqueda+" "
						txtEnd = " "

						f = open(path+"textfile2")
						content = f.read()
						text = content.split(txtStart)[1].split(txtEnd)[0].strip()
						text = cleanhtml(text)
				 


obj = os.scandir(path) 
for entry in obj : 
    if entry.is_dir() or entry.is_file(): 
    	nombre, extension = os.path.splitext(entry.name)
    	if extension == '.zip':
    		ruta = path+nombre+extension
    		os.system("7z x '"+str(ruta)+"' -oficheros -aoa -p"+str(text))