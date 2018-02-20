# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:24:31 2018

@author: Ankur
"""

import sqlalchemy as sa

engine = sa.create_engine('mssql+pyodbc://sa:ankur@TestDBSQLSERVER')

sql = """insert into sample(id,name,sal) values (29,'mishra',77)"""
with engine.begin() as con:
    con.execute("insert into sample(id,name,sal) values (22,'alok',234)")
    con.execute("insert into sample(id,name,sal) values (42,'praksh',34)")
    con.execute(sql)
    
result = engine.execute("select * from sample")

for row in result:
    print(row)