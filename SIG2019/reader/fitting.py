#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 06/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import datetime
import pandas as pd
import numpy as np
import sklearn.metrics as sm
import configparser
import math, os, sys, time
import itertools
import mysql.connector
import fonctions_bot as fonctions
import matplotlib.pyplot as plt

from multiprocessing import Pool
from mpl_toolkits.mplot3d import Axes3D
from distance import distance1, distance2, distance3
from sklearn.cluster import KMeans

def main():

    colormap = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])

    db = fonctions.connectDB()
    cursor = db.cursor()

    themes = fonctions.get_themes()
    clusters = fonctions.get_clusters()
    data = []

    """
    for theme, cluster in themes:
        #data.append((theme, cluster, distance1(theme[0], cluster, 10)))
        #data.append((theme, cluster, distance2(theme, cluster, 10)))
        data.append((theme, cluster, distance3(theme, cluster, 10)))
   
    """
    
    for cluster in clusters:
        for theme in themes:
            data.append((theme, cluster, distance1(theme[0], cluster, 10)))
            #data.append((theme, cluster, distance2(theme, cluster, 10)))
            #data.append((theme, cluster, distance3(theme, cluster, 10)))

    w = open('data/distance1.txt', 'w')
    w.write(data)
    

    x = pd.DataFrame(data=data)
    x.columns=['Theme', 'Cluster', 'Distance']                        # 3D columns
    #x.columns=['Theme', 'Frequence']                                  # 2D columns
    print(x)
    model = KMeans(n_clusters=6)
    model.fit(x)

    fig = plt.figure()

    """  plt.scatter(x.Theme, x.Distance, c=colormap[model.labels_], s=2)
    plt.xlabel('Theme')
    plt.ylabel('Distance') """

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x.Theme, x.Cluster, x.Distance, c=colormap[model.labels_], s=2)
    ax.set_xlabel('Theme')
    ax.set_ylabel('Cluster')
    ax.set_zlabel('Distance')

    plt.show()


if __name__ == "__main__":
    print('\n Starting fitting')
    with Pool(processes=1) as pool:
        res = pool.apply_async(main)
        waiting, n = True, 0
        start = time.time()
        while waiting:
            try:
                waiting = not res.successful()
                data = res.get()
            except AssertionError:
                n = fonctions.loading_animation(n)
        end = time.time()
        sys.stdout.write('\r Fitting Complete. Completed in %s sec\n' % datetime.timedelta(seconds=end-start))