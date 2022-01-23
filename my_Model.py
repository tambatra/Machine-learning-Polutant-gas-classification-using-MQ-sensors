import pickle
import os


class ML_Model(object):
    """This class is used to expose predict method of our random forest model"""

    def __init__(self):
        self.target_names = ('CO2/SMOKE', 'ALCHOOL',
                             'FLAMMABLE_GAS', 'CO', 'EXHAUST_GAS')

        # Load model
        path = os.getcwd()+'/RF_Model.pkl'
        file = open(path, 'rb')
        self.model = pickle.load(file)
        print('RF Model is running...')

    def classMap(self, x):
        output = []
        for i in range(len(x)):
            output.append(self.target_names[x[i]])
        return output

    def predict(self, Q1, Q2, Q3, Q4):
        X = [[Q1, Q2, Q3, Q4]]
        pred = self.model.predict(X)
        gaz = self.classMap(pred)
        return gaz
