import matplotlib.pyplot as plt

dates = ['6-03','6-04','6-05','6-06','6-10','6-11','6-12','6-13','6-14','6-17','6-18','6-19','6-20','6-21','6-24','6-25','6-26','6-27','6-28']
closes = [11.9, 11.85, 11.97, 11.92, 12.34, 12.65, 12.57, 12.59, 12.49, 12.67, 12.8, 13.07, 13.8, 13.64, 13.69, 13.43, 13.37, 13.71, 13.78]
dates2 = ['6-10','6-11','6-12','6-13','6-14','6-17','6-18','6-19','6-20','6-21','6-24','6-25','6-26','6-27','6-28']

def get_MA(closes):
    means = []  #定义一个空的list
    for i in range(len(closes)-5+1):
        close_part = closes[i:i+5]  # 截取5日的收盘价
        close_mean = sum(close_part)/5  # 计算均值
        means.append(close_mean)
    return means


means = get_MA(closes)

print(means)
        
fig = plt.figure(figsize=(18,5))
plt.plot(dates,closes,linewidth=2,color='red',label='close')
plt.plot(dates2,means,linewidth=2,color='blue',label='MA5')
plt.legend(bbox_to_anchor=(0.1,1))
plt.show()

