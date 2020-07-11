import pandas as pd
import numpy as  np
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import bs4
import urllib.request


root_link = "https://www.programiz.com"
file = open("links.txt", "a")

def scrape(url):
	web = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(web, 'lxml')
	return soup

soup = scrape(root_link + "/cpp-programming/library-function")

for i in range(1,15):
	main_class = "view view-c-library-functions-homepage view-id-c_library_functions_homepage view-display-id-attachment_"+ str(i) + " attachment-views-individual"
	divs = soup.findAll("div", {"class": main_class})
	subdivs = divs[0].findAll("div", {"class": "reference-data--row"})

	for a in subdivs:
		file.write(root_link + a.find("a")["href"].strip() + '\n')
		
		print(root_link + a.find("a")["href"].strip())
