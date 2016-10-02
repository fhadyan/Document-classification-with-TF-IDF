import os
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
from UniqueWord import UniqueWord
from nltk.corpus import stopwords

class StopWordRemoval:
    def __init__(self):
        self.sourcePath = "output/training/unique/"
        self.outPath = "output/training/stopword/"
        if os.listdir(self.sourcePath)=="":
            u = UniqueWord()
            u.output()

    def removeWord(self):
        #st = LancasterStemmer()
        stop = stopwords.words('english')
        for filename in os.listdir(self.sourcePath):
            if not filename.endswith('.txt'): continue
            fullname = os.path.join(self.sourcePath, filename)

            file = open(fullname, 'r+')
            out = open(self.outPath + filename, 'wb+')

            strings = file.readlines()
            for string in strings:
                filtered = string[:-5]
                if filtered not in stop:
                    out.write(bytes(filtered+ " - " + string[-2] + "\n", "utf-8"))



sw = StopWordRemoval()
sw .removeWord()
