#cofing:utf8
'''
    该文档仅用于生成所有文件的路径存入f.txt中
    前期需将所有文件提取出来放在同一个目录下
    文件存放路径为F:\test\hksl
    工程存放路径为E:\python_work\dtProc\
    （也可另行编写代码遍历目录下的所有子目录以读取所有文件路径）
'''
import os

with open(r"E:\python_work\dtProc\f.txt",'w+') as f:
    for root,dirs,files in os.walk(r"F:\test\hksl"):
        print(root,dirs,files)
    for i in files:
        print(root + "\\" + i + "\n")
        f.write(root + "\\" + i + "\n")
f.close()