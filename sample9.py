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
    url1.append("https://yobit.net/api/2/" +i.lower()+ "_btc/ticker")
    global ccy
    ccy.append(i.lower())
def get_yob(req):
    print (req)
    start_time = time.time()
    while True:
        try:
            res1 = scraper.get(req)
            try:
                data2 = json.dumps(res1.json())
                data5 = json.loads(data2)
                return data5
            except ValueError as err:
                print ('Req ID ' + req + ' Decode JSON invalid')               
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
def data_update(data1):
    while True:
        try:
            res = data1['ticker']
            tot = len(res) -1
            return res
        except TypeError as terr:
            print (terr)
            break
def get_val(val):
    while True:
        try:
            amt = val['last']
            return amt
        except TypeError as verr:
            print (verr)
            break
def get_time(val1):
    while True:
        try:
            timeval = val1['updated']
            return timeval
        except TypeError as terr1:
            print (terr1)
            break
def get_buy(val2):
    while True:
        try:
            buyval = val2['buy']
            return buyval
        except TypeError as terr2:
            print (terr2)
            break
def get_sell(val2):
    while True:
        try:
            sellval = val2['sell']
            return sellval
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
def check_inc(x1):
    print(url1[x1+1])
    yobjson = data_update(get_yob(url1[x1+1])
    price1 = get_val(yobjson)
    buyprice = get_buy(yobjson)
    sellprice = get_sell(yobjson) 
        if price1 == buyprice:
            global str1
            str1 = 'buy'
        else:
            if price1 == sellprice:
                global str1
                str1 = 'sell'
        if str1 == 'buy':
            if price1 > prvprice:
                i = i + 1
                if i>3:
                    global ccy
                    ccy2 = ccy[x1+1]+ '_btc'
                    sendstr = ccy2+":price Increasing :" + "Type:" + str1 + "Price: " + str(price1) + "PrevPrice:"+ str(prvprice)
                    chat_id = get_chat_id(last_update(get_updates_json(url)))
                    send_mess(chat_id, sendstr)   
                prvprice = price1
                time.sleep(10)
                check_inc(x1)    
#    t = threading.Thread(target=ccy_fun)
#    t.setDaemon(True)
#    t.start()
str1 = ''
for x in range(0, ccyt):
    t = threading.Thread(target=check_inc, args=(x,))
    t.setDaemon(True)
    t.start()
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


