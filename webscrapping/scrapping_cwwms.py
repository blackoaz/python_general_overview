from bs4 import BeautifulSoup
import requests


link = 'https://www.linkedin.com/feed/'
html = requests.get(link)

soup = BeautifulSoup(html.text,"html5lib")  
tag = soup.a
# print(tag.attrs)

# for url in soup.find_all('a'):
#     print(url.get('href'))

headers = "Product_Name,Pricing,Ratings\n"  

with open('data.xlxs','a') as file:
    file.write(headers)