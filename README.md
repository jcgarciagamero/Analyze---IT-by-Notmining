# Analyze---IT-by-Notmining
Mail analyzer script with oletools, Notmining and Virustotal

Modificar el fichero Virustotal.py e introducir clave de API

sudo apt install python3-pip
sudo -H pip3 install -U oletools
sudo apt-get install ripmime
pip3 install virustotal-api
apt-get install libemail-outlook-message-perl
sudo apt-get install git
git clone https://github.com/SpamScope/mail-parser.git
cd mail-parser
sudo python3 setup.py install
Crea la carpeta ficheros en el directorio donde estén los scripts de python.

Instrucciones para analizar un correo:

1 Introducir el correo con extensión .msg o .eml en la carpeta ficheros

Instrucciones para analizar ficheros:

1 Introducir los ficheros a analizar en la carpeta ficheros.

Ejecuta el script analisis.py: python3 analisis.py
