#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, bs4, re, time, json
from pprint import pprint

# MAIN URL VARIABLES
BASE_URL = "http://pyside.github.io/docs/pyside/PySide/QtGui/"
url = BASE_URL + 'index.html'

#
# Define a function to show progress on terminal
#

def update_progress(progress, total=100.):
    import sys
    total = float(total)
    progress_percentage = (progress/total)*100.
    print "\r[{0}{1}] {2:.2f}%".format("#"*(int(progress_percentage/10))," "*(int(10-progress_percentage/10)), progress_percentage),
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

#
# Define function that gets links from the Table of Contents
#

def get_links(obj_index):
	obj_links = dict()

	for (i, link) in enumerate(obj_index.find_all('a')):
		print i, link.string, link['href']
		obj_links[link.string] = BASE_URL + link['href']

	return obj_links

#
# Define function to get into the links of TOC and get inherited objects
#

def get_inherited(url):
	inherited_obj_links = dict()

	soup = make_soup(url)

	strong_tag = soup.find('strong')
	if strong_tag.text.lower() == 'inherited by:':
		#print "children"
		inherited_obj_links["children"] = "TRUE"
		inherited_p_tag = strong_tag.find_next_siblings('a')
		
		for (i, link) in enumerate(inherited_p_tag):
			print i, link.string
			inherited_obj_links[link.string] = BASE_URL + link['href']
	
	else:
		#print "no_children"
		inherited_obj_links["children"] = "FALSE"

	return inherited_obj_links
	

def main():
	

	obj_index = get_toc(url)
	obj_links = get_links(obj_index)

	num_links = len(obj_links.keys())-1
		update_progress(i, num_links)
	with open("objects.txt", "w") as obj_file:
		
		for (i, obj_name) in enumerate(obj_links.keys()):
			try:
				url_of_obj = obj_links[obj_name]
				print obj_name
				obj_file.write(obj_name + "\n")

				update_progress(i, num_links)
				pprint(get_inherited(url_of_obj))

				for obj_child in get_inherited(url_of_obj).keys():
					obj_file.write(str(obj_child) + " ")

				raw_input()
			except KeyboardInterrupt:
				break

	# pprint(obj_links)
	#get_inherited("http://pyside.github.io/docs/pyside/PySide/QtGui/QAbstractButton.html#qabstractbutton")


if __name__ == '__main__':
    main()