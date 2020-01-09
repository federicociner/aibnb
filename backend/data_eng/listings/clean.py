#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from  utils import *
import dask.dataframe as dd
from dask.distributed import Client
client = Client(processes=False)


# path
datadir = getDirectory("/data")
# get all
filenames =  getFiles("*listings.csv.gz", datadir)

for fname in filenames:

	try:
		# read csv
		df= dd.read_csv(fname, dtype=dtypes, compression="gzip", engine="python",  encoding='utf-8', assume_missing=True, sample=1024*1024, error_bad_lines=False)
		# select needed feilds
		data = df[selected]
		# load df in RAM
		data = client.persist(data)
		#- Write to csv, replace null by nan, no index
		data.repartition(npartitions=1).to_csv(str(fname)+'_*.csv', na_rep='nan', index=False)

	except Exception as e:
		print(e)

print ("Done")
