import pandas as pd
from pandas import DataFrame

# https://www.bigdatahub.co.kr/product/view.do?pid=1002231

filename = 'CALL_NDELIVERY_09MONTH.csv'
myframe = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

# print(myframe.shape)
# print(myframe.head())

print(myframe['업종'].value_counts())
# print(myframe['시간대'].value_counts())


filename1 = 'order_2008.csv'
mydata = pd.read_csv(filename1, sep = ',', encoding= 'utf-8')

print(mydata['업종'].value_counts())


