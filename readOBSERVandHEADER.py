#coding:utf8
import re
import getINFO
def readOBSERVandHEADER(FileURL):
    with open(FileURL,"r") as a:
        #第一次与第二次处理，这个while True为
        # while True:
        #     tp_rd = a.readline()
        #     if re.search("# / TYPES OF OBSERV",tp_rd):
        #         tp_rds = re.split('\s+', tp_rd)[2:-6]
        #         length = len(tp_rds)
        #         index = tp_rds.index('L2')
        #         break
        #     else:
        #         continue

        #以下while True仅在第三次处理时改成这样
        while True:
            tp_rd = a.readline()
            if re.search("# / TYPES OF OBSERV", tp_rd):
                tp_rds1 = re.split('#', tp_rd)[0]
                tp_rds1 = re.split('\s+', tp_rds1)[2:]
                if tp_rds1[-1] == '':
                    tp_rds1 = tp_rds1[:-1]
                length1 = len(tp_rds1)
                if length1 == 9:
                    tp_rd = a.readline()
                    tp_rds2 = re.split('\s+', tp_rd)[1:-6]
                    length2 = len(tp_rds2)
                    index = (tp_rds1 + tp_rds2).index('L2')
                    length = length1 + length2
                else:
                    index = tp_rds1.index('L2')
                    length = length1
                break
            else:
                continue
        while True:
            tp_rd = a.readline()
            if re.search("END OF HEADER", tp_rd):
                break
            else:
                continue
        try:
            while True:
                counts = 0
                for i in range(12):
                    chk = a.readline()
                    chks = re.split('\s+',chk)
                    if chks[-1] == '':
                        chks = chks[:-1]
                    # print(chks)
                    date,stNo = getINFO.getDateAndSNum(chks)
                    stNo = int(stNo)
                    if stNo >= 13:
                        a.readline()
                    else:
                        pass
                    counts = getINFO.getCounts(stNo,length,index,counts,a)
                    #第一次处理，此处为savepath.txt
                    #第二次处理，此处为Doublesavepath.txt
                    #第三次处理，此处为Triplesavepath.txt
                with open(r'./savepath.txt', "a+") as t:
                    ct = str(date) + ' ' + str(counts) + '\n'
                    t.write(ct)
                t.close()
        except TypeError:
            print("TypeError----in readOBSERVHEAD----------------")
    a.close()
    return