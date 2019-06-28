#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @author   : Feifei
# @IDE      : Pycharm
# @file     : mergebatfile.py
# @time     : 2019/6/3 14:41

import os
import sys


def mergeBat(inputPath,outputPath):

    listpaths = []
    files = os.listdir(inputPath)

    for file in files:
        if os.path.splitext(file)[1] == '.dat':
            listpaths.append(file)


    if os.path.splitext(outputPath)[1] != '.dat':
        print("请输入正确的输入文件。")
        return

    listinfos = []


    for path in listpaths:
        pathos = os.path.join(inputPath,path)
        with open(pathos,'r') as f:
            while True:
                line = f.readline()
                if line:
                    if (-1 != line.find("info")):
                        listinfos.append(line)
                    else:
                        with open(outputPath,'a+') as wf:
                            wf.write(line)
                else:
                    break

    with open(outputPath, 'a+') as wf:
        wf.write(InfoSum(listinfos))


def InfoSum(infos):

    imgCount = 0
    flytime = 0.0
    flyDistance = 0.0
    defImgs = 0
    defPanels = 0
    m_hotPoints = 0
    m_serHotPoints = 0
    m_norHotPoints = 0



    for info in infos:
        strs = info.split("#")
        digitals = strs[1].split("*")

        imgCount += int(digitals[0])
        flytime += float(digitals[1])
        flyDistance += float(digitals[2])
        defImgs += int(digitals[3])
        defPanels += int(digitals[4])
        m_hotPoints += int(digitals[5])
        m_serHotPoints += int(digitals[6])
        m_norHotPoints += int(digitals[7])

    infoStr = "info#"+str(imgCount) + "*" + str(flytime) + "*" + str(flyDistance) + \
            "*" + str(defImgs) + "*" + str(defPanels) + "*" + str(m_hotPoints) + "*" + \
            str(m_serHotPoints) + "*" + str(m_norHotPoints)

    return infoStr



def main(argv = None):
    listPaths = ["C:\\Users\\fei\\Desktop\\云南永仁电站35mw热斑检测文件\\1区（2版）.dat",
                 "C:\\Users\\fei\\Desktop\\云南永仁电站35mw热斑检测文件\\2-3区（2版）.dat"]
    inputPath = "C:\\Users\\fei\\Desktop\\云南永仁电站35mw热斑检测文件"
    outputPath = "C:\\Users\\fei\\Desktop\\云南永仁电站35mw热斑检测文件\\summary.dat"

    mergeBat(inputPath,outputPath)



if __name__ == '__main__':
    sys.exit(main())












