import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
def prediction(value):
    data = pd.read_csv(r"D:\Coding\heroku\train.csv")
    data = clean_dataset(data)
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)
    X = data[:,0].reshape(-1,1)
    y= data[:,1].reshape(-1,1)
    model = LinearRegression()
    model.fit(X,y)
    return model.predict(np.array(value).reshape(1,-1))

