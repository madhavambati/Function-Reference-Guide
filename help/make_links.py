import pandas as pd
import numpy as  np
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import bs4
import urllib.request

file = open("html_links.txt", "r")
f2 = open('unfinished.txt', 'a')
con = file.read()
links = con.split("\n")
idx = range(len(links))


