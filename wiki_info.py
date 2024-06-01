from bs4 import BeautifulSoup   #good library ngl
import requests

url = "https://en.wikipedia.org/wiki/Machine_learning#External_links"

#access the url
page = requests.get(url)
#get the soup
soup = BeautifulSoup(page.text, 'html.parser')
#title here
title = soup.title.text
print("The title of the page is", title) 

#recursive=True allows us to check the children of parent also
#.text is important as it ensures the output doesnt contain any <char>
#another plus point is that it is dyanamic, and hence can be used for any url without changing the class or any other hassle
first_para = soup.find('p', recursive=True).text

external_link_list = soup.find_all('a',rel="nofollow" ,class_="external text")

# getting the external links
stuff = soup.find_all('div',class_="sidebar-list mw-collapsible mw-collapsed")
for element in stuff:
    external_link = element.find('a').attrs["href"]
    external_link_title = element.find('a').attrs["title"]
    print(external_link)
    print(external_link_title)
    print("-----")

#getting image url and caption
figure = soup.find_all("figure")

for items in figure:
    link = items.find('a').attrs['href']
    caption = items.text
    print(link)
    print(caption)
    print("----------")