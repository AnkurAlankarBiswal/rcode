import pyodbc
import pandas as pd
import pymysql
import sqlalchemy as sa



cnxn = pyodbc.connect(r'Driver={SQL Server};server=localhost;database=TestDB;uid=sa;pwd=ankur');

cursor = cnxn.cursor() 

sql = """select * from sample""" 

df = pd.read_sql(sql,cnxn);

cnxn1 = pymysql.connect("127.0.0.1","root","ankur","test")

sql = """select * from sample""" 

df1 = pd.read_sql(sql,cnxn1);

df.columns = ['id', 'name', 'sal1']

sql.write_frame(df, con=cnxn1, name='sample')

engine = sa.create_engine('mssql+pyodbc://sa:ankur@TestDBSQLSERVER')

