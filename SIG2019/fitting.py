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
import configparser
import math, os, sys, time
import itertools
import mysql.connector
import fonctions_bot as fonctions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans

colormap = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])

db = fonctions.connectDB()
cursor = db.cursor()

#cursor.execute("SELECT * FROM frequences WHERE 1")
cursor.execute("SELECT mot, frequence FROM frequences WHERE 1")
data = cursor.fetchall()

x = pd.DataFrame(data=data)
#x.columns=['Mot', 'Theme', 'Frequence']
x.columns=['Mot', 'Frequence']
print(x)

model = KMeans(n_clusters=8)
model.fit(x)

fig = plt.figure()

plt.scatter(x.Mot, x.Frequence, c=colormap[model.labels_])


#ax = fig.add_subplot(111, projection='3d')

#ax.scatter(x.Mot, x.Theme, x.Frequence, c=colormap[model.labels_],)

#ax.set_xlabel('Mot')
#ax.set_ylabel('Theme')
#ax.set_zlabel('Frequence')

plt.show()