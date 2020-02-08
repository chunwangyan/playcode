import pandas as pd
import os
import time

# df = pd.DataFrame({"id": range(5), "name": range(5, 10)})
#
# # print dataset
# print(df)
#
# # store the dataset
# pd.to_pickle(df, "/Users/yanchw/Desktop/Desktop/codes/python/playcode/dataSet/df.pkl")
#
# # load dataset
# input_df = pd.read_pickle("/Users/yanchw/Desktop/Desktop/codes/python/playcode/dataSet/df.pkl")
#
# print(input_df)
#
# # remove dataset
# os.remove("/Users/yanchw/Desktop/Desktop/codes/python/playcode/dataSet/df.pkl")

# pickle是python中用于对象存储的格式，类似于json，可以对python中各种数据类型进行序列化和反序列化
# 实现文件于内存对象之间的转换，进一步了解可参考：https://cloud.tencent.com/developer/article/1572624

# 通用全局变量初始化配置
config = {
    "picklefilepath": "/Users/yanchw/Desktop/Desktop/codes/python/playcode/dataSet/pickle/"
}

# 全局通用日期
dateday = time.strftime("%Y-%m-%d", time.localtime(time.time()))


# pickle对象的输入/输出
class pickling(object):
    def obj_to_file(self, datasetobj, filepath):
        # 首先，判断文件目录是否存在，如是，直接存储数据，如否，先创建文件夹然后存储数据
        if (os.path.exists(filepath)):
            print("文件夹存在，输出对象至文件！")
            filename = filepath + "df%s.pkl" % (dateday)
            pd.to_pickle(datasetobj, filename)
        else:
            print("文件夹不存在，先创建然后输出对象至文件！")
            os.mkdir(filepath)
            filename = filepath + "df%s.pkl" % (dateday)
            pd.to_pickle(datasetobj, filename)

    def file_to_obj(self):
        pass

    def def_file(self):
        pass


if __name__ == '__main__':
    df = pd.DataFrame({"id": range(5), "name": range(5, 10)})
    pickobj = pickling()
    pickobj.obj_to_file(df, config["picklefilepath"])
