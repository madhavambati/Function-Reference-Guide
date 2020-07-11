from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import urllib.request
import pandas as pd
web = urllib.request.urlopen("https://docs.python.org/3/tutorial/introduction.html#strings").read()
soup = BeautifulSoup(web, 'html.parser')

over = []
heads = []
paras = []




def find_all_p(soup, text):
	over = ""
	for node in soup.findAll(['h2', 'p']):
		if node.name == 'h2':
			head = node.text.replace("\n", "").replace("\r","")

	
    
		elif node.name == 'p':
			if head == text:

				over = over + node.text.replace('\n','').replace("\r","") + " "
		
		
				

	return over



for node in soup.findAll(['h1', 'p']):
	
	if node.name == 'h1':
		head = node.text.replace("\n", "")

	
    
	elif node.name == 'p':
		
		
		over.append((head, node.text.replace('\n','')))
		
#print(over)

hp = dict()
for student,score in over: 
    hp.setdefault(student, []).append(score) 
#print(dict_1) 
#print(heads)
#print(paras)
#print(hp)

over2 = []
cl = soup.findAll('pre')

for i in cl:
	#print(i.find_previous_sibling('p').text)
	#print(i.text)

	l = i.text.replace("\n", "")
	print(l)
	

	over2.append((i.find_previous_sibling('p').text, l))

#print(over2)
pe = {}
for student,score in over2: 
    pe.setdefault(student, []).append(score)

print(hp)
print("-------------------------------------------------------------------------------------------")
print(pe)

df = pd.DataFrame(hp.items(), columns=['h', 'p'])
