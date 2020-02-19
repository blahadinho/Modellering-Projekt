import os
import numpy as np
from numpy import genfromtxt
from manipulateData import make2dDelayFile

def toTrainTest(inFile):
    """
    From inFile, create input and output matrices for train_test_split()
    Returns input-, outputmatrix of sizes (#stations-2)*4 and (#stations-2)*1.
    """

    make2dDelayFile.toDelayFile(inFile)
    delFile = "delays" + inFile
    data = np.genfromtxt(delFile, delimiter= ",")  #read data into numpy array

    rows = len(data) - 2  #number of rows we pick outputs from
    cols = len(data[1]) - 2

    input = np.empty((rows * cols, 4))*0  #initiate input and output matrices
    output = np.empty((rows * cols, 1))*0

    #FILL INPUT AND OUTPUT MATRICES
    count = 0
    for row in range(2,rows + 2):
        for col in range(6):
            tempIn = [data[row-2][col+2], data[row-1][col+2], data[row][col], data[row][col+1]]
            input[count] = tempIn
            output[count] = data[row][col+2]
            count += 1

    path = "C:\\Users\\peran\\PycharmProjects\\MatMod\\manipulateData"
    path = os.path.join(path, delFile)
    os.remove(path)  #remove the temporary delayFile

    return input, output

















