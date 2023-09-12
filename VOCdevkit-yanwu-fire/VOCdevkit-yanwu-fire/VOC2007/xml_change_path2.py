# coding=utf-8
import xml.dom.minidom
import os

import os
import os.path
import xml.dom.minidom



path="22/"
files=os.listdir(path)
s=[]
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        print(xmlFile)

        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement
        name = root.getElementsByTagName('path')
        name[0].firstChild.data = xmlFile[:-4]

        #pathh = root.getElementsByTagName('path')
        #tt = 'C:\\Users\miaoy\Desktop\miao\colazero\\' + xmlFile[:-4] + '.jpg'
        #pathh[0].firstChild.data = tt

        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('写入name/pose OK!')

