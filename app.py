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

import pymysql
import json

# load_dotenv()

# pymysql.install_as_MySQLdb()

# #################################################
# # Database Setup
# #################################################
# username = os.getenv("DATABASE_USERNAME")
# password = os.getenv("DATABASE_PASSWORD")
# host = os.getenv("DATABASE_HOST")
# port = os.getenv("DATABASE_PORT")
# database = os.getenv("DATABASE_NAME")

# # Format:
# # `<Dialect>://<Username>:<Password>@<Host Address>:<Port>/<Database>`
# # Using f-string notation: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# connection = f"mysql://{username}:{password}@{host}:{port}/{database}"

# # engine = create_engine(connection, pool_recycle=1)
# engine = create_engine(connection)
# conn = engine.connect()  # <-- this line is not strictly necessary, but it's ref'd in the docs
# session = Session(bind=engine)

#########################################################
# Flask Setup #
#########################################################

app = Flask(__name__, static_folder='./static', static_url_path='')

#########################################################
# Flask Routes #
#########################################################

@app.route("/")
def index():
    return render_template('index.html')

#########################################################
# API Endpoints #
#########################################################

# @app.route("/api/v1.0/something")
# def something():
#     return jsonify(results)

#########################################################
if __name__ == '__main__':
    app.run(debug=True)