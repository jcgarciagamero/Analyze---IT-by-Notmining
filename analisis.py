# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os, sys
import webbrowser
import mailparser
print("""
 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄        ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄      ▄         ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄                                  
▐░░░░░░░░░░░▐░░▌      ▐░▐░░░░░░░░░░░▐░▌    ▐░▌       ▐░▐░░░░░░░░░░░▐░░░░░░░░░░░▌      ▐░░░░░░░░░░░▐░░░░░░░░░░░▌                                 
▐░█▀▀▀▀▀▀▀█░▐░▌░▌     ▐░▐░█▀▀▀▀▀▀▀█░▐░▌    ▐░▌       ▐░▌▀▀▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀▀▀        ▀▀▀▀█░█▀▀▀▀ ▀▀▀▀█░█▀▀▀▀                                  
▐░▌       ▐░▐░▌▐░▌    ▐░▐░▌       ▐░▐░▌    ▐░▌       ▐░▌         ▐░▐░▌                     ▐░▌         ▐░▌                                      
▐░█▄▄▄▄▄▄▄█░▐░▌ ▐░▌   ▐░▐░█▄▄▄▄▄▄▄█░▐░▌    ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▐░▌         ▐░▌                                      
▐░░░░░░░░░░░▐░▌  ▐░▌  ▐░▐░░░░░░░░░░░▐░▌    ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌         ▐░▌                                      
▐░█▀▀▀▀▀▀▀█░▐░▌   ▐░▌ ▐░▐░█▀▀▀▀▀▀▀█░▐░▌     ▀▀▀▀█░█▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀▐░▌         ▐░▌                                      
▐░▌       ▐░▐░▌    ▐░▌▐░▐░▌       ▐░▐░▌         ▐░▌    ▐░▌         ▐░▌                     ▐░▌         ▐░▌                                      
▐░▌       ▐░▐░▌     ▐░▐░▐░▌       ▐░▐░█▄▄▄▄▄▄▄▄▄▐░▌    ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄▄▄        ▄▄▄▄█░█▄▄▄▄     ▐░▌                                      
▐░▌       ▐░▐░▌      ▐░░▐░▌       ▐░▐░░░░░░░░░░░▐░▌    ▐░░░░░░░░░░░▐░░░░░░░░░░░▌      ▐░░░░░░░░░░░▌    ▐░▌                                      
 ▀         ▀ ▀        ▀▀ ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀      ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀▀      ▀                                       
 ▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄▄        ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄       ▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄        ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄        ▄ ▄▄▄▄▄▄▄▄▄▄▄      
▐░░░░░░░░░░▌▐░▌       ▐░▌     ▐░░▌      ▐░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░▌     ▐░░▐░░░░░░░░░░░▐░░▌      ▐░▐░░░░░░░░░░░▐░░▌      ▐░▐░░░░░░░░░░░▌     
▐░█▀▀▀▀▀▀▀█░▐░▌       ▐░▌     ▐░▌░▌     ▐░▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀▐░▌░▌   ▐░▐░▌▀▀▀▀█░█▀▀▀▀▐░▌░▌     ▐░▌▀▀▀▀█░█▀▀▀▀▐░▌░▌     ▐░▐░█▀▀▀▀▀▀▀▀▀      
▐░▌       ▐░▐░▌       ▐░▌     ▐░▌▐░▌    ▐░▐░▌       ▐░▌    ▐░▌    ▐░▌▐░▌ ▐░▌▐░▌    ▐░▌    ▐░▌▐░▌    ▐░▌    ▐░▌    ▐░▌▐░▌    ▐░▐░▌               
▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▐░▌   ▐░▐░▌       ▐░▌    ▐░▌    ▐░▌ ▐░▐░▌ ▐░▌    ▐░▌    ▐░▌ ▐░▌   ▐░▌    ▐░▌    ▐░▌ ▐░▌   ▐░▐░▌ ▄▄▄▄▄▄▄▄      
▐░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▐░▌       ▐░▌    ▐░▌    ▐░▌  ▐░▌  ▐░▌    ▐░▌    ▐░▌  ▐░▌  ▐░▌    ▐░▌    ▐░▌  ▐░▌  ▐░▐░▌▐░░░░░░░░▌     
▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀      ▐░▌   ▐░▌ ▐░▐░▌       ▐░▌    ▐░▌    ▐░▌   ▀   ▐░▌    ▐░▌    ▐░▌   ▐░▌ ▐░▌    ▐░▌    ▐░▌   ▐░▌ ▐░▐░▌ ▀▀▀▀▀▀█░▌     
▐░▌       ▐░▌    ▐░▌          ▐░▌    ▐░▌▐░▐░▌       ▐░▌    ▐░▌    ▐░▌       ▐░▌    ▐░▌    ▐░▌    ▐░▌▐░▌    ▐░▌    ▐░▌    ▐░▌▐░▐░▌       ▐░▌     
▐░█▄▄▄▄▄▄▄█░▌    ▐░▌          ▐░▌     ▐░▐░▐░█▄▄▄▄▄▄▄█░▌    ▐░▌    ▐░▌       ▐░▌▄▄▄▄█░█▄▄▄▄▐░▌     ▐░▐░▌▄▄▄▄█░█▄▄▄▄▐░▌     ▐░▐░▐░█▄▄▄▄▄▄▄█░▌     
▐░░░░░░░░░░▌     ▐░▌          ▐░▌      ▐░░▐░░░░░░░░░░░▌    ▐░▌    ▐░▌       ▐░▐░░░░░░░░░░░▐░▌      ▐░░▐░░░░░░░░░░░▐░▌      ▐░░▐░░░░░░░░░░░▌     
 ▀▀▀▀▀▀▀▀▀▀       ▀            ▀        ▀▀ ▀▀▀▀▀▀▀▀▀▀▀      ▀      ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀        ▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀        ▀▀ ▀▀▀▀▀▀▀▀▀▀▀      
                                                                                                                                                
""")

