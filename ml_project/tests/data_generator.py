from sklearn.datasets import make_classification
import pandas as pd

def generate_dataset(n_samples, columns, classes, target_col):
    n_features = len(columns)
    n_classes = len(classes)
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features, 
        n_classes=n_classes
    )
    
    df = pd.DataFrame(X, columns=columns)
    df[target_col] = y
    return df