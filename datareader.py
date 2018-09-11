import pandas as pd

'''
This file reads csv and other data and imports it to an array, numpy / pandas array, string or whatever parameter is specified
'''


def readCSV(path):
    return pd.read_csv(path, sep=",", header = 0)
