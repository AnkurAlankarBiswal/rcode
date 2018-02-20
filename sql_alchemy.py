# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:09:44 2018

@author: Ankur
"""
#test example

import sqlalchemy as sa

engine = sa.create_engine('mssql+pyodbc://sa:ankur@TestDBSQLSERVER')

result = engine.execute("select * from sample")

for row in result:
    print(row)
    

