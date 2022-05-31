# -*-coding:utf-8-*-
import openpyxl
import os
import psycopg2
from psycopg2 import extras as ex


def sheet5(cur):
    wb = openpyxl.load_workbook(os.getcwd() + '/sql_app/hz.xlsx')
    sh = wb['Sheet5']

    datalist = []
    sql = '''insert into hanzi ("characterId","fileName",date,type,creator,source) values %s'''
    for cases in list(sh.rows)[1:]:
        characterId = "AT2601" + cases[5].value[:6]
        fileName = cases[5].value
        date = cases[1].value[3:] if cases[1].value != None else ""
        type = cases[2].value
        creator = cases[3].value
        source = cases[4].value
        datalist.append((characterId, fileName, date, type, creator, source))
    ex.execute_values(cur, sql, datalist, page_size=1000)


def sheet1(cur):
    wb = openpyxl.load_workbook(os.getcwd() + '/sql_app/hz.xlsx')
    sh = wb['Sheet2']

    datalist = []
    sql = '''update hanzi set pinyin=data.pinyin,tone=data.tone,title=data.title from (VALUES %s) AS data(characterId, pinyin, tone, title) where "characterId"=data.characterId'''
    for cases in list(sh.rows)[1:]:
        characterId = "AT2601" + str(cases[0].value).zfill(6)
        pinyin = cases[1].value
        tone = cases[2].value
        title = cases[3].value
        datalist.append((characterId, pinyin, tone, title))
    ex.execute_values(cur, sql, datalist, page_size=1000)


# 通过connect方法创建数据库连接
conn = psycopg2.connect(dbname="shufa", user="postgres",
                        password="123456", host="localhost", port="5432")

# 创建cursor以访问数据库
cur = conn.cursor()

sheet5(cur)
sheet1(cur)

# 提交事务
conn.commit()

# 关闭连接
conn.close()
