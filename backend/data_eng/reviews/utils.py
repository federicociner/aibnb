

def getDirectory(datafolder):
	import os
	data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", datafolder)
	return data_dir

def getFiles(filepattern,topdir):
    import os
    import fnmatch
    for path, dirlist, filelist in os.walk(topdir):
        for name in fnmatch.filter(filelist,filepattern):
            yield os.path.join(path,name)

def openFiles(filenames):
    import gzip, bz2
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)


def streamFiles(sources):
	for s in sources:
		linenumber = -1
		for item in s:
			linenumber +=1
			if linenumber == 0:
				continue
			else:
				yield item
