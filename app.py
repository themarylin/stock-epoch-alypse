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

import pymysql
import json
from decimal import *

from flask.json import JSONEncoder
from datetime import date

pymysql.install_as_MySQLdb()
load_dotenv()

# Custom datetime class


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
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
session = Session(bind=engine)

#########################################################
# Flask Setup #
#########################################################

app = Flask(__name__, static_folder='./static', static_url_path='')
app.json_encoder = DecimalEncoder

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


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

#########################################################


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/elements")
def elements():
    return render_template('elements.html')


@app.route("/single-blog")
def single():
    return render_template('single-blog.html')

#########################################################
# API Endpoints #
########################################################

# Endpoint for Disney


@app.route("/api/scen", methods=['GET'])
def get_json_scen():
    
    session = Session(bind=engine)
    results = session.query(
        ScenarioData.date, ScenarioData.ideal_compound_earning_adj)
    session.close()
    return jsonify(
        {
         'data': [
             {
                 'date': result.date.strftime("%Y-%m-%d"),
                 'ideal_earning': result.ideal_compound_earning_adj
             }
             for result in results
         ]
         }
    )



@app.route("/api", methods=['GET'])
def get_json():
    stock_ticker = request.args.get('stock')
    session = Session(bind=engine)
    results = session.query(
        StockData.date, StockData.adj_close).filter_by(stock=stock_ticker).limit(2000).all()
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

#########################################################
if __name__ == '__main__':
    app.run(debug=True)
