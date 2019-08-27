import numpy as np
import pandas as pd
import json


def load_and_prepare_data(file_path=None):
    file = 'exames.json'
    if(file_path):
        file = file_path
    else:
        pass
    datastore = pd.read_json(file)
    return datastore
