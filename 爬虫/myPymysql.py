# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:57:28 2018

@author: Administrator
"""

import pymysql

class DBHelper:
    def __init__(self,host='127.0.0.1',user='root',pwd='123456',db='MaoYan',port=3306,charset='utf8'):
        self.host=host
        self.user=user
        self.password=pwd
        self.db=db
        self.port=port
        self.charset=charset
        self.conn=None
        self.cursor=None
    
    def connectDataBase(self):
        try:
            self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,
                                        db=self.db,charset=self.charset,port=self.port)
        except:
            print("connectDataBase error")
            return False
        
        self.cursor = self.conn.cursor()
        return True
            
    def execute(self,sql,params=None):
        if self.connectDataBase() == False:
            return False
        
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql,params)
                self.conn.commit()
        except:
            print("execute "+sql+" error")
            return False
        return True
            
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        return True
    
if __name__ == '__main__':
    dbhelper = DBHelper()
    #dbhelper.connectDataBase()

    title = '碟中谍6'
    star = '汤姆布鲁斯'
    time = '2018-08-29'
    sql = 'INSERT INTO MaoYan.top100(title,star,time) VALUES(%s,%s,%s)'
    params = (title,star,time)
    if dbhelper.execute(sql,params) == True:
        print('插入成功')
    dbhelper.close()