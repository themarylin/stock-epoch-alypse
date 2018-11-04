
import os
import os.path
import rando

from dotenv import load_dotenv

from flask import Flask
from flask import jsonify
from flask import request
from flask import url_for
from flask import render_template

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import and_

import pymysql
import json
from decimal import *

from flask.json import JSONEncoder
from datetime import date

from random import random, randint
import pandas as pd



pymysql.install_as_MySQLdb()
load_dotenv()



username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
database = os.getenv("DATABASE_NAME")




connection = f"mysql://{username}:{password}@{host}:{port}/{database}"

Base = automap_base()
engine = create_engine(connection, pool_recycle=1)
conn = engine.connect() 



Base.prepare(engine, reflect=True)
StockData = Base.classes.sp5data
session = Session(bind=engine)


stk_list = []
for stk in session.query(StockData.stock).filter(and_(StockData.date.between('2015-09-30', '2018-09-28'), StockData.adj_close.isnot(None))).distinct():
    stk_clean = str(stk)[2:-3]
    stk_list.append(stk_clean)




rand_stock_num = randint(0, len(stk_list)-1)

rand_stock = stk_list[rand_stock_num]
print(rand_stock)




stk_rand_df = pd.DataFrame(columns=['stock','date','adj_close','comp_earning','adj_comp_earning'])
stk_rand_stock_list =[]
stk_rand_date_list =[]
stk_rand_adj_close_list =[]
stk_rand_comp_earning_list =[]




prev_stock = 0
curr_comp_earn = 1
prev_adj_close = 0
kwargs = {'stock': rand_stock}
for stk_rand in session.query(StockData.date,StockData.stock,StockData.adj_close).filter_by(**kwargs).filter(StockData.date.between('2015-09-30', '2018-09-28')):
    stk_rand_stock_list.append(stk_rand.stock)
    stk_rand_date_list.append(stk_rand.date)
    stk_rand_adj_close_list.append(stk_rand.adj_close)
    curr_stock = random() < 0.5
    if curr_stock == False:
        curr_stock= 0
    else:
        curr_stock= 1
    sellbuy_scen = random() < 0.5
    if sellbuy_scen == False:
        sellbuy_scen= 0
    else:
        sellbuy_scen= 1
#     print(f'date:{stk_rand.date}')        
#     print(f'current stock value:{curr_stock}')
#     print(f'previous stock value:{prev_stock}')
#     print(f'sell/buy scenario stock value:{sellbuy_scen}') 
    
    if prev_adj_close == 0:
        prev_adj_close = stk_rand.adj_close
    
    curr_adj_close = stk_rand.adj_close
    
#     print(f'previous adj close:{prev_adj_close}')
#     print(f'curr adj close:{curr_adj_close}')
    
    if prev_stock == 0 and curr_stock == 0:
#         print(f'Current Compound Earnings:{curr_comp_earn}')            
        stk_rand_comp_earning_list.append(curr_comp_earn)
        prev_adj_close=curr_adj_close
        continue
    if prev_stock == 0 and curr_stock == 1:
        prev_stock = 1
#         print(f'Current Compound Earnings:{curr_comp_earn}')            
        stk_rand_comp_earning_list.append(curr_comp_earn)   
        prev_adj_close=curr_adj_close        
        continue
    if prev_stock == 1 and curr_stock == 1:
#         print(f'Current Compound Earnings:{curr_comp_earn}')            
        stk_rand_comp_earning_list.append(curr_comp_earn) 
        prev_adj_close=curr_adj_close        
        continue
    if prev_stock == 1 and curr_stock == 0:
        if sellbuy_scen == 0:
            curr_comp_earn=(((curr_adj_close-prev_adj_close)/prev_adj_close)+1)*curr_comp_earn
            prev_stock = 0
        else:
            curr_comp_earn=(((curr_adj_close-prev_adj_close)/prev_adj_close)+1)*curr_comp_earn
        
#     print(f'Current Compound Earnings:{curr_comp_earn}')            
    stk_rand_comp_earning_list.append(curr_comp_earn)
    prev_adj_close=curr_adj_close
        
# print(f'Final Compound Earnings:{curr_comp_earn}')  



stk_rand_df['stock']=stk_rand_stock_list
stk_rand_df['date']=stk_rand_date_list
stk_rand_df['adj_close']=stk_rand_adj_close_list
stk_rand_df['comp_earning']=stk_rand_comp_earning_list



stk_rand_adj_comp_earning_list = [value-1 for value in stk_rand_comp_earning_list]

len(stk_rand_adj_comp_earning_list)



# stk_rand_df



stk_rand_df['adj_comp_earning']=stk_rand_df.comp_earning-1

# stk_rand_df.tail(10)

