

from bs4 import BeautifulSoup

import requests

url="https://en.wikipedia.org/wiki/Machine_learning"

response=requests.get(url)
response

response.text

#parsing library -html.parser and second is lxml
soup=BeautifulSoup(response.text,"lxml")

soup

for Alink in soup.find_all("a"): 
  #print(Alink)
  print(Alink.get('href'))

for ptag in soup.find_all('p'):
  # print(ptag)
  #now second loop for b tag
   for btag in  ptag.find_all("b"):
      print(btag.text)

import pandas as ps

list=[1,2,3,4]
list1=[4,7,9,1]
list2=[3,5,7,9]
df=ps.DataFrame([list,list1,list2],columns=['age','value','name','marks'])

df

