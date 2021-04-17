import sys
sys.path.append("..") # Adds higher directory to python modules path.
from Data import Data
from Import.RawDataImport import RawDataImport
import xml.etree.cElementTree as ET
from xml.dom import minidom
import os
from zipfile import ZipFile
import zipfile
import re


MAIN_FOLDER_NAME = "D:\\"
#MAIN_FOLDER_NAME = "D:\\TEMSFTPREPORTTRIAL\\KMZ_RSRP5G_FTP\\DONE\\Upload to Cloud OK\\"

matches = []
x = []
for root, dirnames, filenames in os.walk(MAIN_FOLDER_NAME):

	for filename in filenames:
		if filename.endswith(('.xlsx', '.XLSX')):

			#matches.append(filename.split(".")[0].split(" ")[0].split("v2")[0].split("old")[0].split("low")[0].replace("E","Z")[-3:])
			x.append(re.search(r'\d+', filename).group(0))

			set_matches = set(matches)
	break

output = "=OR("
for i in x:
	output+= f'REGEXMATCH(F:F,"{i}"),'
output = output[:-1] + ')'
print(output)

