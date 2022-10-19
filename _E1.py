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
    ax.set_ylabel("Resources visited")
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
    ax.set_ylabel("discussions participated in")
    # ax.set_yticklabels(["Male", "Female"])
    # plt.xlabel(["Male", "Female"])
    # plt.show()

    # == Graph 3 == #
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title('hands raised organised by gender')
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
    ax.set_ylabel("hands raised")


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

    #plt.show()

    # == for preformance == #
    # splitting the data
    ApreformX = data2.loc[data2['SectionID'] == 'A']
    ApreformY = ApreformX['Discussion'].to_numpy()
    ApreformX = ApreformX['SectionID'].to_numpy()

    BpreformX = data2.loc[data2['SectionID'] == 'B']
    BpreformY = BpreformX['Discussion'].to_numpy()
    BpreformX = BpreformX['SectionID'].to_numpy()

    CpreformX = data2.loc[data2['SectionID'] == 'C']
    CpreformY = CpreformX['Discussion'].to_numpy()
    CpreformX = CpreformX['SectionID'].to_numpy()

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(ApreformX, ApreformY, label="A Grade")
    ax.bar(BpreformX, BpreformY, label="B Grade")
    ax.bar(CpreformX, CpreformY, label="C Grade")
    ax.legend(loc='best')
    ax.set_ylabel("Discussion participation")

    # splitting the data
    ApreformX = data2.loc[data2['SectionID'] == 'A']
    ApreformY = ApreformX['AnnouncementsView'].to_numpy()
    ApreformX = ApreformX['SectionID'].to_numpy()

    BpreformX = data2.loc[data2['SectionID'] == 'B']
    BpreformY = BpreformX['AnnouncementsView'].to_numpy()
    BpreformX = BpreformX['SectionID'].to_numpy()

    CpreformX = data2.loc[data2['SectionID'] == 'C']
    CpreformY = CpreformX['AnnouncementsView'].to_numpy()
    CpreformX = CpreformX['SectionID'].to_numpy()

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(ApreformX, ApreformY, label="A Grade")
    ax.bar(BpreformX, BpreformY, label="B Grade")
    ax.bar(CpreformX, CpreformY, label="C Grade")
    ax.legend(loc='best')
    ax.set_ylabel("Announcement views")

    # splitting the data
    ApreformX = data2.loc[data2['SectionID'] == 'A']
    ApreformY = ApreformX['raisedhands'].to_numpy()
    ApreformX = ApreformX['SectionID'].to_numpy()

    BpreformX = data2.loc[data2['SectionID'] == 'B']
    BpreformY = BpreformX['raisedhands'].to_numpy()
    BpreformX = BpreformX['SectionID'].to_numpy()

    CpreformX = data2.loc[data2['SectionID'] == 'C']
    CpreformY = CpreformX['raisedhands'].to_numpy()
    CpreformX = CpreformX['SectionID'].to_numpy()

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(ApreformX, ApreformY, label="A Grade")
    ax.bar(BpreformX, BpreformY, label="B Grade")
    ax.bar(CpreformX, CpreformY, label="C Grade")
    ax.legend(loc='best')
    ax.set_ylabel("Hands raised")


    #seeing if girls preform better than girls
    GirlsPreformanceX = data2.loc[data2['Gender'] == 1]
    GirlsPreformanceY = GirlsPreformanceX['SectionID'].to_numpy()
    GirlsPreformanceX = GirlsPreformanceX['Gender'].to_numpy()
    BoysPreformanceX = data2.loc[data2['Gender'] == 0]
    BoysPreformanceY = BoysPreformanceX['SectionID'].to_numpy()
    BoysPreformanceX = BoysPreformanceX['Gender'].to_numpy()
    newBoysPreform = []
    for i in BoysPreformanceY:
        if i == 'A':
            i = 3
        if i == 'B':
            i = 2
        if i == 'C':
            i = 1
        newBoysPreform.append(i)
    #BoysPreformanceY = [i == 'A' for i in BoysPreformanceY]
    avgPreformance = sum(newBoysPreform) / len(newBoysPreform)
    print("The average preformance for Boys: ", avgPreformance)

    newGirlsPreform = []
    for i in GirlsPreformanceY:
        if i == 'A':
            i = 3
        if i == 'B':
            i = 2
        if i == 'C':
            i = 1
        newGirlsPreform.append(i)
    #BoysPreformanceY = [i == 'A' for i in BoysPreformanceY]
    avgGirlsPreformance = sum(newGirlsPreform) / len(newGirlsPreform)
    print("The average preformance for Girls: ", avgGirlsPreformance)

    # ax.bar(BpreformX, BpreformY, label="")
    plt.show()
    # data2.to_csv("Test.csv")
