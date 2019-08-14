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


def main(argv = None):

    path = "F:\\ShareData\\无人机光伏电站数据\\售前试飞数据\\平地电站"

    dstPath = "F:\\ShareData\\标签数据\\624_hotpoint"

    count = 0
    countfile = 0
    fd = open("count.txt", "a+")
    for fpath, dirs, fs in os.walk(path):
        countfile = 0
        for f in fs:
            fileInfos = os.path.splitext(f)
            if fileInfos[1] =='.xml':
                jpgFile = fileInfos[0]+'.jpg'
                if jpgFile in fs:
                    xml_srcfile = os.path.join(fpath,f)
                    jpg_srcfile = os.path.join(fpath,jpgFile)
                    mycopyfile(xml_srcfile,dstPath,f)
                    mycopyfile(jpg_srcfile, dstPath, jpgFile)
                count += 1
                countfile += 1
                fd.write(f+'\n')
        if countfile != 0:
            info = fpath+"---总共标记："+ str(countfile)+'\n'
            fd.write(info)
            print(info)

    fd.write( "*******************总共标记：*******" + str(count))

    fd.close()



if __name__ == '__main__':
    sys.exit(main())