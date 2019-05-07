import os
import sys

def main(argv = None):
    path = "I:/无人机光伏电站数据/售前试飞数据/平地电站/20180811上汽安悦4MW/红外 上汽安悦4MW 20180811"
    files = os.listdir(path)

    count = 0
    countfile = 0
    fd = open("count.txt", "a+")
    for fpathe, dirs, fs in os.walk(path):
        countfile = 0
        for f in fs:
            if os.path.splitext(f)[1] =='.xml':
                count += 1
                countfile += 1
                fd.write(f+'\n')
        if countfile != 0:
            info = fpathe+"---总共标记："+ str(countfile)+'\n'
            fd.write(info)
            print(info)

    fd.write( "*******************总共标记：*******" + str(count))

    fd.close()



if __name__ == '__main__':
    sys.exit(main())