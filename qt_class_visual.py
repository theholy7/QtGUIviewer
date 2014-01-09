import requests, bs4, re, time
from pprint import pprint

# MAIN URL VARIABLES
BASE_URL = "http://pyside.github.io/docs/pyside/PySide/QtGui/"
url = BASE_URL + 'index.html'

def p_tag_after_h1_tag(tag, elemento):
    	return tag.previous_element is elemento 

def get_toc(url):


#
# Define function to get websites content
#

def make_soup(url):
	response = requests.get(url)
	
	soup = bs4.BeautifulSoup(response.content)

	return soup

	
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