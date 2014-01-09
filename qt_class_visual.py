#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, bs4, re, time
from pprint import pprint

# MAIN URL VARIABLES
BASE_URL = "http://pyside.github.io/docs/pyside/PySide/QtGui/"
url = BASE_URL + 'index.html'

def p_tag_after_h1_tag(tag, elemento):
    	return tag.previous_element is elemento 
#
# Define a function to show progress on terminal
#

def get_toc(url):
def update_progress(progress):
    import sys
    print "\r[{0}{1}] {2}%".format("#"*(progress/10)," "*(10-progress/10), progress),
    sys.stdout.flush()


#
# Define function to get websites content
#

def make_soup(url):
	response = requests.get(url)
	
	soup = bs4.BeautifulSoup(response.content)

	return soup

#
#  Define function to get Table of Contents
#

def get_toc(url):
	soup = make_soup(url)
	
	obj_index = soup.find("tr", "row-odd")

	return obj_index

def get_links(obj_index):
	i=0
	obj_links = dict()

	for link in obj_index.find_all('a'):
		print i, link.string, link['href']
		obj_links[link.string] = BASE_URL + link['href']
		i+=1

	return obj_links

def get_inherited(url):
	soup = make_soup(url)
	

	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.content)

	strong_tag = soup.find_all('strong')
	for strong in strong_tag:
		print strong

def main():
	

	# obj_index = get_toc(url)
	# obj_links = get_links(obj_index)

	# pprint(obj_links)
	get_inherited("http://pyside.github.io/docs/pyside/PySide/QtGui/QAbstractButton.html")


if __name__ == '__main__':
    main()