#!/usr/bin/env python3


# -*- coding: utf-8 -*-

import re
import csv
from  utils import *
datadir = getDirectory("/data")
filenames =  getFiles("*reviews.csv.gz", datadir)
openedfiles = openFiles(filenames)
lines = streamFiles(openedfiles)

with open('/data/reviews.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	try:
		for line in lines:
			line = line[:-1]
			line = line.strip()
			if not line:
				continue
			else:
				l = line.decode("utf-8")
				prog = re.compile(r'(^\d+),(\d+),(\d+-\d+-\d+),(\d+),(\w+),(.*)')
				result = re.findall(prog,l)
				for a,b,c,d,e,f in result:
					g = re.sub('[ ](?=[ ])|[^-_,A-Za-z0-9 ]+', "", e)
					h = re.sub('[ ](?=[ ])|[^-_,A-Za-z0-9 ]+', "", f)
					h1  = h.replace(',', ' ')
					row = [str(a),str(b),str(c),str(d),str(g),str(h1)]
					try:
						writer.writerow(row)
					except Exception as e:
						continue

	except Exception as e:
		print(e)
csvFile.close()
print ("Done")
