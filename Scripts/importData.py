from sklearn.model_selection import train_test_split
import pandas


class ImportDF(object):
    def __init__(self):
        name = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/05.5 - Asteroids_Nasa/Data/nasa.csv'
        self.df = pandas.DataFrame(pandas.read_csv(name))
        self.df = self.dataProcessing()
        self.proportion = 0.2
        self.train = pandas.DataFrame()
        self.test = pandas.DataFrame()

    def dataProcessing(self):
        """
        Data processing method. This method removes the  dataset's:
                - Id
                - Name
                - Dates
        """
        msk = list(self.df.select_dtypes(include=['object', 'int64']).columns)
        self.df.drop(msk, axis=1, inplace=True)

        return self.df

    def dataSeparation(self):
        """
        Data separation method.
        """
        train, test = train_test_split(self.df, test_size=self.proportion)

        self.train = pandas.DataFrame(train)
        self.test = pandas.DataFrame(test)

    def main(self):
        """
        Main method.
        """
        self.dataProcessing()
        self.dataSeparation()
