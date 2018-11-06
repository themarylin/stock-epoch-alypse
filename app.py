import os
import os.path

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
from sqlalchemy import desc
from sqlalchemy import and_

import pymysql
import json
from decimal import *

from flask.json import JSONEncoder
from datetime import date
from random import random, randint

pymysql.install_as_MySQLdb()
load_dotenv()

from NN.pickle_load import load_and_plot
from rando import randomStock
import numpy

# Custom Encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


# #################################################
# # Database Setup
# #################################################
username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
database = os.getenv("DATABASE_NAME")

# Format:
# <Dialect>://<Username>:<Password>@<Host Address>:<Port>/<Database>`
# Using f-string notation: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
connection = f"mysql://{username}:{password}@{host}:{port}/{database}"

Base = automap_base()
engine = create_engine(connection, pool_recycle=1)
# <-- this line is not strictly necessary, but it's ref'd in the docs
conn = engine.connect()

# Generating base classes
Base.prepare(engine, reflect=True)
StockData = Base.classes.sp5data
ScenarioData = Base.classes.scenarios

#########################################################
# List of distinct stocks #
#########################################################
session = Session(bind=engine)
stk_list = []
for stk in session.query(StockData.stock).filter(and_(StockData.date.between('2015-09-30', '2018-09-28'), StockData.adj_close.isnot(None))).distinct():
    stk_clean = str(stk)[2:-3]
    stk_list.append(stk_clean)
session.close()

#########################################################
# Flask Setup #
#########################################################

app = Flask(__name__, static_folder='./static', static_url_path='')
app.config['JSON_SORT_KEYS'] = False
app.json_encoder = CustomEncoder

#########################################################
# Flask Routes #
#########################################################


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get-started")
def get_started():
    return render_template('get-started.html')


@app.route("/machinelearning")
def machinelearning():
    return render_template('machinelearning.html')


@app.route("/comparison")
def comparison():
    return render_template('comparison.html')

@app.route("/apiendpoints")
def endpoints():
    return render_template('apiendpoints.html')

#########################################################
# API Endpoints #
########################################################

# Endpoint for Disney
@app.route("/api", methods=['GET'])
def get_json():
    stock_ticker = request.args.get('stock')
    session = Session(bind=engine)
    results = session.query(
        StockData.date, StockData.adj_close).filter_by(stock=stock_ticker)
    session.close()
    return jsonify(
        {'company': stock_ticker,
         'data': [
             {
                 'date': result.date.strftime("%Y-%m-%d"),
                 'price': result.adj_close
             }
             for result in results
         ]
         }
    )

# Endpoint for Machine Learning Results
@app.route("/api/ml", methods=['GET'])
def get_ml():

    stock_ticker = request.args.get('stock')
    n_neurons = 256
    n_epochs = request.args.get('epochs')
    learning_rate = request.args.get('learnrate')
    future_days = 1
    split = request.args.get('split')

    data = load_and_plot(n_neurons=n_neurons, n_epochs=n_epochs, learning_rate=learning_rate, future_days=future_days, stock_ticker=stock_ticker, split=split)
    return jsonify(
        {
            'company': stock_ticker,
            'n_neurons': n_neurons,
            'n_epochs': n_epochs,
            'learning_rate':learning_rate,
            'future_days':future_days,
            'split':split,
            'data': data
        }
    )

# Endpoint for random stock
@app.route("/api/rand", methods=['GET'])
def get_json_rand():
    session = Session(bind=engine)
    rand_stock_num = randint(0, len(stk_list)-1)
    rand_stock = stk_list[rand_stock_num]
    kwargs = {'stock': rand_stock}
    results = session.query(StockData.date,StockData.stock,StockData.adj_close).filter_by(**kwargs).filter(StockData.date.between('2015-09-30', '2018-09-28'))
    session.close()
    stock_data = randomStock(rand_stock,results)
    return jsonify(stock_data)

# Endpoint for Scenarios Comparison
@app.route("/api/scen", methods=['GET'])
def get_json_scen():
    
    session = Session(bind=engine)
    results = session.query(
        ScenarioData.date, ScenarioData.ideal_compound_earning_adj, ScenarioData.snp500_earning_adj, ScenarioData.ml_earning_adj)
    session.close()
    return jsonify(
        {
         'data': [
             {
                 'date': result.date.strftime("%Y-%m-%d"),
                 'ideal_earning': result.ideal_compound_earning_adj,
                 'snp_500': result.snp500_earning_adj,
                 'ml': result.ml_earning_adj
             }
             for result in results
         ]
         }
    )
#########################################################
if __name__ == '__main__':
    app.run(debug=True)
