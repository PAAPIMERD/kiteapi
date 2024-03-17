from re import X
#importing librarys
from kite_trade import *
from datetime import datetime
import datetime
import pytz
import time

nature = []

#authentication
enctoken = "T7POWdwB0lyH70I+IllQtwK8T5FFqSsLzRKW6YdQEdTHKzql3nzAdoWVOg1OJRoRd/0ueECDBNEARtn0MS9v+EQmJ6bp0iqv9O3STap/fT9wV//EDHhEnw=="
kite = KiteApp(enctoken=enctoken)

def price_fetcher(symbol):
    price = kite.ltp(["NSE:" + symbol])
    final_price = price["NSE:" + symbol]["last_price"]

    return final_price

def sell_symbol(symbol,qty):
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol= "WIPRO",
                         transaction_type=kite.TRANSACTION_TYPE_SELL,
                         quantity=1,
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
    
def buy_symbol(symbol,qty):
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="WIPRO",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=1,
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
    


def current_time_in_india():
    # Get the current time in UTC
    utc_now = datetime.datetime.utcnow()

    # Convert UTC time to Indian Standard Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist)

    return list(str(ist_now.strftime("%H:%M")))




    




def initialiser():
    open_price = price_fetcher("WIPRO")
    time.sleep(140)
    close_price = price_fetcher("WIPRO")
    
    if open_price >= close_price:
        curr_nature = "red"
    else:
        curr_nature = "green"
    
    nature.append(curr_nature)

    trading_strategy()

  



def trading_strategy():
    while True:
        if nature[-1] == "red":
            open_price = price_fetcher("WIPRO")
            sell_symbol("WIPRO", 1)
            time.sleep(140)
            buy_symbol("WIPRO", 1)
            close_price = price_fetcher("WIPRO")

            if open_price >= close_price:
                curr_nature = "red"
            else:
                curr_nature = "green"
            nature.append(curr_nature)

        if nature[-1] == "green":
            open_price = price_fetcher("WIPRO")
            buy_symbol("WIPRO", 1)
            time.sleep(140)
            sell_symbol("WIPRO", 1)
            close_price = price_fetcher("WIPRO")

            if open_price >= close_price:
                curr_nature = "red"
            else:
                curr_nature = "green"
            nature.append(curr_nature)


while True:
  curr_time = current_time_in_india()
  if curr_time == ["0","9",":","1","5"]:
    initialiser()




