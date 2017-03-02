import requests
from lxml import html

//get page
page = requests.get("http://www.abarim-publications.com/Meaning/Abraham.html")

//use lxml for xpath finding text
tree = html.fromstring(page.content)
text = tree.xpath('//article//b/text()')

for item in text:
        print item
