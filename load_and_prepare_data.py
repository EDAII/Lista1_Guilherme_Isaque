import numpy as np
import pandas as pd

def load_and_prepare_data(file_path=None):
    data = 'exames.json'
    if(file_path):
        data = file_path
    else:
        pass
