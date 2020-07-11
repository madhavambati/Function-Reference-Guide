from selenium import webdriver
from PIL import Image
from PIL import Image
import pandas as pd

basewidth = 500

global df

df = pd.read_csv("html.csv", sep=',', encoding='cp1252')
def resize(img, basewidth):
	
	
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	return img



def get_image(tag, link):

	

	
	driver = webdriver.Firefox(executable_path='C:/Users/HP/Downloads/geckodriver-v0.26.0-win64/geckodriver');
	driver.get(link);
	element = driver.find_element_by_id("iframeResult");
	location = element.location;
	size = element.size;
	driver.save_screenshot("test.png");

	# crop image
	x = location['x'];
	y = location['y'];
	width = location['x']+size['width'];
	height = location['y']+size['height'];
	im = Image.open('test.png')
	im = im.crop((int(x), int(y), int(width), int(height)))

	im = resize(im, basewidth=500)

	path = "C:/Users/HP/Documents/python/Scripts/app/images/"+str(tag)+".png"
	im.save(path)

	driver.quit()

	print(path)

	return path



file = open("html_links.txt", "r")
f2 = open('unfinished.txt', 'a')
con = file.read()
links = con.split("\n")
idx = range(len(links))

for i in idx:

	try:
		
		tag = df['name'][i]
		link = links[i].strip()

		print(str(tag) + " done ")
		path = get_image(tag, link)
		df['path'][i] = path

	except:
		print(links[i])
		f2.write(links[i]+'\n')


df.to_csv("images.csv")
df.to_csv("test.csv")
