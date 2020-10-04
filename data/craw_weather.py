import requests
import calendar
import datetime
from bs4 import BeautifulSoup
from pandas import DataFrame

# http://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2020&x=22&y=8&mm=1&obs=1

data = []
now = datetime.datetime.now()
nowyear = now.strftime('%Y')
nowmonth = now.strftime('%m')

for y in range(2019, 2021) :
    print('y : '+str(y) + 'year : ' + str(nowyear))
    if str(y) == str(nowyear) :
        monthrange = int(nowmonth) +1
    else : monthrange = 13

    for m in range(1, monthrange) :
        response = requests.get('http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy=' + str(y) + '&mm='+str(m) +'&obs=1')
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class' : 'table_develop'})

        count = 0
        point = ['']*7
        pointt = ['']*7
        fstr = ['']*7
        estr = ['']*7
        temp = ['']*7
        rain = ['']*7
        
        for tr in table.find_all('tr') :
            tds = list(tr.find_all('td'))

            if tds :
                for i in range(0,7) :
                    point[i] = tds[i].text

                if count%2 != 0:
                    for j in range(0,7) :
                        pointt[j] =  point[j].translate({ord('일'):''})

                if count%2 == 0 :
                    for k in range(0,7) :
                        fstr[k] = point[k].find('최고기온')
                        estr[k] = point[k].find('일강수량')
                        temp[k] = point[k][5:fstr[k]].translate({ord('℃'):''})
                        rain[k] = point[k][estr[k]+5:].translate({ord('-'):'0.0', ord('m'): ''})

                if pointt[0]=='\xa0' or temp[0] == '':
                    sun = ""
                else : 
                    sun = str(y) + ','+str(m) +','+pointt[0] + ','+temp[0]+ ','+rain[0]
                    data.append([sun])

                if pointt[1]=='\xa0' or temp[1] == '':
                        mon = ""
                else : 
                    mon = str(y) + ','+str(m) +','+ pointt[1] + ','+temp[1]+  ','+rain[1]
                    data.append([mon])

                if pointt[2]=='\xa0' or temp[2] == '':
                        tue = ""
                else : 
                    tue = str(y) + ','+str(m) +','+pointt[2] + ','+temp[2]+  ','+rain[2]
                    data.append([tue])

                if pointt[3]=='\xa0' or temp[3] == '':
                        wed = ""
                else : 
                    wed = str(y) + ','+str(m) +','+pointt[3] + ','+temp[3]+  ','+rain[3]
                    data.append([wed])

                if pointt[4]=='\xa0' or temp[4] == '':
                        thr = ""
                else : 
                    thr = str(y) + ','+str(m) +','+pointt[4] + ','+temp[4]+ ','+rain[4]
                    data.append([thr])

                if pointt[5]=='\xa0' or temp[5] == '':
                        fri = ""
                else : 
                    fri = str(y) + ','+str(m) +','+pointt[5] + ','+temp[5]+  ','+rain[5]
                    data.append([fri])

                if pointt[6]=='\xa0' or temp[6] == '':
                        sat = ""
                else : 
                    sat = str(y) + ','+str(m) +','+pointt[6] + ','+temp[6]+  ','+rain[6]
                    data.append([sat])

with open('./orderdata/weather.csv', 'w') as file :
    for i in data :
        file.write('{0}\n'.format(i[0]))                