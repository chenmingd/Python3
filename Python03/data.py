#! /usr/bin/env python3
#-*- coding:utf-8 -*-
'数据库的操作'

'''sqlite数据库'''
import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor()
#cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#cursor.execute("insert into user(id,name) values ('3','chenmd')")
#cursor.execute("insert into user(id,name) values ('4','chenmd')")
cursor.execute("select * from user")
values=cursor.fetchall()
print(values)
cursor.execute("select * from user where id=?","1")
values=cursor.fetchall()
print(values)
#print(cursor.rowcount)
cursor.close()
#conn.commit()
conn.close()