import requests
import cfscrape
import json
import time
import datetime
import os
import threading
from requests import ConnectionError
from datetime import datetime
scraper = cfscrape.create_scraper() 
# print scraper.get("https://yobit.net/api/3/trades/ltc_btc").content

url = "https://api.telegram.org/bot468860549:AAHLj6uQeNHv-NVEhNqkqLNmpR6Q85G2Chw/"
url1 = ["https://yobit.net/api/3/trades/ltc_btc"]
url2 = "https://min-api.cryptocompare.com/data/all/exchanges"
ccyres = scraper.get(url2).json()
ccydata2 = json.dumps(ccyres)
ccydata5 = json.loads(ccydata2)
connection_timeout = 30
yobitccy = ccydata5['Yobit']
ccyt = len(yobitccy) -1
ccy = [' ']
for i in ccydata5['Yobit']:
    print (i)
    url1.append("https://yobit.net/api/3/trades/" +i.lower()+ "_btc")
    global ccy
    ccy.append(i.lower())
def get_yob(req):
    print (req)
    start_time = time.time()
    while True:
        try:
            res1 = scraper.get(req)
            time.sleep(1)
            try:
                data2 = json.dumps(res1.json())
                data5 = json.loads(data2)
                return data5
            except ValueError as err:
                print ('Req ID ' + req + ' Decode JSON invalid'+ str(err))               
                break
            except AttributeError as err1:
                print ('Req ID ' + req + 'Decode JSON invalid')            
                break
        except ConnectionError:
            if time.time() > start_time + connection_timeout:
                raise Exception('Unable to get updates after {} seconds of ConnectionErrors'.format(connection_timeout))
            else:
                time.sleep(1) 
#    print (res1.status_code)
#    print(res1)
#    data2 = json.dumps(res1)
#    data5 = json.loads(data2)
#    return data5
def data_update(data1,ind,ccy1):
    while True:
        try:
            res = data1[ccy1]
            tot = len(res) -1
            return res[ind]
        except TypeError as terr:
            print (terr)
            break
def get_val(val):
    while True:
        try:
            amt = val['price']
            return amt
        except TypeError as verr:
            print (verr)
            break
def get_time(val1):
    while True:
        try:
            timeval = val1['timestamp']
            return timeval
        except TypeError as terr1:
            print (terr1)
            break
def get_type(val2):
    while True:
        try:
            typeval = val2['type']
            return typeval
        except TypeError as terr2:
            print (terr2)
            break
def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    print (response)
    return response.json()
def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id
def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
#        time.sleep(1)
print (time.time()-500)
def ccy_data(yobjson,ccy2):
    sendstr = ' '
    bidflag = True
    print (ccy2)
    for y in range(0,10):
        price1.append(get_val(data_update(yobjson,y,ccy2)))
#        print ('price' +str(y)+ ':'+str(price1[y]))
        timeval1.append(get_time(data_update(yobjson,y,ccy2)))
        time1.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeval1[y])))
        typeval1.append(get_type(data_update(yobjson,y,ccy2)))
#        print (timeval1[y-1])
#        print (time.time()-500)
        if y> 1 and timeval1[y-1]>(time.time()-500):
            if typeval1[y] == typeval1[y-1] and typeval1[y] == 'bid'and bidflag == True:
                bidflag = True
                print('inside bid')
                bidflag = True
                prevtime1n = int(datetime.strptime(time1[y], "%Y-%m-%d %H:%M:%S").strftime('%s'))
                time1n = int(datetime.strptime(time1[y-1], "%Y-%m-%d %H:%M:%S").strftime('%s'))
                timediff = time1n - prevtime1n
                pricediff = price1[y-1] - price1[y]
                print (time1n)
                print (prevtime1n)
                print ('time diff: '+str(timediff))
                print ('price diff:' +str(pricediff))
                print ('Type :' + typeval1[y])
                if timediff > 0 and timediff < 30000 and pricediff > 0 :
                    global sendstr
                    sendstr = ccy2+":price Increasing :" + "Type:" + str(typeval1[y-1]) + "Price: " + str(price1[y-1]) + "Prev Price: " + str(price1[y])
                    print (sendstr)
            else:
                bidflag = False
    global sendstr
    if sendstr > ' ' and bidflag == True:
        print ('inside')
        chat_id = get_chat_id(last_update(get_updates_json(url)))
        str1 = sendstr
        send_mess(chat_id, str1)       
        print (time1)
    del price1[:]
    del timeval1[:]
    del time1[:]
    del typeval1[:]
prevtype = ' '
prevtime1n = 0
sendstr = ' '
price1 = [0]
timeval1=[0]
typeval1=['']
time1=[0]
def fun_start(ccyt1):
    for x in range(0, ccyt1):
#        time.sleep(10)
        yobjson1 = get_yob(url1[x+1])
        global ccy
        ccy21 = ccy[x+1]+'_btc'
        time.sleep(1)
        t = threading.Thread(target=ccy_data, args=(yobjson1,ccy21))
        t.setDaemon(True)
        t.start()
for i in range(0,99999):
    global ccyt
    fun_start(ccyt)

    
def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id += 1
            sleep(1)  
            if __name__ == '__main__':  
                 main()
                 def get_updates_json(request):  
                     params = {'timeout': 100, 'offset': None}
                     response = requests.get(request + 'getUpdates', data=params)
                     return response.json()


