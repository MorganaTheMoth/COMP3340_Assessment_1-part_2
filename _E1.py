import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp


def boop():
    # changeing the data set for ease of use
    data = pd.read_csv("Datasets/xAPI-Edu-Data.csv")
    dummy = pd.get_dummies(data['gender'])
    # modifying for male and female
    data2 = pd.concat((data, dummy), axis=1)
    data2 = data2.drop(['gender'], axis=1)
    data2 = data2.drop(['M'], axis=1)
    data2 = data2.rename(columns={"F": "Gender"})
    # Female: 1  |  Male: 0
    dummy = pd.get_dummies(data2['Relation'])
    data2 = pd.concat((data2, dummy), axis=1)
    data2 = data2.drop(['Relation'], axis=1)
    data2 = data2.drop(['Father'], axis=1)
    data2 = data2.rename(columns={"Mum": "Relation"})
    # raised by the mother: 1 | raised by the father: 0

    # ==== Graphing ==== #
    plt.style.use('_mpl-gallery')
    # discussion
    girlsdiscX = data2.loc[data2['Gender'] == 1]
    girlsdsicY = girlsdiscX['Discussion'].to_numpy()
    girlsdiscX = girlsdiscX['Gender'].to_numpy()

    boysdiscX = data2.loc[data2['Gender'] == 0]
    boysdiscY = boysdiscX['Discussion'].to_numpy()
    boysdiscX = boysdiscX['Gender'].to_numpy()

    # visiting resources
    girlsvisX = data2.loc[data2['Gender'] == 1]
    girlsvisY = girlsvisX['VisITedResources'].to_numpy()
    girlsvisX = girlsvisX['Gender'].to_numpy()

    boysvisX = data2.loc[data2['Gender'] == 0]
    boysvisY = boysvisX['VisITedResources'].to_numpy()
    boysvisX = boysvisX['Gender'].to_numpy()

    # raising hands
    girlrshndX = data2.loc[data2['Gender'] == 1]
    girlrshndY = girlrshndX['VisITedResources'].to_numpy()
    girlrshndX = girlrshndX['Gender'].to_numpy()

    boyrshndX = data2.loc[data2['Gender'] == 0]
    boyrshndY = boyrshndX['VisITedResources'].to_numpy()
    boyrshndX = boyrshndX['Gender'].to_numpy()

    # == Graph 1 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title('visited resources organised by gender')
    ax.set_yticks(np.arange(0, 151, 10))
    ax.set_xticks(np.arange(2), ('Boys', 'Girls'))
    ax.bar(boysvisX, boysvisY,  color='blue', width=0.99, label='Boys')
    ax.bar(girlsvisX, girlsvisY, color='pink', width=0.99, label='Girls')
    # ax.bar(girlsdiscX, girlsdsicY, color='magenta', width=0.25, label='Female')
    # ax.bar_label(group1, padding=3)
    ax.legend(loc='best')
    # ax.set_yticklabels(["Male", "Female"])
    # plt.xlabel(["Male", "Female"])
    # plt.show()

    # == Graph 2 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title('Discussion participation organised by gender')
    ax.set_yticks(np.arange(0, 151, 10))
    ax.set_xticks(np.arange(2), ('Boys', 'Girls'))
    ax.bar(boysdiscX, boysdiscY,  color='blue', width=0.99, label='Boys')
    ax.bar(girlsdiscX, girlsdsicY, color='pink', width=0.99, label='Girls')
    # ax.bar(girlsdiscX, girlsdsicY, color='magenta', width=0.25, label='Female')
    # ax.bar_label(group1, padding=3)
    ax.legend(loc='best')
    # ax.set_yticklabels(["Male", "Female"])
    # plt.xlabel(["Male", "Female"])
    # plt.show()

    # == Graph 3 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title('Discussion participation organised by gender')
    ax.set_yticks(np.arange(0, 151, 10))
    ax.set_xticks(np.arange(2), ('Boys', 'Girls'))
    ax.bar(boyrshndX, boyrshndY,  color='blue', width=0.99, label='Boys')
    ax.bar(girlrshndX, girlrshndY, color='pink', width=0.99, label='Girls')
    # ax.bar(girlsdiscX, girlsdsicY, color='magenta', width=0.25, label='Female')
    # ax.bar_label(group1, padding=3)
    ax.legend(loc='best')
    # ax.set_yticklabels(["Male", "Female"])
    # plt.xlabel(["Male", "Female"])
    # plt.show()

    # == Scatter plots == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    #ax.set_yticks(np.arange(0, 151, 10))
    #ax.set_xticks(np.arange(0, 151, 10))
    G1, _ = sp.stats.pearsonr(boyrshndY, boysdiscY)
    print('Pearsons correlation between raising hands and and participating in discussions amoung boys: %.5f' % G1)
    G2, _ = sp.stats.pearsonr(girlrshndY, girlsdsicY)
    print('Pearsons correlation between raising hands and and participating in discussions amoung girls: %.5f' % G2)
    ax.scatter(boyrshndY, boysdiscY, alpha=0.2, color="blue")
    ax.scatter(girlrshndY, girlsdsicY, alpha=0.2, color="pink")
    # plt.show()

    # == Scatter plots 2 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    #ax.set_yticks(np.arange(0, 151, 10))
    #ax.set_xticks(np.arange(0, 151, 10))
    G3, _ = sp.stats.pearsonr(boyrshndY, boysvisY)
    print('Pearsons correlation between rasing hands and visiting resources amoung boys: %.5f' % G3)
    G4, _ = sp.stats.pearsonr(girlrshndY, girlsvisY)
    print('Pearsons correlation between rasing hands and visiting resources amoung girls: %.5f' % G4)
    ax.scatter(boyrshndY, boysvisY, alpha=0.2, color="blue")
    ax.scatter(girlrshndY, girlsvisY, alpha=0.2, color="pink")

    # == Scatter plot 3 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    #ax.set_yticks(np.arange(0, 151, 10))
    #ax.set_xticks(np.arange(0, 151, 10))
    G3, _ = sp.stats.pearsonr(boysdiscY, boysvisY)
    print('Pearsons correlation between discussion and visiting resources amoung boys: %.5f' % G3)
    G4, _ = sp.stats.pearsonr(girlsdsicY, girlsvisY)
    print('Pearsons correlation between discussion and visiting resources amoung girls: %.5f' % G4)
    ax.scatter(boysdiscY, boysvisY, alpha=0.2, color="blue")
    ax.scatter(girlsdsicY, girlsvisY, alpha=0.2, color="pink")

    plt.show()

    # data2.to_csv("Test.csv")
