import os
import os.path
rootdir = "H:/photos/29Jul2011"                                   # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    i = 11 
    for filename in filenames:
        fullname = os.path.join(parent,filename)
        i = i+1
        newname = os.path.join(parent,'公园'+ str(i) +'.jpg')                        #输出文件信息
        print ("the full name of the file is:" + fullname) #输出文件路径信息
        os.rename(fullname, newname)