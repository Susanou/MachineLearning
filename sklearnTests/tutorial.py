#!/usr/bin/env python

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 06/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import pandas as pd
import numpy as np
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

colormap=np.array(['Red', 'Green', 'Blue'])

iris = datasets.load_iris()

#print(iris)
#print(iris.data)
#print(iris.feature_names)
print(iris.target)
#print(iris.target_names)

x=pd.DataFrame(iris.data)
x.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y=pd.DataFrame(iris.target)
y.columns=['Targets']

print(y.columns)

model = KMeans(n_clusters=3)
model.fit(x)


#plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=40)
plt.show()
