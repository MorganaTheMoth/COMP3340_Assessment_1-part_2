import pandas as pd


def _init_():
    print("starting E2")
    rowNames = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="A")
    rawSamples = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="B:AR")
    rawProteins = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="AS:CF")
    print(rawSamples)
    print(rawProteins)
    # just gunna use a hemming matrix

def genMST():
    return