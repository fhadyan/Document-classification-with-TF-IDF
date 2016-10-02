import os
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
from UniqueWord import UniqueWord

class Stemming:
    def __init__(self):
        self.sourcePath = "output/training/stopword/"
        self.outPath = "output/training/stem/"
        if os.listdir(self.sourcePath)=="":
            u = UniqueWord()
            u.output()

    def stem(self):
        st = PorterStemmer()
        for filename in os.listdir(self.sourcePath):
            if not filename.endswith('.txt'): continue
            fullname = os.path.join(self.sourcePath, filename)

            file = open(fullname, 'r+')
            out = open(self.outPath + filename, 'wb+')

            strings = file.readlines()
            for string in strings:
                stemmed = st.stem(string[:-5])
                out.write(bytes(stemmed + " - " + string[-2] + "\n", "utf-8"))



stem = Stemming()
stem.stem()
