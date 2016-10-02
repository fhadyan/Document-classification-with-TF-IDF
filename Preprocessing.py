import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer

class Preprocessing:
    def __init__(self):
        self.input = ""
        self.path ='dataset/training101/'
        self.outputPath = "output/training/all/"

    def output(self):
        stop = stopwords.words('english')
        st = PorterStemmer()
        for filename in os.listdir(self.path):
            if not filename.endswith('.xml'): continue
            fullname = os.path.join(self.path, filename)
            tree = ET.parse(fullname)
            input = (ET.tostring(tree.getroot(), encoding='iso-8859-1',method='text')).decode("utf-8")

            regex = re.compile('[^a-zA-Z\s]|^\w')
            input = regex.sub('', input)

            #unique word with frequency
            result =nltk.word_tokenize(input,language='english')
            fdist = FreqDist(result)
            words = fdist.keys()
            output = open(self.outputPath + filename[:-4] + ".txt", "wb+")
            for word in words:
                if word not in stop:
                    stemmed = st.stem(word)
                    output.write(bytes(stemmed+ "\n","utf-8"))


res = Preprocessing()
res.output()
res.path = "dataset/Test101/"
res.outputPath = "output/testing/all/"
res.output()