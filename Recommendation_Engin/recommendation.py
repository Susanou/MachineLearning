#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ml-25m/ratings.csv')
print(df.head())

movie_titles = pd.read_csv('ml-25m/movies.csv')
print(movie_titles.head())

df = pd.merge(df, movie_titles, on='movieId')
print(df.head())
print(df.describe())

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
print(ratings.head())