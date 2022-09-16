import numpy as np
import pandas as pd
from scipy.spatial.distance import hamming, jaccard, euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from relativeNeighborhoodGraph import returnRNG as cRNG


def _init_():
    print("starting E2")
    rawNames = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="A")
    Names = np.array(rawNames)

    #print(Names)
    rawSamples = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="B:AR").to_numpy()
    rawProteins = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="AS:CF").to_numpy()
    # print(rawSamples)
    HammSamplesEmpty = np.zeros([ rawSamples.shape[0], rawSamples.shape[0] ], dtype=float)
    HammProteinsEmpty = np.zeros([ rawProteins.shape[0], rawProteins.shape[0] ], dtype=float)

    hammingSamples = calcMatrix(data=rawSamples, matrix=HammSamplesEmpty, offset=0, type=0)
    hammingProteins = calcMatrix(data=rawProteins, matrix=HammProteinsEmpty, offset=0, type=0)

    genMST(matrix=hammingSamples, index=Names, exportLoc="./Answers/E2SamplesMST.xlsx")
    genMST(matrix=hammingProteins, index=Names, exportLoc="./Answers/E2ProteinsMST.xlsx")

    genRNG(data=hammingSamples, index=Names, exportLoc="./Answers/E2SamplesRNG.xlsx")
    genRNG(data=hammingProteins, index=Names, exportLoc="./Answers/E2ProteinsRNG.xlsx")

    #print(rawProteins)
    #print(rawSamples)

    # just gunna use a hemming matrix


def genMST(matrix, index, exportLoc):
    # This is magic to me xD
    Tcsr = minimum_spanning_tree(matrix)
    # print(matrix)
    Tcsr = Tcsr.toarray()
    final = pd.DataFrame(data=Tcsr, columns=index, index=index, dtype=float)
    # print(Tcsr)
    final.to_excel(exportLoc)
    return Tcsr


def calcMatrix(data, matrix, offset, type):
    i = 0
    # print(data.shape)
    while i < data.shape[0]:
        x = i
        # base = makeUseable(np.array2string(data[i]))
        # print("str test: " + base)
        while x < data.shape[0]:
            if type == 0:
                temp = euclidean(data[i], data[x])
                # print(str(i) + " " + str(x) + " " + str(temp) + str(data[i]) + " " + str(data[x]))
            else:
                temp = hamming(data[i], data[x]) * len(data[i])
            matrix[i + offset, x + offset] = temp
            matrix[x + offset, i + offset] = temp
            # print(hamming(data[i], data[x]) * len(data[i]))
            x += 1
        i += 1
    return matrix


def genRNG(data, index, exportLoc):
    # print(data)
    rng = cRNG.returnRNG(data)
    # print(rng)
    rng = rng.to_numpy()
    final = pd.DataFrame(data=rng, columns=index, index=index, dtype=float)
    # print(Tcsr)
    final.to_excel(exportLoc)
    return

