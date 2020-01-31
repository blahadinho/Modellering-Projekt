from bs4 import BeautifulSoup
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import time

req = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=8c788c72e4414669972b2392b9cbbc46&siteid=9192&timewindow=5')

xml = BeautifulSoup(req, 'xml')

open('testfile.txt')

destinations = []

for item in xml.findAll('Bus'):
    #destinations.append(item.text)
    #print("Destination: " + str(item.text))
    #while(item.has)
    print(item.name)
    dest = item.find('Destination')

    print(dest.text)
    destinations.append(dest)

print('\n')
#for d in destinations:
#    print(d)

destinations.write('testfile.txt')



















