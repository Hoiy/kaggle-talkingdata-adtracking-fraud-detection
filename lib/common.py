import pandas as pd

dtypes = {
    'ip'            : 'category',
    'app'           : 'category',
    'device'        : 'category',
    'os'            : 'category',
    'channel'       : 'category',
    'click_time'    : 'uint32',   
    'is_attributed' : 'uint8',
    'click_id'      : 'uint32'
}

train_columns = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed']
test_columns  = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id']

def load_train(**kwargs):
    return pd.read_csv("data/train.csv", parse_dates=['click_time'], usecols=train_columns, dtype=dtypes, **kwargs)

def load_test(**kwargs):
    return pd.read_csv("data/test.csv", parse_dates=['click_time'], usecols=test_columns, dtype=dtypes, **kwargs)

def load_test_supp(**kwargs):
    return pd.read_csv("data/test_supplement.csv", parse_dates=['click_time'], usecols=test_columns, dtype=dtypes, **kwargs)