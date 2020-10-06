import pandas as pd
from pandas import DataFrame
import glob
import os

input_file = r'C:\Users\USER\chatbot-order\data\orderdata'
output_file = r'C:\Users\USER\chatbot-order\data\orderdata\order_total.csv'

# order로 시작하는 파일 모으기
allFile_list = glob.glob(os.path.join(input_file, 'order_*'))
print(allFile_list)

data = []

for file in allFile_list :
    df = pd.read_csv(file)
    data.append(df)

# axis=0은 수직으로 병합
dataCombine = pd.concat(data, axis=0, ignore_index=True)

dataCombine.to_csv(output_file, index=False)


filename = './orderdata/order_total.csv'
myframe = pd.read_csv(filename, sep = ',', encoding= 'utf-8')

filename1 = './orderdata/weather.csv'
myframe1 = pd.read_csv(filename1, sep = ',', encoding= 'utf-8')
myframe1.columns = ['일자(YYYYMMDD)', '평균기온', '강수량']

mydata = pd.merge(myframe, myframe1, on='일자(YYYYMMDD)')

print(mydata.head(10))

final_filename = 'order.csv'
mydata.to_csv(final_filename, mode= 'w', encoding='utf-8',index=False)


print('finished')