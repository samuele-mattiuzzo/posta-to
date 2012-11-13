#!/usr/bin/python
from subprocess import call
import os, shutil

"""
	ALIGN LIBS SCRIPT:

	Requirements:
	- svn
	- git
	- mercurial
	- python
	
	This script automatically clones (either with git or hg) the requirements inside a
	temporary folder and copies the libraries into the main application folder.
	Cleans up at the end and removes the tmp/ directory.
"""


BASE_PATH = "tmp"   # temporary folder for cloning and copying
PROJECT_PATH = ".." # project folder


## Libs folders (comment to avoid copying)
FOLDERS = [
	("djangoappengine/djangoappengine", "djangoappengine"),
	("django-nonrel/django", "django"),
	("djangotoolbox/djangotoolbox", "djangotoolbox"),
	("django-autoload/autoload", "autoload"),
	("django-dbindexer/dbindexer", "dbindexer"),
	("django-filetransfers/filetransfers", "filetransfers"),
	("trunk/tagging", "tagging"),
]

## Repositories (with type associated)
REPOS = [
	("git", "https://github.com/django-nonrel/django-nonrel.git"),
	("git", "https://github.com/django-nonrel/djangoappengine.git"),
	("git", "https://github.com/django-nonrel/djangotoolbox.git"),
	("hg", "https://bitbucket.org/twanschik/django-autoload"),
	("git", "https://github.com/django-nonrel/django-dbindexer.git"),
	("hg", "https://bitbucket.org/wkornewald/django-filetransfers"),
	#("svn", "http://django-tagging.googlecode.com/svn/trunk/"),
]

def main():

	# creating temp directory
	if not os.path.exists(BASE_PATH):
    		os.makedirs(BASE_PATH)

	os.chdir(BASE_PATH)

	# cloning process
	for r in REPOS:
		action = "checkout" if "svn" in r[0] else "clone"
		call([r[0], action, r[1]])		
	
	os.chdir("..")

	# copying the needed libs
	for f in FOLDERS:
		start = os.sep.join([BASE_PATH, f[0]])
		dest = os.sep.join([os.getcwd(), PROJECT_PATH, f[1]])
		
		if not os.path.exists(dest):
			shutil.copytree(start, dest)

	# removing temp directory
	if os.path.isdir(BASE_PATH):
        	shutil.rmtree(BASE_PATH)


if __name__=="__main__":
	main()
