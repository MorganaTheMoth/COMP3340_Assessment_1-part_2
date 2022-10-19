from sklearn.feature_selection import SelectKBest
import sklearn.preprocessing as pp
from sklearn.feature_selection import chi2
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import pandas as pd


def Begin():
    # === Feture selection === #
    # Gathering data
    rawData = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Training Set", usecols="B:CF").to_numpy()
    protienes = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Training Set", usecols="A")
    rawNames = pd.read_excel(io='Datasets/AlzheimersDisease.xls', sheet_name="Training Set")
    NSamples = rawNames.columns.str.split(".").str[0]
    NSamples = NSamples[1:]
    # print(NSamples)
    # normalising all the data usking sklearn's preprocessing
    # normData = pp.normalize(rawData)
    Scalar = pp.MinMaxScaler(feature_range=(0, 1))
    #print(rawData.shape)
    normData = np.transpose(rawData)
    # print(normData.shape)
    normData = Scalar.fit_transform(normData)
    label_encode = pp.LabelEncoder()

    X = normData[:, 0: 121]
    Y = normData[:, -1]
    # print(X)
    Y = label_encode.fit_transform(Y)
    # Extracting the best featurs
    bestFeatures = SelectKBest(score_func=chi2, k=120)
    fit = bestFeatures.fit_transform(X, Y)            # These are the final selected features.
    # print(fit.shape)
    # preping it for use
    dfScores = pd.DataFrame(fit)
    dflabel = pd.DataFrame(NSamples)
    finalFeaturs = pd.concat([dflabel, dfScores], axis=1)
    # finalFeaturs.columns = ['Illness', 'Score']
    finalFeaturs.to_csv('Test.csv')
    # print(finalFeaturs)
    # finalFeatures = fit.scores_

    # === Classifying the data === #
    model = KNeighborsClassifier(n_neighbors=3)
    # -- training the model -- #
    model.fit(fit, NSamples)    # it has learned lots

    #testing it.
    # X_train, X_test, Y_train, Y_test = train_test_split()

    # == Testing it with the other Datasets == #
    # importing data to test it with.   i am removeing the CD class as i have not trained the classifier to deal with them.
    rawTestData = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Test Set AD", usecols="B:CD").to_numpy()
    testData = rawTestData.transpose()
    X_Test = testData[:, 0: 120]
    #X_Test = Scalar.fit_transform(X_Test)
    Y_Test = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Test Set AD", usecols="B:CE")
    Y_Test = Y_Test.columns.str.split(".").str[0]
    # print(Y_Test)
    Y_Test = Y_Test[1:]
    #testing the model
    # Y_pred60 = model.predict(X_Test[:, 0: 60])
    Y_pred120 = model.predict(X_Test[:, 0:120])
    # print (X_Test[:, 0: 60])
    #print (Y_Test.shape)
    # graph = model.kneighbors_graph()
    print("== Results for the test set ==")
    #print("Accuracy 0-60: ", metrics.accuracy_score(Y_Test, Y_pred60))
    print("Accuracy: ", metrics.accuracy_score(Y_Test, Y_pred120))
    #print("Mathews Correlation 0-60: ", metrics.matthews_corrcoef(Y_Test, Y_pred60))
    print("Mathews Correlation: ", metrics.matthews_corrcoef(Y_Test, Y_pred120))
    # print("F-1 Score 0-60: ", metrics.f1_score(Y_Test, Y_pred60, average='weighted'))
    print("F-1 Score: ", metrics.f1_score(Y_Test, Y_pred120, average='micro'))
    # for spesificity & sensativity.
    TN, FP, FN, TP = metrics.confusion_matrix(Y_Test.to_numpy(), Y_pred120, labels=None)
    spc =TN/(TN+FP)
    sen =TP/(TP + FN)
    print("Specificity: ", spc)
    print("Sensitivity: ", sen)
    # print(rawProteins)

    # ==== going for MCI samples === #
    rawTestData = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Test Set MCI", usecols="B:W", skiprows=[0]).to_numpy()
    testData = rawTestData.transpose()

    Y_Test = pd.read_excel(io="Datasets/AlzheimersDisease.xls", sheet_name="Test Set AD", usecols="B:CE")
    Y_Test = Y_Test.columns.str.split(".").str[0]
    Y_Test = Y_Test[:22]
    # print(Y_Test)

    TestData = testData[:, 0: 120]
    # TestData = np.delete(TestData, 0, 1)

    Y_pred120 = model.predict(TestData)
    # TestData = pd.DataFrame(TestData)
    # TestData.to_csv("Test.csv")
    # print(rawTestData)
    print("\n== Results for the test set ==")
    #print("Accuracy 0-60: ", metrics.accuracy_score(Y_Test, Y_pred60))
    print("Accuracy: ", metrics.accuracy_score(Y_Test.to_numpy(), Y_pred120))
    #print("Mathews Correlation 0-60: ", metrics.matthews_corrcoef(Y_Test, Y_pred60))
    print("Mathews Correlation: ", metrics.matthews_corrcoef(Y_Test.to_numpy(), Y_pred120))
    # print("F-1 Score 0-60: ", metrics.f1_score(Y_Test, Y_pred60, average='weighted'))
    print("F-1 Score: ", metrics.f1_score(Y_Test.to_numpy(), Y_pred120, average='micro'))
    # for spesificity & sensativity.
    temp = metrics.confusion_matrix(Y_Test.to_numpy(), Y_pred120, labels=None)
    print(temp)
    TN, FP, FN, TP = temp
    spc =TN/(TN+FP)
    sen =TP/(TP + FN)
    print("Specificity: ", spc)
    print("Sensitivity: ", sen)
    # print(rawProteins)
    # print(Y_Test)
    return