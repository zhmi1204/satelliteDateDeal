#coding:utf8
import re
import readOBSERVandHEADER
sum = 0
valueError = 0
#第一次处理，此处为./f.txt
#第二次处理，此处为./ValueError.txt
#第三次处理，此处为./DoubleValueError
with open('./f.txt','r') as f:
    p = 1
    while p:
        FileURL = f.readline()
        print("FileURL:",FileURL,"-ValueError:", valueError,"-sum:",sum)
        if FileURL == '':
            f.close()
            break
        FileURL = re.split(r'\n', FileURL)[0].replace('\\\\', '\\')
        sum += 1
        #可完整读出C1L1...列表,返回值L2的下标index与列表长度length
        # try:
        try:
            readOBSERVandHEADER.readOBSERVandHEADER(FileURL)
        except ValueError:
            valueError += 1
            # print("ValueError----inner readFileURL------------------")
            # 第一次处理，此处为ValueError.txt
            # 第二次处理，此处为DoubleError.txt
            # 第三次处理，此处为TripleError.txt
            # with open('./ValueError.txt','a+') as m:
            #     m.write(FileURL + '\n')
            # m.close()
        # except OSError:
        #     print("ValueError----outer readFileURL------------------")
