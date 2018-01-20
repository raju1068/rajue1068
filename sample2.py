import requests 
import cfscrape
import json
import time
import datetime
import os
from requests import ConnectionError
from datetime import datetime
scraper = cfscrape.create_scraper() 
# print scraper.get("https://yobit.net/api/3/trades/ltc_btc").content

url = "https://api.telegram.org/bot468860549:AAHLj6uQeNHv-NVEhNqkqLNmpR6Q85G2Chw/"
<<<<<<< HEAD
url1 = ["https://yobit.net/api/3/trades/ltc_btc"]
=======
url1 = ""
>>>>>>> e143fe9d549cf93da81eaf2485794e189035824b
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
<<<<<<< HEAD
    url1.append("https://yobit.net/api/3/trades/" +i.lower()+ "_btc")
    global ccy
    ccy.append(i.lower())

def get_yob(req):
    print (req)
    start_time = time.time()
    while True:
        try:
            res1 = scraper.get(req).json()
            try:
                data2 = json.dumps(res1)
                data5 = json.loads(data2)
            except(json.decoder.JSONDecodeError,ValueError):
                print 'Question ID ' + questionId + ' Decode JSON has failed'
                logging.info("This qid didn't work " + questionId
            return data5
            break
        except ConnectionError:
            if time.time() > start_time + connection_timeout:
                raise Exception('Unable to get updates after {} seconds of ConnectionErrors'.format(connection_timeout))
            else:
                time.sleep(1) 
#    print (res1.status_code)
=======
    url1.append("https://yobit.net/api/3/trades/" +i+ "_btc")
    
def get_yob(req):
    res1 = scraper.get(url1).json()
>>>>>>> e143fe9d549cf93da81eaf2485794e189035824b
#    print(res1)
#    data2 = json.dumps(res1)
#    data5 = json.loads(data2)
#    return data5
def data_update(data1,ind,ccy1):
    res = data1[ccy1]
    tot = len(res) -1
    return res[ind]
def get_val(val):
    amt = val['price']
    return amt
def get_time(val1):
    timeval = val1['timestamp']
    return timeval
def get_type(val2):
    typeval = val2['type']
    return typeval
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
prevtype = ' '
prevtime1n = 0
sendstr = ' '
for x in range(0, ccyt):
    price1=[0]
    timeval1=[0]
    typeval1=['']
    time1=[0]
    for y in range(1,10):
    #   time.sleep(10)
        yobjson = get_yob(url1[x+1])
<<<<<<< HEAD
        global ccy
        ccy2 = ccy[x+1]+ '_btc'
        price1.append(get_val(data_update(yobjson,y,ccy2)))
=======
        price1.append(get_val(data_update(yobjson,y)))
>>>>>>> e143fe9d549cf93da81eaf2485794e189035824b
        print ('price' +str(y)+ ':'+str(price1[y]))
        timeval1.append(get_time(data_update(yobjson,y,ccy2)))
        time1.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeval1[y])))
        typeval1.append(get_type(data_update(yobjson,y,ccy2)))
        if y> 1:
            if typeval1[y] == typeval1[y-1] and typeval1[y] == 'bid':
                print('inside bid')
                bidflag = True
                prevtime1n = int(datetime.strptime(time1[y], "%Y-%m-%d %H:%M:%S").strftime('%s'))*1000
                time1n = int(datetime.strptime(time1[y-1], "%Y-%m-%d %H:%M:%S").strftime('%s'))*1000
                timediff = time1n - prevtime1n
                pricediff = price1[y-1] - price1[y]
                print (time1n)
                print (prevtime1n)
                print ('time diff: '+str(timediff))
                print ('price diff:' +str(pricediff))
                print ('Type :' + typeval1[y])
                if timediff > 0 and pricediff > 0 :
                    sendstr = ccy2+":price Increasing :" + "Type:" + str(typeval1[y-1]) + "Price: " + str(price1[y-1]) + "Prev Price: " + str(price1[y])
                    print (sendstr)
            else:
                bidflag = False
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


