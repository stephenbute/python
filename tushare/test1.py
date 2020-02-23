import tushare as ts

ts.set_token('')

pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20191201', end_date='20191231')

print(df)
