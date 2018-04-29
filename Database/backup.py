#!/usr/bin/env python

import sys, datetime, time, os

def main():
	if (len(sys.argv) != 3):
		sys.stderr.write("Missing collection name and path")
		exit(84);
	collection = sys.argv[1]
	path = sys.argv[2]
	date = datetime.datetime.now()
	date = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
	fileName = path + date + "-" + collection + ".json"
	os.system("mongoexport --db 'LeanConnectedServicePlatform' --collection " + collection + " --out " + fileName)

main()