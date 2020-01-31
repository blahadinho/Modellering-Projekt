from urllib.request import urlopen
from xml.etree.ElementTree import parse
import xml.dom.minidom

var_url = urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=72aa2ba7cbc04b01a59fc07e81f6825c&siteid=9192&timewindow=6')

doc = xml.dom.minidom.parse(var_url)


print(doc.nodeName)
name = doc.getElementsByTagName("Bus")
for item in name:
    Des = item.getElementsByTagName("Destination")
    print(Des.childNode)
    print(item.childNodes)
