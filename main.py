from re import X
#importing librarys
from kite_trade import *
from datetime import datetime
import time
data_file = open("data_file.txt","a+")

#authentication
enctoken = "H3eGq5A8LURd/rSQQ6uIOELJcs0OmpHNrv68ie/yZob2lcOimTOMFIJSQmVU5tdg+5Isxpa5pwWgoyaBI0IgqCLJLZrugy3dFSLQdp0ZovcjoGsmip8pkQ=="
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
  current_time = str(datetime.now())
  data_file.write(str(x))
  data_file.write("  ")
  data_file.write(curr_price)
  data_file.write("  ")
  data_file.write(current_time)
  data_file.write("\n")
  x+=1


  time.sleep(5)
  data_file.close()



