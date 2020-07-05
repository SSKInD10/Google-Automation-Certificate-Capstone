#!/usr/bin/env python3
import os
from multiprocessing import Pool
from PIL import Image
def imgconv(src):
	with Image.open(src).convert("RGB") as im:
		im.resize((600,400)).save(src.replace('tiff','jpeg'),format = "JPEG")
if __name__ == "__main__":
	src = "supplier-data/images/"
	for root,dirs,files in os.walk(src):
		for name in files:
			if name[-4:] != 'tiff':
				continue
			srcs = os.path.join(root,name)
			imgconv(srcs)
		break
