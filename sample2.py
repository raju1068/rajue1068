import requests
import cfscrape
import json
import time
import datetime
from datetime import datetime
scraper = cfscrape.create_scraper() 
# print scraper.get("https://yobit.net/api/3/trades/ltc_btc").content

url = "https://api.telegram.org/bot468860549:AAHLj6uQeNHv-NVEhNqkqLNmpR6Q85G2Chw/"
url1 = "https://yobit.net/api/3/trades/ltc_btc"
def get_yob(req):
    res1 = scraper.get("https://yobit.net/api/3/trades/ltc_btc").json()
    data2 = json.dumps(res1)
    data5 = json.loads(data2)
    return data5
def data_update(data1,ind):
    res = data1['ltc_btc']
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
price1 = [0]
time1 = [0]
typeval1 = [' ']
timeval1 =['0']
for x in range(0, 999999):
    for y in range(0,10):
 #   time.sleep(10)
        yobjson = get_yob(url1)
        price1.append(get_val(data_update(yobjson,y)))
        print ('price' +str(y+1)+ ':'+str(price1[y+1]))
        timeval1.append(get_time(data_update(yobjson,y)))
        time1.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeval1[y+1])))
        typeval1.append(get_type(data_update(yobjson,y)))
        if typeval1[y+1] == typeval1[y]:
            time1n = int(datetime.strptime(time1[y+1], "%Y-%m-%d %H:%M:%S").strftime('%s'))*1000
            prevtime1n = int(datetime.strptime(time1[y], "%Y-%m-%d %H:%M:%S").strftime('%s'))*1000
            timediff = time1n - prevtime1n
            pricediff = price1[y+1] - price1[y]
#        print (time1n)
#        print (prevtime1n)
            print ('time diff: '+str(timediff))
            print ('price diff:' +str(pricediff))
            print ('Type :' + typeval1[y+1])
            if timediff > 0 and pricediff > 0 :
                sendstr = "Price Increasing :" + "Type:" + str(typeval1) + "Price: " + str(amt1) + "Prev Price: " + str(prevamt1)
                print (sendstr)
                if sendstr > ' ' :
                    print ('inside')
                    chat_id = get_chat_id(last_update(get_updates_json(url)))
                    str1 = 'ltc_btc' + ':' + str(amt1) +';'+str(time1)+"status"+sendstr
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


