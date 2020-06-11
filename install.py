import os
from zipfile import ZipFile

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("pip install selenium")

os.chdir('sele')
with ZipFile("chromedriver_win32.zip", "r") as zip:
    zip.extractall()