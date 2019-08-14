#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : delPanelLabel.py
# @time     : 2019/6/29 16:23




from xml.etree.ElementTree import ElementTree,Element
import os,shutil
import sys



def mycopyfile(srcfile,dstFolder,dstFileName):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        #fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(dstFolder):
            os.makedirs(dstFolder)                #创建路径
        dstfile = os.path.join(dstFolder,dstFileName)
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print( "copy %s -> %s"%( srcfile,dstfile))



def deleteNode_xml(srcfile,nodeName):

    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
        return
    ################ 1. 读取xml文件  ##########
    tree = ElementTree()
    tree.parse(srcfile)

    ################ 2. 属性修改 ###############
    #nodes = find_nodes(tree, "object")  # 找到父节点
    root = tree.getroot()
    isModify = False
    for element in tree.findall('object'):  # Element.findall()
        name = element.find('name')
        if(name.text == nodeName):
            root.remove(element)
            isModify = True
    #updateTree.write(srcfile)  # 写回原文件
    if(isModify):
        tree.write(srcfile,encoding="utf-8", xml_declaration=True)
        info = srcfile + "--hot point to spot"
        print(info)
    #write_xml(tree, "xiugai.xml")
    return isModify



def main(argv = None):

    path = "J:\\标签数据\\0702_spot\\trainData"

    #path = "J:\\无人机光伏电站数据\\售前试飞数据\\平地电站"

    #"F:\\ShareData\\无人机光伏电站数据\\售前试飞数据\\平地电站"

    #dstPath = "F:\\ShareData\\标签数据\\625_hotpoint\\traindata"
    #path = "C:\\Users\\fei\\Desktop\\test"
    count = 0
    countfile = 0
    #fd = open("count.txt", "a+")
    for fpath, dirs, fs in os.walk(path):
        countfile = 0
        for f in fs:
            fileInfos = os.path.splitext(f)
            if fileInfos[1] =='.xml':
                jpgFile = fileInfos[0]+'.jpg'
                if jpgFile in fs:
                    xml_srcfile = os.path.join(fpath,f)
                    jpg_srcfile = os.path.join(fpath,jpgFile)

                    if(deleteNode_xml(xml_srcfile,'panel')):
                        count += 1

                countfile += 1
                #fd.write(f+'\n')
        if countfile != 0:
            info = fpath+"---总共标记："+ str(countfile)+'\n' + "---总共标记缺陷图片：" + str(count)+'\n'
            #fd.write(info)
            print(info)

    #fd.write( "*******************总共标记：*******" + str(count))

    #fd.close()



if __name__ == '__main__':
    sys.exit(main())

