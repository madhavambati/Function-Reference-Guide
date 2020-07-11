from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import urllib.request
import pandas as pd
web = urllib.request.urlopen("https://www.w3schools.com/python/python_syntax.asp").read()
soup = BeautifulSoup(web, 'html.parser')

over = []
heads = []
paras = []

for node in soup.findAll(['h2', 'p']):
	
	if node.name == 'h2':
		head = node.text.rstrip()
	
    
	elif node.name == 'p':
		
		
		over.append((head,node.text.rstrip('\n')))
		
#print(over)

hp = dict()
for student,score in over: 
    hp.setdefault(student, []).append(score) 
#print(dict_1) 
#print(heads)
#print(paras)
print(hp)

over2 = []
cl = soup.findAll('div', {"class": "w3-example"})

for i in cl:
	#print(i.find_previous_sibling('p').text)
	#print(i.text)

	l = i.text.strip('\n')
	

	over2.append((i.find_previous_sibling('p').text, l))

#print(over2)
pe = {}
for student,score in over2: 
    pe.setdefault(student, []).append(score)

print(hp)
print(pe)

df = pd.DataFrame(hp.items(), columns=['h', 'p'])
