#!/usr/bin/env python3

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

themes = fonctions.get_themes()
data = []

""" for theme in themes:

    cursor.execute("SELECT frequences.mot as mot, frequences.theme as theme, frequences.frequence as frequence FROM frequences, variance WHERE theme=(SELECT id FROM themes WHERE nom='%s') AND frequences.mot=variance.Mot AND variance.Variance > 4 ORDER BY frequence DESC"% theme)             # 3D data
    #cursor.execute("SELECT theme, frequence FROM frequences WHERE 1") # 2D data
    data = data + cursor.fetchall()
    print(data) """

cursor.execute("SELECT mot, theme, frequence FROM fittingData")
data = cursor.fetchall()
print(data)
x = pd.DataFrame(data=data)
x.columns=['Mot', 'Theme', 'Frequence']                        # 3D columns
#x.columns=['Theme', 'Frequence']                                  # 2D columns
print(x)

model = KMeans(n_clusters=3)
model.fit(x)

fig = plt.figure()

#plt.scatter(x.Theme, x.Frequence, c=colormap[model.labels_], s=2)


ax = fig.add_subplot(111, projection='3d')
ax.scatter(x.Theme, x.Mot, x.Frequence, c=colormap[model.labels_], s=2)
ax.set_xlabel('Theme')
ax.set_ylabel('Mot')
ax.set_zlabel('Frequence')

plt.show()