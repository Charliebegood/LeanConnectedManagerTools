#!/usr/bin/env python

import sys, os

def main():
	if (len(sys.argv) != 3):
		sys.stderr.write("Missing collection name and path")
		exit(84);
	collection = sys.argv[1]
	path = sys.argv[2]
	os.system("mongoimport --db 'LeanConnectedServicePlatform' --collection " + collection + " --file " + path)

main()