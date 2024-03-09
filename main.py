#importing librarys
from kite_trade import *
import time
data_file = open("data_file.txt","a+")

#authentication
enctoken = "hNm0UwKpq5IhZY4y5Up56Kbyhy/vAU0NuvUxW69OphGGpk7mf465/pNoteqo6oMD5cibV4261nJqDMWcR+YPg+lu00ZFcwtzA3LAOKknZV55E70dNziS6A=="
kite = KiteApp(enctoken=enctoken)

def price_fetcher(symbol):
    price = kite.ltp(["NSE:" + symbol])
    final_price = price["NSE:" + symbol]["last_price"]

    return final_price


x = 0

while True:
  data_file = open("data_file.txt","a+")
  print(x)
  curr_price =  str(price_fetcher("WIPRO"))
  print(curr_price)
  data_file.write(curr_price)
  x+=1
  time.sleep(10)
  data_file.close()
