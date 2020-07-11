import pandas as pd
import numpy as  np
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import bs4
import urllib.request

def get_params(soup):
	params = ""
	nextNode = soup.find_all('h2')[1]
	while True:
		nextNode = nextNode.nextSibling
		if nextNode.name == 'h2':
			break
		else:
			#print(type(nextNode))
			if isinstance(nextNode, bs4.element.Tag):
				params = params + nextNode.text.strip()
	return params


def make_DB(url, df, i):

	web = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(web, 'lxml')
	h1 = soup.findAll('h1')[0]
	h2 = soup.find_all('h2')
	eg = h2[1].findNext('pre').text.strip()

	
	df['name'][i] = h1.text[3:].strip()
	df['desp'][i] = h1.findNext('h4').text.strip()
	df['module'][i] = soup.find_all('span', {'class' : 'breadcumb__label'})[2].text.strip()
	df['synx'][i] = h2[0].findNext('pre').text.strip()
	df['example'][i] = eg
	df['parameter'][i] = get_params(soup)
	df['output'][i] = soup.findAll('samp')[0].text.strip()
	return df

#soup = scrape("https://www.programiz.com/cpp-programming/library-function/cmath/remainder")
columns = ['name','desp', 'example', 'synx', 'parameter', 'output', 'module']
file = open("test_links.txt", "r")
f2 = open('unfinished.txt', 'a')
con = file.read()
links = con.split("\n")
idx = range(len(links))
df = pd.DataFrame(columns=columns, index=idx)


#df = make_DB(links[0], df, 0)

#print(df['example'][0])



for i in idx:
	
	#print(links[i])
	#print(i)
	try:
		df = make_DB(links[i], df, i)
		print(i)
	except:
		print(links[i])
		f2.write(links[i]+'\n')
		


df.to_csv("test.csv", index=False)





#print(df['output'][0])



