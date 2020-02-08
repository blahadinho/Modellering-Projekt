import numpy as np
import os
import matplotlib as plt
from io import StringIO
from sklearn.neural_network import MLPRegressor
# C:\Users\peran\Anaconda3\pkgs\scikit-learn-0.21.3-py37h6288b17_0\Lib\site-packages\sklearn\datasets\data

data = open('2020-02-01_Sofia_2.txt').read()
data = np.genfromtxt(StringIO(data), delimiter=",")
nrBusses = 10
rows = np.size(data, 0) - nrBusses

X = np.empty([rows, 20])  #input data
y = np.empty([1, rows])  #output data

for i in range(0, rows):  #traverse all busses
    tempRow = np.array([data[i][1], data[i][3]])
    for j in range(i+1, i+nrBusses):  #group busses of 10
        tempRow = np.append(tempRow, data[j][1])
        tempRow = np.append(tempRow, data[j][3])
    X[i] = tempRow  #append to input matrix
    y[0][i] = data[i+nrBusses][3]

y = y[0]  #y is a (1 x rows) row-matrix

clf = MLPRegressor(solver='lbfgs', alpha=0.01, hidden_layer_sizes=(20, 10), random_state=1, learning_rate='adaptive')
clfFit = clf.fit(X, y)
#score = clf.predict([[2., 2.], [-1., -2.]])


# CREATE TEST SET
testX = np.empty([2, 20])

testY = np.empty([1, 2])

for i in range(10, 12):
    tempRow = np.array([data[i][1], data[i][3]])
    for j in range(i+1, i+nrBusses):  #group busses of 10
        tempRow = np.append(tempRow, data[j][1])
        tempRow = np.append(tempRow, data[j][3])
    testX[i-10] = tempRow  #append to input matrix
    testY[0][i-10] = data[i+2][3]

testY = testY[0]  #y is a (1 x rows) row-matrix

pred = clfFit.predict(testX)
print("Prediction: ", pred)
print("True result: ", testY)

#print(testX)
#print(testY)


 




































