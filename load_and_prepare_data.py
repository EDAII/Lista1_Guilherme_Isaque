import numpy as np
import pandas as pd
import json
from operator import itemgetter
#import matplotlib.pyplot as plt
# load the iris dataset
# separate the data from the target attributes
# normalize the data attributes

# Cabeçalho do dataset 'co_cnes','co_ibge','origem_dado','data_atualizacao','lat','long'
# Link do dataset http://dados.gov.br/dataset/cnes

# normalized_data = preprocessing.normalize(sortedlist)


def load_and_prepare_data(file_path=None):
    file = 'data_set/cnesnone.csv'
    if(file_path):
        file = file_path
    else:
        pass
    datastore = pd.read_csv(file)
    data = datastore.values.tolist()
    sortedlist = sorted(data, key=itemgetter(0))

    return sortedlist
