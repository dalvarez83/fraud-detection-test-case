import pandas as pd
import numpy as np


class DataGeneratorRandomInt:
    def __init__(self, num_rows, num_features, min_value, max_value, null_prob, flip_y):
        self.num_rows = n_rows
        self.num_features = n_features
        self.min_value = min_value
        self.max_value = max_value
        self.null_prob = null_prob
        self.flip_y= flip_y

    def generate_random_data(self):
        X = np.random.randint(self.min_value, self.max_value, size=(self.num_rows+1, self.num_features+1))
        
        ### generate binary output variable    
        y = np.random.choice([0, 1], size=self.num_rows, p=[1-self.flip_y, self.flip_y])  # Binary output column
        return X,y

    def create_dataframe(self):
        X,y = self.generate_random_data()
        data = pd.DataFrame(data=X[1:,1:], index=X[1:,0], columns=X[0,1:])
        y = pd.DataFrame(pd.Series(data=y[:]), columns=['y'])
        
        # create column names
        featurenames = list()
        for i in range(n_features):
            featurenames.append(f"x{i}")
        data.columns = featurenames

        ### generate random null values
        for col in data.columns:
            mask_values = np.random.choice([np.nan, True], size=data.shape[0], p=[self.null_prob, 1 - self.null_prob])
            data[col] = data[col]*mask_values
        
        data = data.reset_index()
        
        df = pd.concat([pd.DataFrame(data, columns=featurenames),
                       pd.DataFrame(y, columns=['y'])], axis=1)

        ### create resulting dataframe
        df = pd.concat([pd.DataFrame(data, columns=featurenames),
               pd.DataFrame(y, columns=['y'])], axis=1)
        
        return df