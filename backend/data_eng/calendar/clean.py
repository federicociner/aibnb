#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import re
import csv
from  utils import *

datadir = getDirectory("/data")
filenames =  getFiles("*calendar.csv.gz", datadir)
openedfiles = openFiles(filenames)
lines = streamFiles(openedfiles)

with open('/data/calendar.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	try:
		for line in lines:
			line = line[:-1]
			line = line.strip()
			if not line:
				continue
			else:
				l = line.decode("utf-8")
				prog = re.compile(r'(^\d+),(\d+-\d+-\d+),(t|f),(.*)')
				result = re.findall(prog,l)
				for a,b,c,d in result:
					e  = d.replace('$', '')
					e1  = e.replace('"', '')
					row = [str(a),str(b),str(c),str(e1)]
					try:
						writer.writerow(row)
					except Exception as e:
						continue

	except Exception as e:
		print(e)
csvFile.close()
print ("Done")
