import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re

class UniqueWord:
    def __init__(self):
        self.input = ""
        self.path ='dataset/training101/'
        # for filename in os.listdir(path):
        #     if not filename.endswith('.xml'): continue
        #     fullname = os.path.join(path, filename)
        #     tree = ET.parse(fullname)
        #     self.input +=(ET.tostring(tree.getroot(),encoding='iso-8859-1',method='text')).decode("utf-8")
        # tree = ET.parse('dataset/training101/6146.xml')
        # self.input = (ET.tostring(tree.getroot(), encoding='iso-8859-1',method='text')).decode("utf-8")

    def output(self):
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
            output = open("output/training/unique/" + filename[:-4] + ".txt", "wb+")
            for word in words:
                output.write(bytes(word+ " - " + str(fdist.get(word)) + "\n","utf-8"))
                #print(word + " - " +str(fdist.get(word)))
            #.unique word with frequency


            #unique word only

            #.unique word only


res = UniqueWord()
res.output()
