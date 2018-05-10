import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import TimeSeriesSplit
from lib import dtypes, train_columns
#import dask.dataframe as dd

def process_date(col):
    def process_df(df):
        df['%s_day'%col] = df[col].apply(lambda x: x.day)
        df['%s_hour'%col] = df[col].apply(lambda x: x.hour)
        df['%s_minute'%col] = df[col].apply(lambda x: x.minute)
        df['%s_second'%col] = df[col].apply(lambda x: x.second)
        return df
    return process_df

print("Processing Training")


train = pd.read_csv(
    "data/train.csv", 
    parse_dates=['click_time'], 
    usecols=train_columns, 
    dtype=dtypes
).map_partitions(process_date('click_time')).to_csv("data/preprocessed_train.csv")