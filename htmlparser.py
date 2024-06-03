from bs4 import BeautifulSoup

# Set up our soup object
f = open("wikipedia_page.html", "r", encoding="utf8")
html_doc = f.read()
soup = BeautifulSoup(html_doc)

# Finds all links in the document
def getLinks(soup):
    for link in soup.find_all('a'):
        print(link.get('href'))



getLinks(soup)