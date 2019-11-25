import requests
import json
import time
import pandas as pd

# 配置信息
config = {

    # 输入文件路径
    "input_filePath": "C:/Users/zhht/Desktop/hd_debt/debtorder.csv",

    # 输出文件路径
    "output_filePath": "C:/Users/zhht/Desktop/hd_debt/debtorder2.csv",

    # 图片不完备的carId存储路径，避免多次请求图片接口
    "carIdSet_filePath": "C:/Users/zhht/Desktop/hd_debt/carIdSet.txt",

    # 会员欠费明细文件路径
    "member_result_path": "C:/Users/zhht/Desktop/hd_debt/member_detail.csv",

    # 非会员欠费明细文件路径
    "non_member_result_path": "C:/Users/zhht/Desktop/hd_debt/mm_member_detail.csv",

    # 图片服务接口
    "picService_url": "http://pic.hd.aipark.com/picture/2.0/business/query/",

    # 金额区间划分
    "listBins": [0, 5000, 10000, 20000, 30000, 40000, 50000, 10000000000],

    # 区间标签
    "listLabels": ['<50', '50-100', '100-200', '200-300', '300-400', '400-500', '>500']
}


# 邯郸图片接口服务
def getPictureByOprNum(oprNum):
    try:
        response = json.loads(requests.get(config["picService_url"] + oprNum).text)
        if response["state"] == 0:
            return response
        else:
            return None
    except:
        return None


# 判断图片是否完备 0-完备，1-不完备
def isFull(jsonData):
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


# 读取文件,找出图片不完备的carId
def filterCarId(path):
    carIdSet = set()
    csv_data = pd.read_csv(config["inputFilePath"])
    carId_oprNum = csv_data[["carId", "oprNum"]]
    for row in carId_oprNum.iterrows():
        time.sleep(0.5)
        oprNum = row["oprNum"]
        carId = row["carId"]
        if carId in carIdSet:
            continue
        else:
            response = getPictureByOprNum(oprNum)
            flag = isFull(response)
            if flag == 1:
                carIdSet.add(carId)
    return carIdSet


# 删除图片不完备的carId存在的行
def getFilteredData(carIdSet):
    csv_data = pd.read_csv(config["input_filePath"])
    csv_data = csv_data[~csv_data["carId"].isin(carIdSet)]
    csv_data.to_csv(config["output_filePath"])
    return csv_data


# 统计每辆车的欠费金额
def moneyStatics(data, isRegister, savePath):
    if isRegister == 1:
        data_new = data[~data["memberId"].str.contains("N")]
    elif isRegister == 0:
        data_new = data[data["memberId"].str.contains("N")]
    else:
        raise ValueError("isRegister只有0，1两种值！")
    data_new.to_csv(savePath)
    result = data_new.groupby("carId")["money"].sum()
    dict_result = {"carId": result.index, "totalMoney": result.values}
    return pd.DataFrame(dict_result)


# 根据区间进行分组
def dataCut(data):
    listBins = config["listBins"]
    listLabels = config["listLabels"]
    data["label"] = pd.cut(data["totalMoney"], bins=listBins, labels=listLabels, include_lowest=True)
    return data


# 根据分组进行汇总统计
def groupResult(data):
    return data.groupby("label").agg({"totalMoney": pd.Series.sum, "carId": pd.Series.count})


if __name__ == '__main__':
    # 第一步，调用图片服务，找出图片不完备的carId集合，并保存
    carIdSet = filterCarId(config["input_filePath"])

    # carIdSet = ("1968654688276860032", "1968654515123408384", "1974890979922497664")

    # 第二步，删除原始数据中图片不完备的carId，并保存为新文件
    filteredData = getFilteredData(carIdSet)

    # 第三步，获取会员和非会员的明细数据，并保存文件
    member_detail = moneyStatics(filteredData, 1, config["member_result_path"])
    non_member_detail = moneyStatics(filteredData, 0, config["non_member_result_path"])

    # 第四步，对明细数据进行金额分组打标签
    group_member = dataCut(member_detail)
    group_non_member = dataCut(non_member_detail)

    # 第五步，统计区间分组汇总结果
    print("------------------会员汇总结果------------------")
    print(groupResult(group_member))
    print("------------------非会员汇总结果------------------")
    print(groupResult(group_member))
