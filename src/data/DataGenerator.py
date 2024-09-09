import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

class DataGenerator:
    
    def __init__(self, n_samples, n_features, n_informative, n_redundant, n_repeated, n_classes, 
                 n_clusters_per_class, flip_y, null_prob):
        ''' generate data using the make_classification module '''
        self.n_samples = n_samples
        self.n_features = n_features
        self.n_informative = n_informative
        self.n_redundant = n_redundant
        self.n_repeated = n_repeated
        self.n_classes = n_classes
        self.n_clusters_per_class = n_clusters_per_class
        self.flip_y = flip_y
        self.null_prob = null_prob

    def generate_random_data(self):
        X,y = make_classification(n_samples=self.n_samples, n_features=self.n_features,
                            n_informative=self.n_informative, n_redundant=self.n_redundant, n_repeated=self.n_repeated, 
                            n_classes=self.n_classes, n_clusters_per_class=self.n_clusters_per_class, weights=None, 
                            flip_y=self.flip_y, class_sep=1.0, hypercube=True, shift=0.0, 
                            scale=1.0, shuffle=True, random_state=None)
        return X,y
        
    def create_dataframe(self):
        X,y = self.generate_random_data()
        featurenames = list()
        for i in range(n_features):
            featurenames.append(f"x{i}")
        df = pd.concat([pd.DataFrame(X, columns=featurenames), 
                        pd.DataFrame(y, columns=['y'])], axis=1)

        ### generate random null values
        X = df.drop('y', axis=1) ### create dataframe with just X variables
        for col in X.columns:
            mask_values = np.random.choice([np.nan, True], size=df.shape[0], p=[self.null_prob, 1 - self.null_prob])
            df[col] = df[col]*mask_values
        return df