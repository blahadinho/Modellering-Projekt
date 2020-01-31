from bs4 import BeautifulSoup
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import time
import textwrap

def calcError(old, new):
    old = textwrap.wrap(old, 2)
    old = list(map(int, old))
    oldT = old[0] *3600 + old[1] * 60 + old[2]

    new = textwrap.wrap(new, 2)
    new = list(map(int, new))
    newT = new[0] * 3600 + new[1] * 60 + new[2]

    return newT - oldT


t = time  #in order to get data from URL every 5 seconds

journeys = []  #list with JourneyNumbers in order to register unique bus journeys

with open("journeys.txt", 'r') as f:  # contains every journey documented (good when re-running the program)
    lines = f.readlines()
    if len(lines) != 0:
        journeys = lines[0].split(" ")

date = "2020-01-31_"

while(True):
    req = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=8c788c72e4414669972b2392b9cbbc46&siteid=9192&timewindow=5')

    xml = BeautifulSoup(req, 'xml')

    for bus in xml.findAll('Bus'):
        #temporary bus values
        tempDest = bus.find('Destination').text
        tempLine = bus.find('LineNumber').text
        dispTemp = bus.find('DisplayTime').text
        journey = bus.find('JourneyNumber').text

        nExist = journey not in journeys

        if dispTemp == "Nu" and nExist:
            journeys.append(journey)
            ttdt = bus.find('TimeTabledDateTime').text[11:]
            ttdt = ttdt.replace(':', '')
            edt = bus.find('ExpectedDateTime').text[11:]
            edt = edt.replace(':', '')
            error = calcError(ttdt, edt)

            fileName = date + tempDest + "_" + tempLine + ".txt"

            with open(fileName, 'a') as f:  #insert data in fileName
                f.write(ttdt + ", " + edt + ", " + journey + ", " + str(error) + '\n')

            with open("journeys.txt", "a") as j:  # insert unique journey into text file
                j.write(journey + " ")

    #print('\n')
    #print(journeys)
    #for d in destinations:
    #    print(d)

    t.sleep(2)





















