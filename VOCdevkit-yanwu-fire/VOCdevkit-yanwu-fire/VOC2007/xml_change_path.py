# coding=utf-8
import xml.dom.minidom
import os
# 打开xml文档

import os
import os.path
import xml.dom.minidom



path="Annotations/"
files=os.listdir(path)  #得到文件夹下所有文件名称
s=[]
for xmlFile in files: #遍历文件夹
    if not os.path.isdir(xmlFile): #判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
        root = dom.documentElement
        # 获取标签对name/pose之间的值
        name = root.getElementsByTagName('filename')
        name[0].firstChild.data = xmlFile[:-4]

        #pathh = root.getElementsByTagName('path')
        #tt = 'C:\\Users\miaoy\Desktop\miao\colazero\\' + xmlFile[:-4] + '.jpg'
        #pathh[0].firstChild.data = tt

        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('写入name/pose OK!')

    # dom = xml.dom.minidom.parse('/home/gumpcome/anaconda3/envs/tensorflow/models-master/research/object_detection/cym/VOC2007/maidong/maidong(1).xml')
    #
    #
    # root=dom.documentElement
    #
    #
    # item=root.getElementsByTagName('filename') #获取了所有名字为item的node
    # item=item[0]  #拿到第一个item,获取相关属性值
    # value = item.childNodes[0].data = 5
    # print(item.childNodes[0].data)
