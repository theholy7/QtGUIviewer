import requests, bs4, re, time
from pprint import pprint

# MAIN URL VARIABLES
BASE_URL = "http://pyside.github.io/docs/pyside/PySide/QtGui/"
url = BASE_URL + 'index.html'


def get_toc(url):
	response = requests.get(url)
	
	soup = bs4.BeautifulSoup(response.content)
	
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



def main():
	

	obj_index = get_toc(url)
	obj_links = get_links(obj_index)

	pprint(obj_links)


if __name__ == '__main__':
    main()