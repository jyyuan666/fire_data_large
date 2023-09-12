# coding=utf-8
import os
import os.path
import xml.dom.minidom
import cv2
img_path = 'JPEGImages/'
xml_path = 'Annotations/'
for img_file in os.listdir(img_path):
    img_name = os.path.splitext(img_file)[0]
    img = cv2.imread(img_path + img_file)
    sp = img.shape
    sz1 = sp[0]  # height(rows) of image
    sz2 = sp[1]  # width(colums) of image

    # 将获取的xml文件名送入到dom解析
    dom = xml.dom.minidom.parse(os.path.join(xml_path, img_name + '.xml'))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
    root = dom.documentElement
    # 获取标签对name/pose之间的值
    name = root.getElementsByTagName('width')
    pose = root.getElementsByTagName('height')
    print(name[0].firstChild.data )
    # 重命名class name
    name[0].firstChild.data = sz2
    pose[0].firstChild.data = sz1

    # 保存修改到xml文件中
    with open(os.path.join(xml_path, img_name + '.xml'), 'w') as fh:
        dom.writexml(fh)
        print('写入name/pose OK!')
