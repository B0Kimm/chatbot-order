import pandas as pd
from pandas import DataFrame


filename = 'Calldata_2007.csv'
myframe = pd.read_csv(filename, sep = ',', encoding= 'utf-8')


# print(myframe.columns)
myframe = myframe.drop(columns = '통화비율(시군구내)')
# print(myframe.columns)

# print(myframe)
print(myframe.shape)
# print(type(myframe))

# print(myframe['대분류'].unique())
print(myframe['대분류'].value_counts())

sublist=[]
mycolumns = ('일자(YYYYMMDD)', '연령', '성별','발신지(시도)','발신지(시군구)','업종')
for index, row in myframe.iterrows() :
    
    if row['대분류'] == '음식점' :
   
        imsi = [row['일자(YYYYMMDD)'], row['연령'], row['성별'],row['발신지(시도)'],row['발신지(시군구)'],row['중분류']]
        sublist.append(imsi)
    

result = pd.DataFrame(sublist, columns=mycolumns)

for index,row in result.iterrows() :
    result['계절'] = '여름'

print(type(result))
print(result.head())

filename1 = 'order_2007.csv'
result.to_csv(filename1, mode= 'w', encoding='utf-8',index=False)

print('finished')
