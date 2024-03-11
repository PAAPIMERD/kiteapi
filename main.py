from re import X
#importing librarys
from kite_trade import *
from datetime import datetime
import time
data_file = open("data_file.txt","a+")

#authentication
enctoken = "kj6OsLUHjPzRUrF5aF/l56q6n8xsnzwea+MIsVIArQyXoGfJRKpR4M81bFm9oc8u3bu2MWXuHpWnu9szPg7kNaOuO4Xw8DN4ahl967/b9eYPWCqvz5eioA=="
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
  time.sleep(20)
  order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="IDEA",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=5,
                         product=kite.PRODUCT_MIS,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")

  time.sleep(30)
  order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="IDEA",
                         transaction_type=kite.TRANSACTION_TYPE_SELL,
                         quantity=5,
                         product=kite.PRODUCT_MIS,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")

  time.sleep(5)
  data_file.close()

