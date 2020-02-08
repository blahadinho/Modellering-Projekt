from sklearn.neural_network import MLPRegressor
import numpy as np

X = [[0., 0.], [1., 1.]]
Xnp = np.array([[0, 0], [1, 1]])  #same as X
y = [0, 1]
ynp = np.array([0, 1])  #same as y
clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
#print(clf)

clfFit = clf.fit(X, y)
#print(clfFit)

pred = clf.predict([[2., 2.], [-1., -2.]])

print(pred)














