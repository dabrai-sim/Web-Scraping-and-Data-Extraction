#Get the page https://www.python.org/ via functionality provided in the requests module in Python.

#setting website to scrape
url_py="https://www.python.org/"
response_py=requests.get(url_py)
print(response_py)

#creating a parsing object
html_py=response_py.content
Soup=BeautifulSoup(html_py,"html.parser")

#extract all the URLs that are nested within li tags
li_tag_list=[i.get('href') for i in Soup.find_all(['li','a'])]
url_list=[url for url in li_tag_list if 'https' in str(url)]
url_list

#list of all the h1, h2, h3 tags from the webpage
for tag in Soup.find_all('h1'):
  print(tag)

for tag in Soup.find_all('h2'):
  print(tag)

for tag in Soup.find_all('h3'):
  print(tag)

#extract all the text from the given web page
print(Soup.get_text())

#find and print all li tags of a given web page.
for tag in Soup.find_all('li'):
  print(tag)
