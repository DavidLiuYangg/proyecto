import csv
import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
from recommender import Recommender
from sklearn.feature_extraction.text import TfidfVectorizer

    
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
b = np.array([1, -1, 2])


ab = np.empty(0)
for fila, num in zip(a, b): 
    print(fila, num, fila*num, (fila*num))
    mul = fila*num
    ab = np.append(ab, np.array([mul]))

ab = np.reshape(ab, (3, 3))
