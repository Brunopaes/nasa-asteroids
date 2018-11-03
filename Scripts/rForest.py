from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from Scripts.importData import ImportDF
import pandas


class RandomForest(object):

    def __init__(self):
        self.rForest = RandomForestClassifier(n_estimators=100)
        self.data = ImportDF()
        self.data.main()

    # Used in predict
    def fit(self):
        """
        Fit model.
        :return self.rFores.fit(): fitted model
        """
        data = ImportDF()
        data.main()

        x = data.train.iloc[:, :-1]
        y = data.train.iloc[:, -1]

        return self.rForest.fit(x.values, y.values)

    # Used in val
    def predict(self, rForest):
        """
        Predict method.
        :param rForest: fitted model
        :return rForest.predict(): predicted model
        """
        return rForest.predict(self.data.test.iloc[:, :-1])

    # Used in main
    def val(self, model):
        """
        Assertiveness rate validation method.
        :param model: predicted model
        """
        y = self.data.test.iloc[:, -1]
        print('The Random Forest model assertiveness rate was: {0:.2f} %'.format(sum(model == y)/len(y) * 100))
        print('The dumb algorithm assertiveness rate was {0:.2f} %'.format(sum(y == True)/len(y) * 100))

        print(pandas.DataFrame(confusion_matrix(y, model), ['Hazardous', 'Not Hazardous'], ['Hazardous', 'Not Hazardous']))

    def main(self):
        """
        Main method
        """
        self.val(self.predict(self.fit()))
