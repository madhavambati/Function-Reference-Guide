import pandas as pd
import numpy as np


df_html = pd.read_csv("cpp.csv")
df_html = df_html.applymap(str)

def split_string(string): 
  
    # Split the string based on space delimiter 
    list_string = string.split(':') 
      
    return list_string 
  
def join_string(list_string): 
  
    # Join the string based on '-' delimiter 
    string = '\n'.join(list_string) 
      
    return string 

j = 0
for i in df_html['parameter']:
	l = split_string(i)
	k = join_string(l)
	df_html['parameter'][j] = k
	j += 1

df_html.to_csv("copy.csv")
print(df_html)