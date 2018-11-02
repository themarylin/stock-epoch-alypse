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

    # Number of stocks in training data
    n_stocks = X_train.shape[1]
    n_stocks

    # Neurons
    n_neurons_1 = n_neurons
    n_neurons_2 = n_neurons_1//2
    n_neurons_3 = n_neurons_2//2
    n_neurons_4 = n_neurons_3//2

    # Session
    net = tf.InteractiveSession()

    # Placeholder
    X = tf.placeholder(dtype=tf.float32, shape=[None, n_stocks])
    Y = tf.placeholder(dtype=tf.float32, shape=[None])

    # Initialize weights and bias of NN using uniform distribution and fan_avg
    sigma = 1
    weight_initializer = tf.variance_scaling_initializer(
        mode="fan_avg", distribution="uniform", scale=sigma)
    bias_initializer = tf.zeros_initializer()

    # Hidden weights-self exp
    W_hidden_1 = tf.Variable(weight_initializer([n_stocks, n_neurons_1]))
    bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
    W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
    bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
    W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
    bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))
    W_hidden_4 = tf.Variable(weight_initializer([n_neurons_3, n_neurons_4]))
    bias_hidden_4 = tf.Variable(bias_initializer([n_neurons_4]))

    # Output weights
    W_out = tf.Variable(weight_initializer([n_neurons_4, 1]))
    bias_out = tf.Variable(bias_initializer([1]))

    # Building hidden layers, using relu activation function
    hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
    hidden_2 = tf.nn.relu(
        tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
    hidden_3 = tf.nn.relu(
        tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))
    hidden_4 = tf.nn.relu(
        tf.add(tf.matmul(hidden_3, W_hidden_4), bias_hidden_4))


    # Output layer (transpose!)-find info
    out = tf.transpose(tf.add(tf.matmul(hidden_4, W_out), bias_out))

    # Cost function - MSE, standard in NN
    mse = tf.reduce_mean(tf.squared_difference(out, Y))

    # Optimizer
    # stock learning rate = .001
    opt = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(mse)

    # Init
    net.run(tf.global_variables_initializer())

    # In[26]:
    # Setup plot
    plt.ion()
    fig = plt.figure()
    ax1 = fig.add_subplot(311)  # 311 means "3x1" grid, 1st subplot
    # take out dates_test for normalized data printing for both line 1 and line 2
    line1, = ax1.plot(dates_test, y_test)
    # results what we predict the output to be (.5 so that the graph starts lower then heightens as it starts to match the test data)
    line2, = ax1.plot(dates_test, y_test * 0.5)

    mse_length = epochs*((len(y_train) // batch_size // graph_updates) + 1)

    print("Length expected: ", mse_length)
    # create a list of zeros for the plot to append to for the graphing
    mse_plot_train = np.zeros(mse_length)
    mse_plot_test = np.zeros(mse_length)
    ax2 = fig.add_subplot(312)  # 312 means "3x1" grid, 2nd subplot
    ax2.set_ylim(0, 1000)  # range of plot(y)
    line3, = ax2.plot(mse_plot_test)
    line4, = ax2.plot(mse_plot_train)
    ax3 = fig.add_subplot(313)  # 313 means "2x1" grid, 3nd subplot
    ax3.set_ylim(-100, 100)  # range of plot(y)
    line5, = ax3.plot(dates_test, y_test)
    line6, = ax3.plot(dates_test, np.zeros(y_test.shape[0]))

    plt.show()

