#!/usr/bin/python

'''
	Align script to copy over the folders needed
'''

import os, shutil
import sys

BASE_PATH = "/home/smau/Workspace/GitHub/DJGAE" # basefolder for django appengine libraries
PROJECT_PATH = ".."		 # project folder
FOLDERS = [			 # libraries (comment do avoid copying)
	("djangoappengine/djangoappengine", "djangoappengine"),
	("django-nonrel/django", "django"),
	("djangotoolbox/djangotoolbox", "djangotoolbox"),
	("django-autoload/autoload", "autoload"),
	("django-dbindexer/dbindexer", "dbindexer"),
]



def main():
	for f in FOLDERS:
		shutil.copytree(
			os.sep.join([BASE_PATH, f[0]]) ,			# source
			os.sep.join([os.getcwd(), PROJECT_PATH, f[1]])	# destination
		)


if __name__=="__main__":
	main()
