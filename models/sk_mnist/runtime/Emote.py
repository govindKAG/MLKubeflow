from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

class Emote(object):
    def __init__(self):
        #self.class_names = ["class:{}".format(str(i)) for i in range(10)]
        self.clf = joblib.load('/data/mymodel.pkl') 

    def predict(self,X,feature_names):
        vectorizer = joblib.load('/data/vect.pkl') 
        feat = vectorizer.transform(X[0])
        return self.clf.predict(feat)

    
