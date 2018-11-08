# Stock Epoch-Alypse
Deployed on AWS: http://ec2-3-16-30-247.us-east-2.compute.amazonaws.com:5000/

## Introduction
This application is designed for stock market newcomers and how they can use machine learning for trading. 
The application offers 4 scenarios to compare stock prices:
 - Machine learning trading scenario (tensor flow neural network trained on the S&P500 daily adjusted close)
 - Ideal trading scenario (trading with perfect knowledge of the future)
 - Random trading scenario (based on a random stock buy/sell/hold randomly)
 - S&P500 hold trading scenario (buys on 9/30/2015 then sells on 9/28/2018)

## Requirements

This application requires Python 3.6 to run and access to a MySQL instance 5.6 or greater.

## Installation

1. Copy the `.env.example` file at the root of the repository and rename it `.env`; 
   update the environment variables so it can connect to the database that you created or procured for this application.

## Running the Application

Now you should be able to launch the Flask application:

```bash
FLASK_APP=app.py flask run
```

Or simply:

```bash
python app.py
```

## Data Collection

Parsed data in python and filtered by S&P500 stocks:

Stock API Data from Quotemedia:
https://www.quandl.com/api/v3/databases/EOD/

S&P500 Stocks as of 11/1/2018:
https://us.spdrs.com/site-content/xls/SPY_All_Holdings.xls



## Back End

Using Python Pandas imported data tables into Amazon Web Services connected MySQL database
