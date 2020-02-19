import numpy as np
from io import StringIO
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import math


#READ DELAY-DATA TO ARRAY data
data = open("modDifferences.txt").read()
data = np.genfromtxt(StringIO(data))
#print(data)

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

#these are numpy-arrays
X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.2, random_state=42)

#print(np.shape(X_train))  #206 x 10
#print(np.shape(y_train))  #206 x 1
#print(np.shape(X_test))  #52 x 10
#print(np.shape(y_test))  #52 x 1

clf = MLPRegressor(solver='lbfgs', alpha=0.1, hidden_layer_sizes=(1), random_state=1, learning_rate='adaptive')
clfFit = clf.fit(X_train, y_train)


y_test = np.transpose(y_test)
y_train = np.transpose(y_train)

trainPredict = clfFit.predict(X_train)  #numpy array

#CALCULATE RSM OF PREDICTION AND TRUE VALUES (TRAINING)
diftr = trainPredict - y_train
diftr = np.transpose(diftr)
#print("dif.shape(): ", np.shape(dif))
print()
rmsTraining = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, diftr))))/len(trainPredict))
print("Train: ", len(trainPredict))
print("rms of training data: ", rmsTraining)
print()

#CALCULATE RSM OF PREDICTION AND TRUE VALUES (TEST)
testPredict = clfFit.predict(X_test)
difte = testPredict - y_test
difte = np.transpose(difte)
#print("dif: ", dif)
rmsTest = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difte))))/len(testPredict))
print("Test: ", len(testPredict))
print("rms of test data: ", rmsTest)
print()

#print("len of ytrain: ", len(y_train))

#CREATE BASEMODEL
baseTrain = np.ones((len(y_train), 1))*25/maxElem
difbtr = baseTrain - y_train
difbtr = np.transpose(difbtr)
rmsBTr = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difbtr))))/len(trainPredict))
print("baseTrain: ", len(trainPredict))
print("baseTrain vs y_train: ", rmsBTr)
print()

baseTest = np.ones((len(y_test), 1))*25/maxElem
difbte = baseTest - y_test
difbte = np.transpose(difbte)
rmsBTe = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difbte))))/len(testPredict))
print("baseTest: ", len(testPredict))
print("baseTest vs y_test: ", rmsBTe)


