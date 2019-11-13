#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 Purpose: 生成日汇总对账文件
 Created: 2015/4/27
 Modified:2015/5/1
 @author: guoyJoe
"""
# 导入模块
import MySQLdb
import time
import datetime
import os

# 日期
today = datetime.date.today()
yestoday = today - datetime.timedelta(days=1)
# 对账日期
checkAcc_date = yestoday.strftime('%Y%m%d')
# 对账文件目录
fileDir = "/u02/filesvrd/report"
# SQL语句
sqlStr1 = 'SELECT distinct pay_custid FROM dbpay.tb_pay_bill WHERE date_acct = %s'
# 总笔数|成功交易笔数|成功交易金额|退货笔数|退货金额|撤销笔数|撤销金额
sqlStr2 = """SELECT totalNum,succeedNum,succeedAmt,returnNum,returnAmt,revokeNum,revokeAmt
  FROM
    (SELECT count(order_id) AS totalNum
      FROM (SELECT p.order_id as order_id
        FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.paycust_accttype = 2
        AND p.Paycust_Type = 1
        AND p.stat_bill in (0, 4)
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.pay_custid = %s
        AND q.date_acct = %s
        UNION ALL
        SELECT p.order_id as order_id
        FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.col_accttype = 2
        AND p.col_type = 1
        AND p.stat_bill in (0, 4)
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.col_custid = %s
        AND q.date_acct = %s
        UNION ALL
        SELECT R.ORDER_ID AS ORDER_ID
        FROM DBPAY.TB_REFUND_BILL R, DBPAY.TB_PAYBILLSERIAL Q
        WHERE R.oid_refundno = Q.OID_BILLNO
         AND R.ORI_COL_ACCTTYPE = 2
         AND R.ORI_COL_TYPE = 1
         AND R.STAT_BILL = 2
         AND Q.PAY_STAT = 1
         AND Q.COL_STAT = 1
         AND R.ORI_COL_CUSTID = %s
         AND Q.DATE_ACCT = %s ) as total) A,
        (SELECT count(order_id) succeedNum ,sum(amt_paybill) succeedAmt
         FROM (SELECT p.order_id as order_id,
        q.amt_payserial/1000 as amt_paybill
        FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.paycust_accttype = 2
        AND p.Paycust_Type = 1
        AND p.stat_bill = '0'
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.pay_custid = %s
        AND q.date_acct = %s
        UNION ALL
        SELECT p.order_id as order_id,
        q.amt_payserial/1000 as amt_paybill
        FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.col_accttype = 2
        AND p.col_type = 1
        AND p.stat_bill = '0'
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.col_custid = %s
        AND q.date_acct = %s ) as succeed) B,
        (SELECT count(order_id) returnNum, sum(amt_paybill) returnAmt
        FROM (SELECT R.ORDER_ID AS ORDER_ID,
        Q.AMT_PAYSERIAL/1000 AS AMT_PAYBILL
        FROM DBPAY.TB_REFUND_BILL R, DBPAY.TB_PAYBILLSERIAL Q
        WHERE R.oid_refundno = Q.OID_BILLNO
         AND R.ORI_COL_ACCTTYPE = 2
         AND R.ORI_COL_TYPE = 1
         AND R.STAT_BILL = 2
         AND Q.PAY_STAT = 1
         AND Q.COL_STAT = 1
         AND R.ORI_COL_CUSTID = %s
         AND Q.DATE_ACCT = %s ) as retur) C,
         (SELECT count(order_id) revokeNum,sum(amt_paybill) revokeAmt
         FROM (SELECT p.order_id as order_id,
         q.amt_payserial/1000 as amt_paybill
         FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.paycust_accttype = 2
        AND p.Paycust_Type = 1
        AND p.stat_bill = '4'
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.pay_custid = %s
        AND q.date_acct = %s
        UNION ALL
        SELECT p.order_id as order_id,
        q.amt_payserial/1000 as amt_paybill
        FROM dbpay.tb_pay_bill p, dbpay.tb_paybillserial q
        WHERE p.oid_billno = q.oid_billno
        AND p.col_accttype = 2
        AND p.col_type = 1
        AND p.stat_bill = '4'
        AND q.pay_stat = 1
        AND q.col_stat = 1
        AND p.col_custid = %s
        AND q.date_acct = %s) as revok) D"""
try:
    # 连接MySQL数据库
    connDB = MySQLdb.connect("192.168.1.6", "root", "root", "test")
    connDB.select_db('test')
    curSql1 = connDB.cursor()
    # 查询商户
    curSql1.execute(sqlStr1, checkAcc_date)
    payCustID = curSql1.fetchall()
    if len(payCustID) < 1:
        print('No found checkbill data,Please check the data for %s!' % checkAcc_date)
        exit(1)
    for row in payCustID:
        custid = row[0]
        # 创建汇总日账单文件名称
        fileName = '%s/JYMXSUM_%s_%s.csv' % (fileDir, custid, checkAcc_date)
        # 判断文件是否存在, 如果存在则删除文件,否则生成文件！
        if os.path.exists(fileName):
            os.remove(fileName)
        print
        'The file start generating! %s' % time.strftime('%Y-%m-%d %H:%M:%S')
        print
        '%s' % fileName
        # 打开游标
        curSql2 = connDB.cursor()
        # 执行SQL
        checkAcc_date = yestoday.strftime('%Y%m%d')
        curSql2.execute(sqlStr2,
                        (custid, checkAcc_date, custid, checkAcc_date, custid, checkAcc_date, custid, checkAcc_date, c
                         ustid, checkAcc_date, custid, checkAcc_date, custid, checkAcc_date, custid, checkAcc_date))
        # 获取数据
        datesumpay = curSql2.fetchall()
        # 打开文件
        outfile = open(fileName, 'w')
        for sumpay in datesumpay:
            totalNum = sumpay[0]
            succeedNum = sumpay[1]
            succeedAmt = sumpay[2]
            returnNum = sumpay[3]
            returnAmt = sumpay[4]
            revokeNum = sumpay[5]
            revokeAmt = sumpay[6]
            # 生成汇总日账单文件
            outfile.write(
                '%s|%s|%s|%s|%s|%s|%s\n' % (totalNum, succeedNum, succeedAmt, returnNum, returnAmt, revokeNum, revo
                                            keAmt))
        outfile.flush()
        curSql2.close()
    curSql1.close()
    connDB.close()
    print
    'The file has been generated! %s' % time.strftime('%Y-%m-%d %H:%M:%S')
except MySQLdb.Error, err_msg:
    print
    "MySQL error msg:", err_msg