print("Selecciona el tipo de fichero a analizar: ")
print("(1): MSG o EML")
print("")
print("(2): Otros")
print("(0): Exit")
print("")
option = input("Option: ")




if option == "1":
    
    option2 = input("Introduce el nombre del fichero sin la extensión: ")

    if option2:

        os.system('python3 desing.py "'+option2+'.html"')
        os.system('echo "" > ficheros/result.txt')
        os.system('echo "" > ficheros/tmp.txt')
        os.system('msgconvert "ficheros/'+option2+'.msg"')
        os.system('mv "'+option2+'.eml" "ficheros/'+option2+'.eml"')
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system("echo '<strong>FROM:</strong>' >> '"+option2+".html'")
        os.system('mailparser -f "ficheros/'+option2+'.eml" -m -l CRITICAL >> "'+option2+'.html"')
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system("echo '<strong>TO:</strong>' >> '"+option2+".html'")
        os.system('mailparser -f "ficheros/'+option2+'.eml" -t -l CRITICAL >> "'+option2+'.html"')
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system("echo '<strong>ASUNTO:</strong>' >> '"+option2+".html'")
        os.system('mailparser -f "ficheros/'+option2+'.eml" -u -l CRITICAL >> "'+option2+'.html"')
        os.system('echo "</br>" >> "'+option2+'.html"')
      
        
        os.system('mailparser -f "ficheros/'+option2+'.eml" -c -l CRITICAL >> "'+option2+'.html"')

        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system('echo "<h2>ANÁLISIS DE URLS EN EL CUERPO DEL CORREO</H2>" >> "'+option2+'.html"')
        os.system('python3 enlaces.py "'+option2+'"')
        os.system('cat ficheros/result.txt >> "'+option2+'.html"')
        os.system('rm -rf ficheros/*.txt')
        os.system('rm -rf > ficheros/result.txt')
        os.system('rm -rf ficheros/tmp.txt')
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system("ripmime -i 'ficheros/"+option2+".eml' -d ficheros/")
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system('python3 passSearch.py')
        os.system('echo "<h2>ANÁLISIS DE FICHEROS ADJUNTOS:</H2>" >> "'+option2+'.html"')
        os.system("python3 buscadoc.py '"+option2+"'")
        os.system('echo "<h2>CUERPO DEL CORREO:</H2>" >> "'+option2+'.html"')
        os.system("cat ficheros/textfile0 >> '"+option2+".html'")
        os.system('echo "</br>" >> "'+option2+'.html"')
        os.system("cat ficheros/textfile1 >> '"+option2+".html'")
        os.system('echo "</br><pre>" >> "'+option2+'.html"')
       
        os.system('echo "</pre>" >> "'+option2+'.html"')
        os.system('echo "</div></section></body></html>" >> "'+option2+'.html"')
        print("Se ha realizado el análisis con éxito")
        webbrowser.open(option2+'.html', new = 2)
    
    
elif option == "2":
    os.system('echo "<h1>Reporte del análisis realizado </h1></br>" > reporte.html')
    os.system('echo "</br><h2>ANÁLISIS DE FICHEROS ADJUNTOS:</H2></br>" >> reporte.html')
    os.system("python3 buscadoc.py reporte")
    os.system('echo "</br>" >> reporte.html')
    print("Se ha realizado el análisis con éxito")
    webbrowser.open('reporte.html', new = 2)

else: 

    print ("Introduce una opción válida")



