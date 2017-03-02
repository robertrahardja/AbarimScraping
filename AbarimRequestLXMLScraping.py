import requests
from lxml import html

nameArray = ['Mary','Abraham']

for nameKey in nameArray:

    #get page
    page = requests.get("http://www.abarim-publications.com/Meaning/"+nameKey+".html")

    #use lxml for xpath finding text
    tree = html.fromstring(page.content)
    text = tree.xpath('//article//b/text()')

    for item in text:
        print item
