import pymysql
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 日期参数
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# 时间参数
today_time = today.strftime('%Y-%m-%d') + ' 16:00:00'
yesterday_time = yesterday.strftime('%Y-%m-%d') + ' 16:00:00'

# 数据库连接参数配置
db_config = {
    "host": "rr-2zef6116602572p0gbo.mysql.rds.aliyuncs.com",
    "user": "prod_aipc_rr_big",
    "password": "",
}

sql_str = """SELECT
  a.memberId 会员id,
  c.mobile 手机号,
  a.payTime 充值时间,
  a.money 充值金额单位分,
  a.refoundmoney 赠送余额单位分
FROM
  (SELECT
    memberId,
    money,
    payTime,
    CASE
      WHEN money >= 500
      AND money < 1000
      THEN 150
      WHEN money >= 1000
      AND money < 3000
      THEN 350
      WHEN money >= 3000
      AND money < 4000
      THEN 1500
      WHEN money >= 4000
      AND money < 5000
      THEN 1800
      WHEN money >= 5000
      AND money < 10000
      THEN 2000
      WHEN money >= 10000
      AND money < 30000
      THEN 3000
      WHEN money >= 30000
      THEN 6000
      ELSE 0
    END refoundmoney
  FROM
    `prod_aipc_memberdb`.`t_recharge`
  WHERE money >= 500
    AND payTime >= %s -- 活动期间统计前一日下午4点到本日下午4点的充值明细数据,25号最后一天给11月25号下午4点到25号0点数据
     AND payTime <= %s) a
  LEFT JOIN
    (SELECT
      memberId,
      mobile
    FROM
      `prod_aipc_memberdb`.`t_member`) c
    ON a.memberId = c.memberId
ORDER BY a.payTime DESC
"""

# 创建文件目录
file_dir = "/Users/yanchw/Desktop"

# 邮件服务器
email_host = "smtp.qiye.163.com"

# 设置邮件发送者和接收者地址
email_sender = ''
email_receivers = ['']

# 邮箱密码
email_password = ""


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
            cursor.execute(sql_str, (yesterday_time, today_time))
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
        file_name = '%s/hd_recharge%s.csv' % (file_dir, today)
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


# 邮件操作类
class email_operation:

    # 邮件初始化
    def email_init(self):
        # 邮件标题
        email_subject = '邯郸充值返利活动%s数据导出' % (today)
        # 邮件正文内容
        email_message_content = MIMEText("Hi:附件中是%s至%s邯郸项目充值明细，请研发参照附件内容进行充值。" % (yesterday_time, today_time), "plain",
                                         "utf-8")
        # 邮件附件内容
        file_name = '%s/hd_recharge%s.csv' % (file_dir, today)
        email_att = MIMEText(open(file_name, "rb").read(), "base64", "utf-8")
        email_att["Content-Type"] = 'application/octet-stream'
        email_att["Content-Disposition"] = 'attachment; filename=hd_recharge%s.csv' % (today)
        # 构造邮件
        email_message = MIMEMultipart()
        email_message.attach(email_message_content)
        email_message.attach(email_att)
        email_message["From"] = Header("yanchw", "utf-8")
        email_message["To"] = Header("yanchw", "utf-8")
        email_message["Subject"] = Header(email_subject, "utf-8")
        return email_message

    # 发送邮件
    def email_send(self, email_message):
        try:
            smtp_obj = smtplib.SMTP(host=email_host)
            smtp_obj.login(email_sender, password=email_password)
            smtp_obj.sendmail(email_sender, email_receivers, email_message.as_string())
            print("邮件发送成功")
        except:
            print("邮件发送失败")


if __name__ == '__main__':
    # 实例化一个db操作对象
    db_obj = db_operation()
    # 连接数据库
    db_res = db_obj.db_connct()
    # 查询并返回结果
    sl_res = db_obj.db_select(db_res)
    # print(sl_res)
    # 关闭数据库
    db_obj.db_close(db_res)

    # 实例化一个file操作对象
    file_obj = file_operation()
    # 文件初始化
    filename = file_obj.file_name_init()
    # print(filename)
    # 判断文件是否存在，如是，则删除该存在的文件
    file_obj.file_is_exists(filename)
    # 将查询记录插入文件中
    file_obj.write_res_to_file(filename, sl_res)

    email_obj = email_operation()
    res_message = email_obj.email_init()
    email_obj.email_send(res_message)
