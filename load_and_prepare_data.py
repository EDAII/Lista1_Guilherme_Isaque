import numpy as np
import pandas as pd
import json


def load_and_prepare_data(file_path=None):
    file = 'data_set/cnesnone.csv'
    if(file_path):
        file = file_path
    else:
        pass
    datastore = pd.read_csv(file)
    return datastore

# primeira opção
def selectionSort(datastore):
   for i in range(len(datastore)):
      # Encontra o elemento mínimo
       minPosition = i
    for j in range(i+1, len(datastore)):
        if datastore[minPosition] > datastore[j]:
            minPosition = j
    # Troca o menor elemento encontrado por minPosition
    temp = datastore[i]
    datastore[i] = datastore[minPosition]
    datastore[minPosition] = temp
    return datastore

# segunda opção
sortedlist = sorted(data, key=lambda row: row[0], reverse=True)
