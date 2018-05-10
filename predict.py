import pickle
import sys
from .common import dtypes

test_columns  = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id']

model = pickle.load(sys.argv[1])

test = pd.read_csv("test.csv", usecols=test_columns, parse_dates=['click_time'], dtype=dtypes)
model.predict()

