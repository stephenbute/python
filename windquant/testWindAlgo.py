#方法二：利用Wind API直接获取均线数据，支持不复权、前复权、后复权
from WindAlgo import * 
from datetime  import  *
from pandas import DataFrame
from WindPy import *
w.start(show_welcome=False)

def prepare_data(context):
    #利用WIND API获取复权后的均线数据
    context.ma5={}
    context.ma15={}
    for code in context.securities:
        #获取5日前复权均线
        error,wsd_df5=w.wsd(code, "MA", context.start_date, context.end_date, "MA_N=5;PriceAdj=F",usedf=True)
        assert error ==0 , "API数据提取错误，ErrorCode={}，具体含义请至帮助文档附件《常见API错误码》中查询。".format(error)  # 若API提取数据出错（error != 0），就返回后面的异常提示
        wsd_df5.index = [i.date() for i in wsd_df5.index]  #提取原始日期索引中的年月日作为新的日期索引
        context.ma5[code]=wsd_df5
        #获取15日前复权均线
        error,wsd_df15=w.wsd(code, "MA", context.start_date, context.end_date, "MA_N=15;PriceAdj=F",usedf=True)
        assert error ==0 , "API数据提取错误，ErrorCode={}，具体含义请至帮助文档附件《常见API错误码》中查询。".format(error)
        wsd_df15.index = [i.date() for i in wsd_df15.index]
        context.ma15[code]=wsd_df15

#定义初始化函数
def initialize(context):
    context.capital = 1000000
    context.securities = ["000333.SZ"]
    context.start_date = "20160201"
    context.end_date = "20170501"
    context.period = 'd'
    prepare_data(context)

#定义策略函数
def handle_data(bar_datetime, context, bar_data):
    position=bkt.query_position()  #获取历史数据
    bar_datetime = bar_datetime.date() #提取原始bar_datetime中的年月日作为新的bar_datetime
    if('000333.SZ' in position.get_field('code')):
        if(context.ma5['000333.SZ']['MA'][bar_datetime]<context.ma15['000333.SZ']['MA'][bar_datetime]):
            bkt.batch_order.sell_all()
    else:
        if('000333.SZ' not in position.get_field('code')):
            if(context.ma5['000333.SZ']['MA'][bar_datetime]>context.ma15['000333.SZ']['MA'][bar_datetime]):
                res = bkt.order_percent('000333.SZ',0.9, 'buy')

bkt = BackTest(init_func = initialize, handle_data_func=handle_data)
res = bkt.run(show_progress=True)
nav_df=bkt.summary('nav')