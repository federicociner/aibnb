#!/usr/bin/env python3


# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests
import os
from dask import compute, delayed, threaded
import datetime
T = datetime.datetime.now()
T = T.isoformat().split(':')[0]
Y,M,D = T.split("-")
# we collect monthly
cflag = str(Y)+str(M)+"00"


def scraper(url):
	html_page = requests.get(url).content
	soup = BeautifulSoup(html_page, 'lxml')
	links = []
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		a = link.get('href')
		if a.endswith("calendar.csv.gz"):
			links.append(a)
		else:
			pass
	return links

def worker(url):
	meta = url.split("/")
	y,m,d =meta[6].split("-")
	mflag = str(y)+str(m)+str(d)
	if int(mflag >= cflag):
		name =meta[3]+"_"+meta[4]+"_"+meta[5]+"_"+meta[6]+"_"+meta[8]
		fname = os.path.basename(name)
		r = requests.get(url)
		print(fname)
		with open("/data/"+fname, "wb") as f:
			f.write(r.content)
	else:
		pass

if __name__ == "__main__":
	L= scraper("http://insideairbnb.com/get-the-data.html")
	url_list = []
	try:
		for l in L:
			url_list.append(l)
	except Exception as e:
		print(e)

	values = [delayed(worker)(url) for url in url_list]
	results = compute(*values, scheduler='threads')
