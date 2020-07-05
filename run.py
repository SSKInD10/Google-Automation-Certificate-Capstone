#!/usr/bin/env python3
import os,requests
src = 'supplier-data/descriptions/'
for i in os.listdir(src):
	with open(os.path.join(src,i),'r') as fptr:
		dict = {}
		dict["name"] = fptr.readline()
		dict["weight"] = int((fptr.readline())[:-5])
		dict["description"] = fptr.readline()
		dict["image_name"] = i.replace('.txt','.jpeg')
		response = requests.post("http://localhost/fruits/",data=dict)
