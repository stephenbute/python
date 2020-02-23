# -*- coding: UTF-8 -*-

import akshare as ak
provinceData = ak.epidemic_163(indicator="省份")


#for i in range(len(epidemic_163_df)):
print(provinceData.head())


df = ak.get_js_dc_current()
df[df.coinType == "比特币(美元)"]
print(df)
