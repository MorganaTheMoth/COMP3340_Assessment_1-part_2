import numpy as np
import pandas as pd
from scipy.spatial.distance import hamming, jaccard, euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from relativeNeighborhoodGraph import returnRNG as cRNG
from sigfig import round


def _init_():
    print("starting E2")
    rawNames = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="A")
    NProtienes = rawNames.values.flatten()

    rawNames = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set")
    NSamples = rawNames.columns.values.tolist()
    NSamples = NSamples[1:]
    print(len(NSamples))

    rawSamples = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="B:CF").to_numpy()

    rawProteins = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set", usecols="B:CF").to_numpy()

    rawSamples = np.transpose(rawSamples)
    # print(rawSamples)
    HammSamplesEmpty = np.zeros([rawSamples.shape[0], rawSamples.shape[0]], dtype=float)
    HammProteinsEmpty = np.zeros([rawProteins.shape[0], rawProteins.shape[0]], dtype=float)

    hammingSamples = calcMatrix(data=rawSamples, matrix=HammSamplesEmpty, offset=0, type=0)
    hammingProteins = calcMatrix(data=rawProteins, matrix=HammProteinsEmpty, offset=0, type=0)

    genMST(matrix=hammingSamples, index=NSamples, exportLoc="./Answers/E2SamplesMST.xlsx")
    genMST(matrix=hammingProteins, index=NProtienes, exportLoc="./Answers/E2ProteinsMST.xlsx")

    genRNG(data=hammingSamples, index=NSamples, exportLoc="./Answers/E2SamplesRNG.xlsx")
    genRNG(data=hammingProteins, index=NProtienes, exportLoc="./Answers/E2ProteinsRNG.xlsx")

    # print(rawProteins)
    # print(rawSamples)

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
                #temp = round(temp, sigfig=5)
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
    rng = remDoubleLines(rng)
    final = pd.DataFrame(data=rng, columns=index, index=index, dtype=float)
    # print(Tcsr)
    final.to_excel(exportLoc)
    return


def remDoubleLines(matrix):
    X = 0
    Y = 0
    while X < matrix.shape[1]:
        Y = 0
        while Y < matrix.shape[0]:
            if matrix[X, Y] != 0:
                if matrix[X, Y] == matrix[Y, X]:
                    # print(matrix[X, Y])
                    matrix[X, Y] = 0
            Y += 1
        X += 1
    # print(str(X) + " " + str(Y))
    return matrix
