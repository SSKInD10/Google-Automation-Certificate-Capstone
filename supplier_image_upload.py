#!/usr/bin/env python3
import os
from multiprocessing import Pool
from PIL import Image
import requests
if __name__ == "__main__":
	src = "supplier-data/images/"
	url = "http://localhost/upload/"
	for root,dirs,files in os.walk(src):
		for name in files:
			if name[-4:] != 'jpeg':
				continue
			srcs = os.path.join(root,name)
			with open(srcs,'rb') as opened:
				r = requests.post(url, files={'file':opened})
