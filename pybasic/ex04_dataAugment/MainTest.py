#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : MainTest.py
# @time     : 2019/7/3 16:57

from data_aug import *
from bbox_util import *
from read_bbox_xml import *
import numpy as np
import cv2
import matplotlib.pyplot as plt


xmlpath = "testdata\\20180811_114023.xml"
img = cv2.imread("testdata\\20180811_114023.jpg")[:,:,::-1]   #opencv loads images in bgr. the [:,:,::-1] does bgr -> rgb
#bboxes = pkl.load(open("messi_ann.pkl", "rb"))
bboxes = read_bbox_data("testdata\\20180811_114023.xml")
print(bboxes)
bboxes = np.array(bboxes)
print(bboxes)
plotted_img = draw_rect(img, bboxes)
plt.imshow(plotted_img)
plt.show()

fileInfos = os.path.splitext(os.path.basename(xmlpath))
newfilename = fileInfos[0] + "_1"+".xml"
img1, bboxes_ = HorizontalFlip()(img.copy(), bboxes.copy())
plotted_img = draw_rect(img1, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_1.jpg",cv2.cvtColor(img1,cv2.COLOR_RGB2BGR))
destSrcfile =os.path.join(os.path.dirname(xmlpath),newfilename)
update_bbox_data(xmlpath,destSrcfile,bboxes_)



img2, bboxes_ = RandomScale(0.3, diff = True)(img.copy(), bboxes.copy())
print("*******scale**********")
print(bboxes_)
plotted_img = draw_rect(img2, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_2.jpg",cv2.cvtColor(img2,cv2.COLOR_RGB2BGR))


img3, bboxes_ = RandomRotate(10)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img3, bboxes_)
print(bboxes)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_3.jpg",cv2.cvtColor(img3,cv2.COLOR_RGB2BGR))


img4, bboxes_ = RandomShear(0.15)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img4, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_4.jpg",cv2.cvtColor(img4,cv2.COLOR_RGB2BGR))

'''
img5, bboxes_ = Resize(700)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img5, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_5.jpg",cv2.cvtColor(img5,cv2.COLOR_RGB2BGR))
'''

img6, bboxes_ = RandomHSV(50, 50, 30)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img6, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_6.jpg",cv2.cvtColor(img6,cv2.COLOR_RGB2BGR))

img0, bboxes_ = RandomTranslate(0.2, diff = True)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img0, bboxes_)
plt.imshow(plotted_img)
plt.show()
cv2.imwrite("20180811_114023_0.jpg",cv2.cvtColor(img0,cv2.COLOR_RGB2BGR))