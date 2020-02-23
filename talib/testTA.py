# coding=utf-8 
 
import talib 
import time

def init(context): 
    context.FAST = 30 # 短周期 
    context.SLOW = 60 # 长周期 
    context.symbol = 'DCE.i1801' # 订阅&交易标的 
    context.period = context.SLOW + 1 # 订阅数据滑窗长度 
    subscribe(context.symbol, '60s', count=context.period) # 订阅行情
    return

context.init()

fast_avg = talib.SMA(prices.values.reshape(context.period), context.FAST)
slow_avg = talib.SMA(prices.values.reshape(context.period), context.SLOW)

print(fast_avg)
print(slow_avg)
