import pymysql
import os
import requests
import pandas as pd
import json
import time

# 数据库连接参数配置
db_config = {
    "host": "rr-2zef6116602572p0gbo.mysql.rds.aliyuncs.com",
    "user": "prod_aipc_rr_big",
    "password": "hfei34lei737FFFde"
}

pic_config = {
    # 图片服务接口
    "picService_url": "http://pic.hd.aipark.com/picture/2.0/business/query/",
    "inputFilePath": "/Users/yanchw/Desktop/hd_debt_order_full.csv"
}

sql_str = """"""

# 创建文件目录
file_dir = "/Users/yanchw/Desktop"


# 数据库操作类
class db_operation:
    # 数据库连接
    def db_connct(self):
        try:
            db = pymysql.connect(db_config["host"], db_config["user"], db_config["password"])
        except:
            print("数据库连接失败，请检查网络或者传入参数的合法性")
        return db

    # 数据库查询并返回结果
    def db_select(self, db):
        try:
            # 创建游标对象
            cursor = db.cursor()
            cursor.execute(sql_str)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
            print("数据库查询失败，请稍后尝试")

    # 数据库关闭
    def db_close(self, db):
        try:
            db.close()
        except:
            print("数据库关闭失败")


# 文件操作类
class file_operation:
    # 创建文件目录和文件名
    def file_name_init(self):
        file_name = '%s/hd_debt_order.csv' % (file_dir)
        return file_name

    # 判断文件是否存在，如否，则创建此文件
    def file_is_exists(self, file_name):
        try:
            if os.path.exists(file_name):
                print("删除已存在的文件")
                os.remove(file_name)
        except:
            print("文件已存在，但删除目录失败")

    # 打开文件，并将查询结果写入
    def write_res_to_file(self, file_name, sl_res):
        # 以可写方式打开文件
        out_file = open(file_name, 'w')
        # 循环写记录到文件
        for rc in sl_res:
            memberid = rc[0]
            mobile = rc[1]
            paytime = rc[2].strftime('%Y-%m-%d %H:%M:%S')
            money = rc[3]
            refoundmoney = rc[4]
            try:
                out_file.write('%s,%s,%s,%s,%s\n' % (memberid, mobile, paytime, money, refoundmoney))
            except:
                print("记录写入文件失败")
        out_file.close()


# 图片查询服务
class hd_pic_query:
    # 邯郸图片接口服务
    def getPictureByOprNum(self, oprNum):
        try:
            response = json.loads(requests.get(pic_config["picService_url"] + oprNum).text)
            if response["state"] == 0:
                return response
            else:
                return None
        except:
            return None

    # 读取文件,找出图片不完备的carId
    def hdPicQuerySum(self):
        entry_total_none = 0
        exit_total_none = 0
        csv_data = pd.read_csv(pic_config["inputFilePath"])
        df_entryOprNum = csv_data["entryOprNum"]
        df_exitOprNum = csv_data["exitOprNum"]
        for entryOprNum in df_entryOprNum:
            response_entryOprNum = self.getPictureByOprNum(entryOprNum)
            print(response_entryOprNum)
            flag_01 = self.isFull(response_entryOprNum)
            if flag_01 == 1:
                entry_total_none = entry_total_none + 1
        print(entry_total_none)  # 1812
        for exitOprNum in df_exitOprNum:
            response_exitOprNum = self.getPictureByOprNum(exitOprNum)
            flag_02 = self.isFull(response_exitOprNum)
            if flag_02 == 1:
                exit_total_none = exit_total_none + 1
        print(exit_total_none)  #
        return None

    # 判断图片是否完备 0-完备，1-不完备
    def isFull(self, jsonData):
        flag = 0
        if jsonData is None:
            flag = 1
        else:
            values = jsonData["value"]
            for value in values:
                if len(value["picUrl"]) == 0:
                    flag = 1
                    break
        return flag


if __name__ == '__main__':
    # 实例话一个图片查询对象
    hd_pic_query_obj = hd_pic_query()
    # 调用图片服务，汇总图片不全记录条数
    hd_pic_query_obj.hdPicQuerySum()

    #
