#importing librarys
from kite_trade import *
import time

#authentication
enctoken = "hNm0UwKpq5IhZY4y5Up56Kbyhy/vAU0NuvUxW69OphGGpk7mf465/pNoteqo6oMD5cibV4261nJqDMWcR+YPg+lu00ZFcwtzA3LAOKknZV55E70dNziS6A=="
kite = KiteApp(enctoken=enctoken)

def price_fetcher(symbol):
    price = kite.ltp(["NSE:" + symbol])
    final_price = price["NSE:" + symbol]["last_price"]

    return final_price


x = 0

while True:
  print(x)
  price_fetcher("WIPRO")
  x+=1
  time.sleep(10)