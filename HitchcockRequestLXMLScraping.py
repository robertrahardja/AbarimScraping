import requests
from lxml import html


nameArray = ['Abana','Abba']



#nameArray = ['Aaron','Abba',]

#open file Output.txt
with open('Output.txt', 'w') as f:
    #loop through each name in dictionary
    for nameKey in nameArray:
        
        #get page
        page = requests.get("http://www.biblestudytools.com/dictionaries/hitchcocks-bible-names/"+nameKey+".html")
        
        
        #use lxml for xpath finding text
        tree = html.fromstring(page.content)
        text = tree.xpath('//blockquote/text()')
        
        #var to print with plist format
        toprint = "<key>" + nameKey + "</key><string>"
        
        #for loop to print each key with value
        for item in text:
           toprint = toprint + item + " "
        
        toprint = toprint + "</string>"
        print toprint
        #print to file
        f.write(toprint + "\n")
#close file
f.close()
