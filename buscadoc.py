# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os 
import sys 
  

path = 'ficheros/'
option2 = sys.argv[1]  

obj = os.scandir(path) 
  



for entry in obj : 
    if entry.is_dir() or entry.is_file(): 
        
        nombre, extension = os.path.splitext(entry.name)
        if extension=='.doc' or extension=='.docx' or extension=='.xls' or extension == '.xlsm' or extension == '.xlsx':
            
            ruta = nombre+extension
            os.system('echo "</br><h3>ANÁLISIS DE MACROS SOSPECHOSAS:</H3></br>" >> "'+option2+'.html"')
           
            
            out = os.popen("olevba -a 'ficheros/"+ruta+"' | grep 'Suspicious' >> '"+option2+".html'").read()
            
            if not out:
                out = os.popen("olevba -a 'ficheros/"+ruta+"' | grep 'No VBA macros found' >> '"+option2+".html'").read()
                
            
                
            
            os.system("echo '</br>' >> '"+option2+".html'")
            ruta = nombre+extension
            os.system('echo "</br><h3>ANÁLISIS DE VIRUSTOTAL:</H3></br>" >> "'+option2+'.html"')
            os.system("echo El reporte del fichero "+ruta+ " en Virustotal es: >> '"+option2+".html'")
            os.system("python3 virustotal.py 'ficheros/"+ruta+"' >> '"+option2+".html'")
        
        elif extension == '.pdf' or extension == '.zip' or extension == '.exe' or extension == '.bin' or extension == '.msi' or extension == '.rar' or nombre == 'file>':
            ruta = nombre+extension
            os.system('echo "</br><h3>ANÁLISIS DE VIRUSTOTAL:</H3></br>" >> "'+option2+'.html"')
            os.system("echo El reporte del fichero "+ruta+ " en Virustotal es: >> '"+option2+".html'")
            os.system("python3 virustotal.py 'ficheros/"+ruta+"' >> '"+option2+".html'")
