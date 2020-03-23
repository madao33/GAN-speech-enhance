# coding=utf-8
 
from sphfile import SPHFile
import glob
import os
import sys
 
if __name__ == "__main__":
    path = '/home/madao/文档/codes/python/GanSound/TIMIT/TEST/DR2/'
    files = os.listdir(path)      #返回指定路径下的文件和文件夹列表
    print(files)
    for file in files:
        path_n = os.path.join(path, file)  # 连接两个或更多的路径名
        # print(path_n)
        path_ns = path_n+ "/" + "*.WAV"
        print(path_ns)
 
        #file_n = os.listdir(path_n)     #返回指定路径下的文件和文件夹列表
        # print(file_n)
 
        # for i in file_n:      # 循环读取路径下的文件并筛选输出 (可行)
        #     if os.path.splitext(i)[1] == ".wav":  # 筛选 wav文件
        #         print(i)  # 输出所有的 wav文件
        # os.system("pause")
 
        sph_files = glob.glob(path_ns)      #返回所有匹配的文件路径列表
        print(len(sph_files), "train utterences")
        print(sph_files)
        # os.system("pause")
 
        for i in sph_files:
            sph = SPHFile(i)
            sph.write_wav(filename=i.replace(".WAV", "_N.WAV"))   #保存在源文件所在文件夹
            print(i)
            # os.remove(i)    # 不用删除语音文件
        print("Completed")
        # os.system("pause")