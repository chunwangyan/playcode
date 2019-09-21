from urllib import request
import pandas as pd
import json

d = pd.read_csv('/Users/yanchw/Desktop/debtorder.csv', header=1)

dd = open("/Users/yanchw/Desktop/debtorder_out.csv", "w")

d.columns = ['debtOrderId', 'parkRecordId', 'carId',
             'money', 'entryTime', 'exitTime', 'createdTime',
             'updatedTime', 'remoney', 'reshouldPay', 'carId',
             'memberId', 'memberCarState', 'memberId', 'mobile',
             'memberState', 'parkRecordId', 'entryId', 'exitId',
             'parkId', 'berthCode', 'plateNumber', 'ocrRecordId', 'entryOprNum', 'oprNum']
print(d.head(5))

# key = []
# value = []

for line in d['oprNum']:
    url = 'http://pic.hd.aipark.com/picture/2.0/business/query/' + line
    tmp = request.urlopen(url)
    res_dic = json.loads(tmp.read().decode())
    for value in res_dic.keys():
        if value == "value":
            # print(line + ',' + '1')
            dd.write(line + ',' + '1' + '\n')


dd.close()
