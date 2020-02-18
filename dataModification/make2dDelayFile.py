import csv
import os

def removeTwoFrist(inFile):
    """
    Remove journey number and arrival at Slussen for every trip
    (two first columns in txt-file are removed)
    """
    begin = 2
    end = 11
    outfile = "mod" + infile

    with open(inFile, "r") as file_in:
        with open(outfile, "a") as file_out:
            writer = csv.writer(file_out)

            for row in csv.reader(file_in):
                #print(row)
                list = row[begin:end]
                line = ','.join(list)
                file_out.write(line + '\n')

def fillGaps(inFile):  #replace 3000-values with the mean of the elements to the left and right
    """
    Replace 3000-values with the mean of the values on either side of this one
    """
    with open(inFile) as file_in:
        outFile = "filled" + inFile
        with open(outFile, 'a') as file_out:
            for row in csv.reader(file_in):
                unfilledList = list(map(int, row))
                first = 0
                last = 0
                pos = 0
                while pos < 9:  #loop over all 9 delays
                    temp = unfilledList[pos]
                    if temp == 3000:
                        mean = first
                        while last < 9 and unfilledList[last] == 3000:
                            last += 1
                        if last != 9:
                            mean = (unfilledList[last] + first)/2

                        rep = [mean for i in range(last-pos)]
                        unfilledList[pos:last] = rep

                    pos = last if last > pos else pos+1
                    first = unfilledList[pos - 1]
                    last = pos

                filledList = list(map(str, unfilledList))
                filledList = ','.join(filledList)
                file_out.write(filledList + '\n')




def toDelayFile(inFile):
    """
    Make a delay(difference) file from the 2dCollect data
    """
    removeTwoFrist(inFile)
    modfile = "mod" + inFile
    fillGaps(modfile)
    outfile = "filled" + modfile
    with open(outfile) as file_in:
        delFile = "delays" + inFile
        with open(delFile, 'a') as file_out:
             for row in csv.reader(file_in):
                rlist = list(map(float, row))
                delList = []
                for i in range(8):
                    delList.append(rlist[i+1] - rlist[i])
                delList = list(map(str, delList))
                delList = ','.join(delList)
                file_out.write(delList + '\n')

    #REMOVE EXTRA FILES
    path = "C:\\Users\\peran\\PycharmProjects\\MatMod\\manipulateData"
    files = [modfile, outfile]
    for file in files:
        tempPath = os.path.join(path, file)
        os.remove(tempPath)


#infile = "testFile.txt"
#toDelayFile(infile)
























