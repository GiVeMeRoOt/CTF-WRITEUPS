#author-Chitrarth Tomar
from socket import *
def tell(coin,price):
    ls = coin.keys()
    lsort=sorted(ls,reverse=True)
    for a in lsort:
        if(price<0.001):
            break
        val = float(a)
        while(price>=val-0.001):
            price -= val
            coin[a]+=1
    print("exiting")

count=0
sock=socket(AF_INET, SOCK_STREAM)
sock.connect(('misc.chal.csaw.io',8000))
price=0.0
coin={}
while(1):
    data,address=sock.recvfrom(8000)
    print(data)
    if '.' in data:
        coin = {10000:0,5000:0,1000:0,500:0,100:0,50:0,20:0,10:0,5:0,1:0,0.5:0,0.25:0,0.1:0,0.05:0,0.01:0}
        start = data.find('$')+1
        end = data.find('.', start)+3
        price=data[start:end]
        #price= data[10:14] if 'correct!' in data else data[1:5]
        print("price",price)
        tell(coin,float(price))
        print(coin.items())
        strn = str(coin[10000])+"\n"
        sock.send(strn)
        print("counter:",count)
        count+=1
    else:
        if 'bills' in data:
            key = data[1:-8]
            key = key.replace(",","")
            print("key",key)
            strn = str(coin[int(key)])+"\n"
            sock.send(strn)
        elif data[-3]==')':
            key = data[-6:-4] if data[-6].isdigit() else data[-5:-4]
            a=int(key)/100.0
            strn = str(coin[a])+"\n"
            sock.send(strn)
