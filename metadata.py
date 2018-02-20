# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:59:06 2018

@author: Ankur
"""

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc://sa:ankur@TestDBSQLSERVER')

metadata = MetaData()

user_table = Table('sampletest',metadata,
                   Column('id',Integer),
                   Column('name',String),
                   Column('fulname',String)
                   )

user_table.create(engine)

print(user_table.name)

print(user_table.columns)

