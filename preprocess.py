import pandas as pd


def preprocess():
    df = pd.read_csv('/resources/data-1.csv')
    print(df.shape)