import numpy as np
from sklearn.linear_model import LinearRegression
from twoDModels import makeTrainingTestSet
from sklearn.model_selection import train_test_split
import math

inFile = "feb17.txt"
inp, outp = makeTrainingTestSet.toTrainTest(inFile)

imean = np.mean(inp)
ivar = np.sqrt(np.var(inp))
inp = (inp - imean)/ivar

omean = np.mean(outp)
ovar = np.sqrt(np.var(outp))
outp = (outp - omean)/ovar

#CREATE STOCHASTIC MODEL
X_train, X_test, y_train, y_test = train_test_split(inp, outp, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)

#CREATE PREDICTED MATRICES
intercept = model.intercept_  #intercept of LR-modell
coeffs = model.coef_[0]  #the four coefficients of the LR-modell

rowsTr = len(X_train)  #rows in matrices for prediction on training data
predTr = np.empty((rowsTr, 1))  #will contain predictions of training data

for r in range(rowsTr):  #make predictions and fill predTr
    temp = sum(X_train[r] * coeffs)
    predTr[r] = temp

predTr = predTr + intercept  #add intercept in order to complete predictions

diftr = predTr - y_train
rmsTr = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, diftr))))/rowsTr)
print("LM training score: ", rmsTr)

#DO THE SAME FOR TEST DATA
rowsTe = len(X_test)  #rows in matrices for prediction on training data
predTe = np.empty((rowsTe, 1))  #will contain predictions of training data

for r in range(rowsTe):  #make predictions and fill predTr
    temp = sum(X_test[r] * coeffs)
    predTe[r] = temp

predTe = predTe + intercept  #add intercept in order to complete predictions

difte = predTe - y_test
rmsTe = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difte))))/rowsTe)
print("LM test score: ", rmsTe)

#CREATE BASE MODEL
predBTr = np.zeros((rowsTr, 1))  #base model (predicts 0 for all inputs)
difBtr = predBTr - y_train
rmsBTr = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difBtr))))/rowsTr)
print("Base model on training score: ", rmsBTr)

predBTe = np.zeros((rowsTe, 1))  #base model (predicts 0 for all inputs)
difBte = predBTe - y_test
rmsBTe = math.sqrt(sum(np.asarray(list(map(lambda x : x**2, difBte))))/rowsTe)
print("Base model on test score: ", rmsBTe)







