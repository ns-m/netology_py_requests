#pip install yadisk
import yadisk
import zipfile
import os

arh = zipfile.ZipFile('outfiles.zip', 'w')
for root, dirs, files in os.walk('Outfiles'):
    for file in files:
        arh.write(os.path.join(root,file))

arh.close()

ya = yadisk.YaDisk(token="")

try:
    ya.remove("/outfile.zip", permanently=True)
except:
    ya.upload('outfiles.zip', "/outfile.zip")
