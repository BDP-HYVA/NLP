import re
import numpy as np
import pandas as pd
import os
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
data = pd.read_csv('/content/reviews_rawdata_4.csv',names=("flag","site","review"))
data['review2'] = [re.sub('[^A-Za-z0-9가-힣]', '', s) for s in data['review']]
data1 = data['review2']
data1.to_csv('love.csv',index=False,encoding='utf-8-sig')
