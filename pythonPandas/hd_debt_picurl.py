import requests
import pandas as pd
import json


class hdPicService(object):
    def hdDebtPicurl(self, oprnum_dic):
        with open("/Users/yanchw/Desktop/hd_debt_info.txt", "w") as f:
            for index, row in oprnum_dic.iterrows():
                # print(index)
                # print(row[0])
                # print(row[1])
                # print('---------------------')
                entryurl = "http://pic.hd.aipark.com/picture/2.0/business/query/" + row[0]
                exiturl = "http://pic.hd.aipark.com/picture/2.0/business/query/" + row[1]
                # print(entryurl, exiturl)
                respose_entry = json.loads(requests.get(entryurl).text)
                respose_exit = json.loads(requests.get(exiturl).text)
                print(respose_entry["value"], respose_exit["value"])
                f.write(json.dumps(respose_entry))
                f.write("\n")
                f.write(json.dumps(respose_exit))
                f.write("\n")


if __name__ == '__main__':
    localpath = "/Users/yanchw/Desktop/hd_debt_info.xlsx"
    df = pd.read_excel(localpath)
    oprnum_dic = {}
    oprnum_dic = df[["进场oprnum", "出场oprnum"]]
    res = hdPicService()
    res.hdDebtPicurl(oprnum_dic)
