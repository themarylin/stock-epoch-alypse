# Import
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from datetime import datetime
import pickle
import pymysql
pymysql.install_as_MySQLdb()

# Settings for NN
future_time = 1
# list of stocks to train
stocks_to_train = ["DIS"]
# # of neurons in first layer, subsequent layers are //2 respectively
n_neurons = 256
epochs = 1000
# how often the graph visually updates(# of batches per update)
graph_updates = 5
batch_size = 256
learning_rate = .003  # .001 = og
# % is train,rest = test
train_test_split = .80

# import CSV file
data_raw = pd.read_sql_table(
    "sp500", "mysql://hjjms:uscdata123@stockml.cdav1uud78om.us-east-2.rds.amazonaws.com/stockAnalysis")

data_raw_1 = data_raw.fillna(0)
data_raw_1 = data_raw_1.query('index > 10000')

# forloop through stocks in NN
for train_stock in stocks_to_train:

    # date column
    dates_raw = data_raw_1['date']
    # drop date variable
    data_all = data_raw_1.drop(['date'], 1)
    dates = []

    # train_column is the stock that we want to predict
    train_column = data_all.columns.get_loc(train_stock)
    # n just contains the size of the array
    n = data_all.shape[0]
    p = data_all.shape[1]
    # make data a np.array(for inputting)
    data = data_all.values
    print(p)
    print(n)

 # Splitting training and test set into 2 diff arrays
    train_start = 0
    train_end = int(np.floor(train_test_split*n))
    test_start = train_end + 1
    test_end = n
    data_train = data[np.arange(train_start, train_end), :]
    data_test = data[np.arange(test_start, test_end), :]

    # Scale data
    # scaler = MinMaxScaler(feature_range=(-1, 1))
    # scaler.fit(data_train)
    # data_train = scaler.transform(data_train)
    # data_test = scaler.transform(data_test)

    # Build X and y
    # X_train = [:-future, 1:] disregarding last data point so the sizes of the arrays match(shift the time frame so that when we are comparing
    # the already shifted snp500 data, to the correctly correlated time in the DIS stock index)
    X_train = data_train[:-future_time, :]
    y_train = data_train[future_time:, train_column]
    X_test = data_test[:-future_time, :]
    y_test = data_test[future_time:, train_column]
    print(y_test)
    # pulling out dates that we are testing on for plotting
    dates_test = dates_raw[
        test_start + future_time: test_end + future_time]
