
from datetime import datetime
import pandas as pd
import time
import warnings

pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

url = 'https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz'

startTime = time.time()
df = pd.read_cvs(url, compression='gzip', sep='\t', on_bad_lines='skip')

executionTime= (time.time() - startTime)
print('Execution time in minutes: ' + str(round(executionTime / 60, 2)))
print('Num of rows:', len(df))
print('Num of cols:', len(df.columns))
df.head()
