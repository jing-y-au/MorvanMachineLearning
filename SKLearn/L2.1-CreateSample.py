#coding=utf-8
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=20)
plt.scatter(X, y)
plt.show()