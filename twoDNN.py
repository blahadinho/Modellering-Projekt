import numpy as np
from io import StringIO
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import math
from manipulateData import makeTrainingTestSet, makeTrainingTestSetWS

'''
#READ DELAY-DATA TO ARRAY data
data = open("modDifferences.txt").read()
data = np.genfromtxt(StringIO(data))
#print(data)

#ÄNDRA HUR VI NORMERAR
maxElem = np.amax(data)
print(maxElem)
data = data/maxElem

#CREATE INPUT-OUTPUT MATRICES input and output
depBusses = 10  #specify bus-dependence

rows = len(data) - depBusses  #number of total datapoints

input = np.empty([rows, depBusses])  
#output = np.empty([1, rows])
output = np.empty([rows, 1])

for i in range(0, rows):  #traverse all delays
    tempRow = []
    for j in range(i, i+depBusses):  #group busses into groups of depBusses (numbers)
        tempRow.append(data[j])
    input[i] = tempRow  #append to input matrix
    #output[0][i] = data[i+depBusses]
    output[i] = data[i + depBusses]
'''
#DATA WITH STATION INFORMATION
'''
#Random split
#allData = open("allData.txt").read
[input, output] = makeTrainingTestSet.toTrainTest("allData.txt")

#these are numpy-arrays
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.2, random_state=42)
'''
'''
#Predeterment test/train data
[input_train, output_train] = makeTrainingTestSet.toTrainTest("trainData.txt")
[input_test, output_test] = makeTrainingTestSet.toTrainTest("testData.txt")
'''

#DATA WITHOUT STATION INFORMATION

#Random split
#allData = open("allData.txt").read
[input, output] = makeTrainingTestSetWS.toTrainTest("allData.txt")

#these are numpy-arrays
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.2, random_state=42)

'''
#Predeterment test/train data
[input_train, output_train] = makeTrainingTestSetWS.toTrainTest("trainData.txt")
[input_test, output_test] = makeTrainingTestSetWS.toTrainTest("testData.txt")
'''
#print(np.shape(X_train))  #206 x 10
#print(np.shape(y_train))  #206 x 1
#print(np.shape(X_test))  #52 x 10
#print(np.shape(y_test))  #52 x 1

clf = MLPRegressor(solver='lbfgs', alpha=0.1, hidden_layer_sizes=(5,2), random_state=1, learning_rate='adaptive')
clfFit = clf.fit(input_train, output_train)


output_test = np.transpose(output_test)
output_train = np.transpose(output_train)

trainPredict = clfFit.predict(input_train)  #numpy array

#CALCULATE RSM OF PREDICTION AND TRUE VALUES (TRAINING)
diftr = trainPredict - output_train
diftr = np.transpose(diftr)
#print("dif.shape(): ", np.shape(dif))
print()
rmsTraining = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, diftr))))/len(trainPredict))
print("Train: ", len(trainPredict))
print("rms of training data: ", rmsTraining)
print()

#CALCULATE RSM OF PREDICTION AND TRUE VALUES (TEST)
testPredict = clfFit.predict(input_test)
difte = testPredict - output_test
difte = np.transpose(difte)
#print("dif: ", dif)
rmsTest = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difte))))/len(testPredict))
print("Test: ", len(testPredict))
print("rms of test data: ", rmsTest)
print()

#print("len of ytrain: ", len(y_train))

#CREATE BASEMODEL
baseTrain = np.zeros((len(output_train), 1))#/maxElem
difbtr = baseTrain - output_train
difbtr = np.transpose(difbtr)
rmsBTr = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difbtr))))/len(trainPredict))
print("baseTrain: ", len(trainPredict))
print("baseTrain vs y_train: ", rmsBTr)
print()

baseTest = np.zeros((len(output_test), 1))#/maxElem
difbte = baseTest - output_test
difbte = np.transpose(difbte)
rmsBTe = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difbte))))/len(testPredict))
print("baseTest: ", len(testPredict))
print("baseTest vs y_test: ", rmsBTe)