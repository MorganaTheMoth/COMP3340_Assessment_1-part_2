from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

def Begin():
    rawProteins = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="B:CF").to_numpy()
    
    return