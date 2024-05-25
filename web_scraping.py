#Get the page http://quotes.toscrape.com via functionality provided in the requests module in Python.

#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#setting website to scrape
url=" http://quotes.toscrape.com"
response=requests.get(url)
print(response)

#creating a parsing object
html=response.content
soup=BeautifulSoup(html,"html.parser")

#Find the title tag.
print(soup.title)

#retrieve all the paragraph tags
paragraph_tag = soup.find_all('p')
for tag in paragraph_tag:
  print(tag)

#extract the text in the first paragraph tag
for text in soup.p.strings:
  print(text)

#Find all the h2 tags
h2_tag = soup.find_all('h2')
for tag in h2_tag:
  print(tag)

#find the length of the text of the first h2 tag
print(soup.h2.string)

#find the text of the first a tag
print(soup.a.string)

#find the href of the first a tag
#a_tag = soup.find_all('a')
#for tag in a_tag:
#  print(tag.get('href'))
print(soup.a.get('href'))

#Quotes on quotes.toscrape.com often are categorized with tags. On the first page, create a dict for each quote using the BeautifulSoup object
quotes=[quote.string for quote in soup.find_all('span','text')]
quotes

#Using the BeautifulSoup object, get links to all author pages on the website quotes.toscrape.com. (Notice that links on this page are relative links.) Put
#these links in a list or dict. (You only need to do this for the first page of the website.)

author=[quote.string for quote in soup.find_all('small')]
author

#Put all quotes and author name in CSV file
df=pd.DataFrame(data=[],columns=['quotes','author'])
df['quotes']=quotes
df['author']=author
df.to_csv('dataset.csv')
