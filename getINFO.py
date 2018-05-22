#coding:utf8

import re
def getDateAndSNum(list):
        global tmpEx
        date =list[1:6]
        for j in list:
            if re.search('0{4,5}', j)!= None:
                tmpEx = j
                break
            else:
                continue
        s_tmp = list.index(tmpEx) + 2
        stNo = list[s_tmp].split('G')[0]
        # print(date,stNo)
        return date, stNo

'''
@:param
    stNo:数据块（按5s划分）的卫星G01G02R11....的个数
    length:数据块中每一条数据的长度
    index:L2在#TYPES OF OBSERV中的下标
    counts:每分钟数据L2为空的counts
'''
def getCounts(stNo,length,index,counts,file):
    ptn = '\s+'
    for i in range(stNo):
        if 0<length<=5:
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len = len(t_tp)
            if index<= tmp_len -1:
                continue
            else:
                counts += 1
                continue
        elif 6<=length<=10:
            t_tp = re.split(ptn,file.readline())[1:-1]
            tmp_len = len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            if index <= tmp_len - 1:
                continue
            else:
                counts += 1
                continue
        elif 11<=length<=15:
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len = len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            if index <=tmp_len -1:
                continue
            else:
                counts += 1
                continue
        elif 16<=length<=20:
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len = len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            t_tp = re.split(ptn, file.readline())[1:-1]
            tmp_len += len(t_tp)
            if index <= tmp_len -1:
                continue
            else:
                counts += 1
                continue
        else:
            continue
    return counts