#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : Image_aug.py
# @time     : 2019/7/4 17:55



from data_aug import *
from bbox_util import *
from read_bbox_xml import *
import numpy as np
import cv2
import matplotlib.pyplot as plt

def saveImgXml(img,bboxes,img_file,xml_file,index):

    fileInfos = os.path.splitext(os.path.basename(xml_file))
    newfilenamexml = fileInfos[0] + "_" +str(index) + ".xml"
    newfilenamejpg = fileInfos[0] + "_" +str(index) + ".jpg"
    destSrcFilejpg = os.path.join(os.path.dirname(img_file), newfilenamejpg)
    cv2.imwrite(destSrcFilejpg, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    destSrcFilexml = os.path.join(os.path.dirname(xml_file), newfilenamexml)
    update_bbox_data(xml_file, destSrcFilexml, bboxes)


def augImg(img_file,xml_file):

    img = cv2.imread(img_file)[:, :,::-1]  # opencv loads images in bgr. the [:,:,::-1] does bgr -> rgb
    bboxes = read_bbox_data(xml_file)
    bboxes = np.array(bboxes)

    img_, bboxes_ = RandomScale(0.3, diff=True)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 1)
    info = "RandomScale:" + xml_file
    print(info)

    img_, bboxes_ = RandomRotate(10)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 2)
    info = "RandomRotate:" + xml_file
    print(info)

    img_, bboxes_ = RandomShear(0.15)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 3)
    info = "RandomShear:" + xml_file
    print(info)

    img_, bboxes_ = RandomTranslate(0.2, diff=True)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 4)
    info = "RandomTranslate1:" + xml_file
    print(info)

    img_, bboxes_ = RandomTranslate(0.2, diff=True)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 5)
    info = "RandomTranslate2:" + xml_file
    print(info)

    img_, bboxes_ = RandomHSV(50, 50, 30)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 6)
    info = "RandomHSV1:" + xml_file
    print(info)

    img_, bboxes_ = RandomHSV(50, 50, 30)(img.copy(), bboxes.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 7)
    info = "RandomHSV1:" + xml_file
    print(info)

    imgflip, bboxes2 = HorizontalFlip()(img.copy(), bboxes.copy())
    saveImgXml(imgflip, bboxes2, img_file, xml_file, 8)
    info = "HorizontalFlip:" + xml_file
    print(info)

    img_, bboxes_ = RandomScale(0.3, diff=True)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 9)
    info = "flipRandomScale:" + xml_file
    print(info)

    img_, bboxes_ = RandomRotate(10)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 10)
    info = "flipRandomRotate:" + xml_file
    print(info)

    img_, bboxes_ = RandomShear(0.15)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 11)
    info = "flipRandomShear:" + xml_file
    print(info)

    img_, bboxes_ = RandomTranslate(0.2, diff=True)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 12)
    info = "flipRandomTranslate1:" + xml_file
    print(info)

    img_, bboxes_ = RandomTranslate(0.2, diff=True)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 13)
    info = "flipRandomTranslate2:" + xml_file
    print(info)

    img_, bboxes_ = RandomHSV(50, 50, 30)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 14)
    info = "flipRandomHSV1:" + xml_file
    print(info)

    img_, bboxes_ = RandomHSV(50, 50, 30)(imgflip.copy(), bboxes2.copy())
    saveImgXml(img_, bboxes_, img_file, xml_file, 15)
    info = "flipRandomHSV1:" + xml_file
    print(info)


def main(argv = None):
    img_file = "testdata\\20180811_114023.jpg"
    xml_file = "testdata\\20180811_114023.xml"
    augImg(img_file, xml_file)



if __name__ == '__main__':
    sys.exit(main())