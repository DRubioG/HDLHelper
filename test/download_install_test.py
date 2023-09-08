import zipfile
from io import BytesIO
import requests, os

url = "https://github.com/DRubioG/HDLHelper/archive/refs/tags/0.0.zip"
req = requests.get(url)

filename = url.split('/')[-1]
with open(filename, 'wb') as output_file:
    output_file.write(req.content)

zipfile = zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall(".")

os.remove(filename)