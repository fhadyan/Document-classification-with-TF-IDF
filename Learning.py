import os
import xml.etree.ElementTree as ET
# import nltk
# from nltk import FreqDist
import re
# from nltk.corpus import stopwords
# from nltk.stem.lancaster import LancasterStemmer
# from nltk.stem.porter import PorterStemmer
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import Weighting

class Learning:
    def __init__(self):
        self.trainingSetPath = "output/testing/tfidf/training.xlsx"
        self.testSetPath = "output/testing/tfidf/testing.xlsx"
        self.trainingTopicPath = "dataset/topic/Training101.txt"
        self.testingTopicPath = "dataset/topic/Test101.txt"
        if os.listdir("output/testing/tfidf/")=="":
            d = Weighting()
            d.output()

    def output(self):
        df = pd.read_excel(self.trainingSetPath)
        trainingSet =  df.as_matrix()
        for temp in trainingSet:
            temp[0] = int(temp[0][:-4])
        trainingSet = trainingSet[np.argsort(trainingSet[:,0])]
        #trainingSet = trainingSet[:,1:]
        # for temp in trainingSet:
        #     print(temp)

        df = pd.read_excel(self.testSetPath)
        testingSet =  df.as_matrix()
        for temp in testingSet :
            temp[0] = int(temp[0][:-4])
        testingSet = testingSet [np.argsort(testingSet[:,0])]
        #testingSet = testingSet[:,1:]

        topicFile = open(self.trainingTopicPath,"r+")
        strings = topicFile.readlines()
        trainingTopic = []
        for string in strings:
            temp = string.split(' ')
            temp[2] = int(temp[2][:-1])
            trainingTopic.append(temp[1:])
        trainingTopic = np.array(trainingTopic)

        topicFile = open(self.testingTopicPath,"r+")
        strings = topicFile.readlines()
        testingTopic = []
        for string in strings:
            temp = string.split(' ')
            temp[2] = int(temp[2][:-1])
            testingTopic.append(temp[1:])
        testingTopic = np.array(testingTopic)
        #print(testingTopic)


        #naive bayes
        gnb = GaussianNB()
        model = gnb.fit(trainingSet[:,1:], np.squeeze(trainingTopic[:,1:]))
        prediction = model.predict(testingSet[:,1:])

        result = confusion_matrix(np.squeeze(testingTopic[:,1:]), prediction)

        acc = (result[0,0]+result[1,1])/result.sum()
        presicion = result[0,0]/(result[0,0]+result[1,0])
        recall = result[0,0]/(result[0,0]+result[0,1])
        f1 = 2*presicion*recall/(presicion+recall)

        print("Naive Bayes")
        print("[tp   fn]")
        print("[fp   tn]")
        print(result)
        print("accuracy : " + str(acc*100) + "%")
        print("presicion : " + str(presicion*100) + "%")
        print("recall : " + str(recall*100) + "%")
        print("f1 : " + str(f1*100) + "%")

        #SVM
        svm = SVC()
        model = svm.fit(trainingSet[:,1:], np.squeeze(trainingTopic[:,1:]))
        prediction = model.predict(testingSet[:,1:])

        result = confusion_matrix(np.squeeze(testingTopic[:,1:]), prediction)

        acc = (result[0,0]+result[1,1])/result.sum()
        presicion = result[0,0]/(result[0,0]+result[1,0])
        recall = result[0,0]/(result[0,0]+result[0,1])
        f1 = 2*presicion*recall/(presicion+recall)

        print("\nSVM")
        print("[tp   fn]")
        print("[fp   tn]")
        print(result)
        print("accuracy : " + str(acc*100) + "%")
        print("presicion : " + str(presicion*100) + "%")
        print("recall : " + str(recall*100) + "%")
        print("f1 : " + str(f1*100) + "%")

        #Desicion Treee
        dst = DecisionTreeClassifier(random_state=0)
        model = dst.fit(trainingSet[:,1:], np.squeeze(trainingTopic[:,1:]))
        prediction = model.predict(testingSet[:,1:])

        result = confusion_matrix(np.squeeze(testingTopic[:,1:]), prediction)

        acc = (result[0,0]+result[1,1])/result.sum()
        presicion = result[0,0]/(result[0,0]+result[1,0])
        recall = result[0,0]/(result[0,0]+result[0,1])
        f1 = 2*presicion*recall/(presicion+recall)

        print("\nDesicion Tree")
        print("[tp   fn]")
        print("[fp   tn]")
        print(result)
        print("accuracy : " + str(acc*100) + "%")
        print("presicion : " + str(presicion*100) + "%")
        print("recall : " + str(recall*100) + "%")
        print("f1 : " + str(f1*100) + "%")

        #kNN
        knn = KNeighborsClassifier(n_neighbors=8)
        model = knn.fit(trainingSet[:,1:], np.squeeze(trainingTopic[:,1:]))
        prediction = model.predict(testingSet[:,1:])

        result = confusion_matrix(np.squeeze(testingTopic[:,1:]), prediction)

        acc = (result[0,0]+result[1,1])/result.sum()
        presicion = result[0,0]/(result[0,0]+result[1,0])
        recall = result[0,0]/(result[0,0]+result[0,1])
        f1 = 2*presicion*recall/(presicion+recall)

        print("\nkNN")
        print("[tp   fn]")
        print("[fp   tn]")
        print(result)
        print("accuracy : " + str(acc*100) + "%")
        print("presicion : " + str(presicion*100) + "%")
        print("recall : " + str(recall*100) + "%")
        print("f1 : " + str(f1*100) + "%")

res = Learning()
res.output()