#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : read_bbox_xml.py
# @time     : 2019/7/3 16:58


from xml.etree.ElementTree import ElementTree,Element
import os,shutil
import sys
import numpy as np


def read_bbox_data(srcfile):

    errorType=['panel','spot','stripe']

    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
        return
    ################ 1. 读取xml文件  ##########
    tree = ElementTree()
    tree.parse(srcfile)

    ################ 2. 读取属性 ###############
    bboxs=[ ]
    box_index = 0

    for element in tree.findall('object'):
        element_name = element.find('name').text
        for box in element.findall('bndbox'):  # Element.findall()

            x1 = float(box.find('xmin').text)
            y1 = float(box.find('ymin').text)
            x2 = float(box.find('xmax').text)
            y2 = float(box.find('ymax').text)

            bbox=[x1,y1,x2,y2,box_index]
            bboxs.append(bbox)
        box_index+=1

    return bboxs

def update_bbox_data(srcfile,destSrcfile,bboxes):

    errorType=['panel','spot','stripe']

    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
        return
    ################ 1. 读取xml文件  ##########
    tree = ElementTree()
    tree.parse(srcfile)
    root = tree.getroot()

    ################ 2. 修改属性 ###############
    bboxs=[ ]
    box_indexs = bboxes[:,4:5]
    box_indexs = box_indexs.reshape(-1, 1)
    box_index = 0


    for element in tree.findall('object'):
        element_name = element.find('name').text
        if(box_index not in box_indexs):
            root.remove(element)
            box_index += 1
            continue
        for bbox in bboxes:
            if(box_index == bbox[4]):
                for box in element.findall('bndbox'):  # Element.findall()
                    box.find('xmin').text=str(int(bbox[0]))
                    box.find('ymin').text=str(int(bbox[1]))
                    box.find('xmax').text=str(int(bbox[2]))
                    box.find('ymax').text=str(int(bbox[3]))
                break

        box_index+=1



    tree.write(destSrcfile,encoding="utf-8", xml_declaration=True)



def main(argv = None):

   # boxs = read_bbox_data("testdata\\20180811_114023.xml")
   # print(boxs)
    bboxes = np.array([[1,2,3,4,0],[5,6,7,8,2]])
    update_bbox_data("testdata\\20180811_114023.xml", "testdata\\20180811_114023_1.xml",bboxes)


if __name__ == '__main__':
    sys.exit(main())