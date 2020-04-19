import tushare as ts

ts.set_token('013b523b111f490aa74dadb1d3365b68e61c173b05f05d9bad0cb833')

pro = ts.pro_api()

# df = pro.daily(ts_code='000001.SZ', start_date='20191201', end_date='20191231')
df = pro.btc8(start_date='2019-08-17 16:00:00', end_date='2019-08-17 18:00:00', \
                fields='title, url, datetime')
print(df)
