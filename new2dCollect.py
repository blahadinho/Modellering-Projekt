from bs4 import BeautifulSoup
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import time
import textwrap
import winsound
import os

#HELP METHODS
def calcError(old, new):  #return error between times old and new
    old = textwrap.wrap(old, 2)
    old = list(map(int, old))
    oldT = old[0] *3600 + old[1] * 60 + old[2]

    new = textwrap.wrap(new, 2)
    new = list(map(int, new))
    newT = new[0] * 3600 + new[1] * 60 + new[2]

    return str(newT - oldT)

def placeInFile(fileName, journey):  #return index of journey in fileName, -1 if not in file
    place = -1
    try:
        with open(fileName, 'r') as f:
            lines = f.readlines() #list containing the lines in testFile.txt
            for i, line in enumerate(lines):
                if line.startswith(journey):
                    place = i
                    break
        return place
    except:
        with open(fileName, 'a') as f:
            f.write("")
        return place


def newJourney(fileName, line):
    with open(fileName, 'a') as f:
        f.write(','.join(str(i) for i in line) + '\n' )


def appendToJourney(fileName, place, delay):  #append delay to journey in row (row) in fileName
    with open(fileName, 'r+') as f:
        lines = f.readlines()
        #print("delay: ", type(delay))
        #print(lines[place])
        lines[place] = lines[place][:-1] + "," + delay + "\n"
        f.seek(0)
        for line in lines:
            f.write(line)

stations = ["Slussen", "Medborgarplatsen", "Nytorgsgatan", "Åsögatan", "Gotlandsgatan", "Södermannagatan", "Skanstull",
            "Eriksdal", "Rosenlund"]
indices = [2, 3, 4, 5, 6, 7, 8, 9, 10]
statDic = dict(zip(stations, indices))  #dictionary for ordering sthe stations by index

journeyDic = {}  #read in the current values (useful if the program temporarily crashes)
with open("2020-02-14.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(",")  #create list of words in line
        key = line[0]

        #create key-value (which is a list)
        value = [3000 for i in range(0,11)]
        for i in range(0, len(line)):
            value[i] = line[i].strip()

        journeyDic[key] = value  #append key-value pair to dictionary


print("Collecting data..")

t = time  #in order to get data from URL every 20 seconds

while(True):
    startTime = time.time()

    try:  #try loading page with data
        #print("Fetching data")
        reqSlussen = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=9192&timewindow=4')
        reqMedborgarplatsen = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=9191&timewindow=4')
        reqNytorgsgatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1327&timewindow=4')
        reqÅsögatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1308&timewindow=4')
        reqGotlandsgatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1312&timewindow=4')
        reqSödermannagatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1311&timewindow=4')
        reqSkanstull = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=9190&timewindow=4')
        reqEriksdal = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1352&timewindow=4')
        reqRosenlund = urllib.request.urlopen(
            'https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1351&timewindow=4')
    except:  #sleep ten seconds before refreshing
        print("Nu kunde sidan inte hämtas")
        winsound.PlaySound("Crash-Cymbal-1.wav", winsound.SND_FILENAME)
        t.sleep(20)
        reqSlussen = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=9192&timewindow=4')
        reqMedborgarplatsen = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=540b26d4e7bf4b8bbcf9a808c357dcbc&siteid=9191&timewindow=4')
        reqNytorgsgatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1327&timewindow=4')
        reqÅsögatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1308&timewindow=4')
        reqGotlandsgatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1312&timewindow=4')
        reqSödermannagatan = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1311&timewindow=4')
        reqSkanstull = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=9190&timewindow=4')
        reqEriksdal = urllib.request.urlopen('https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1352&timewindow=4')
        reqRosenlund = urllib.request.urlopen(
            'https://api.sl.se/api2/realtimedeparturesV4.xml?key=40b33d715cc44637944291785efcf849&siteid=1351&timewindow=4')
        print("Det löste sig")
        winsound.PlaySound("FANFARE.wav", winsound.SND_FILENAME)

    #collect all requests in one list
    requests = [reqSlussen, reqMedborgarplatsen, reqNytorgsgatan, reqÅsögatan, reqGotlandsgatan, reqSödermannagatan,
                reqSkanstull, reqEriksdal, reqRosenlund]
    i = 0
    for req in requests:  #traverse requests
        i = i + 1
        xml = BeautifulSoup(req, 'xml')

        for bus in xml.findAll('Bus'):
            #temporary bus values
            tempDest = bus.find('Destination').text
            tempLine = bus.find('LineNumber').text
            dispTemp = bus.find('DisplayTime').text
            journey = bus.find('JourneyNumber').text
            station = bus.find('StopAreaName').text

            if dispTemp == "Nu" and tempDest == "Södersjukhuset" and tempLine == "3":  #control that it's a bus on bus line 3

                date = bus.find('TimeTabledDateTime').text[0:10]

                #calculate bus delay
                ttdt = bus.find('TimeTabledDateTime').text[11:]
                ttdt = ttdt.replace(':', '')
                edt = bus.find('ExpectedDateTime').text[11:]
                edt = edt.replace(':', '')
                delay = calcError(ttdt, edt)  #string

                fileName = date + ".txt"

                exists = journey in journeyDic  #examine if we've already added journey to our dictionary
                if not exists:
                    jlist = [journey, edt, "3000", "3000", "3000", "3000", "3000", "3000", "3000", "3000", "3000"]
                    #if station == "Slussen":
                    jlist[i+1] = delay
                    journeyDic[journey] = jlist

                    #line = journey + "," + edt + "," + delay + "\n" #line to be written into the dataset-file
                    #newJourney(fileName, line)
                    if int(journey)-10 in journeyDic:
                        inputLine = journeyDic[journey - 10]
                        newJourney(fileName, inputLine)

                    #winsound.PlaySound("FANFARE.wav", winsound.SND_FILENAME)

                else:
                    #jlist[i+1] = delay
                    #print("-----------------------------------------")
                    #print("Fetched station, journey: ", station, journey)
                    index = statDic[station]
                    #print("TTDT: ", ttdt)
                    #print("EDT: ", edt)
                    #print("Journey delay: ", delay)
                    #print("value for journey/station in dictionary: ", journeyDic[journey][index])
                    empty = journeyDic[journey][index] == "3000"
                    if empty:
                        journeyDic[journey][index] = delay
                        #place = placeInFile(fileName, journey)
                        #appendToJourney(fileName, place, delay)

                        #print("appended " + delay + " to " + journey + "/" + station + " successfully")
                    #print("-----------------------------------------")

                '''
                
                place = journeyInFile(fileName, journey)
                
                if place == -1:
                    with open(fileName, 'a') as f:
                        f.write(journey + "," + edt + "," + delay + "\n")
                else:
                    appendToJourney(fileName, place, delay)
                '''
            #if i == 9:
             #   newJourney(fileName, jlist)

    finishTime = time.time()

    totTime = finishTime - startTime
    print("Total time for one iteration: ", totTime)  #between 1.4-12 seconds
    #if(input() == "q"):
    #    break
    t.sleep(5)

for e in journeyDic.values():
    newJourney(fileName, e)


    


    




















