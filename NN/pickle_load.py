from matplotlib import pyplot as plt
import pickle
import numpy as np
import pandas as pd

# loading the predictions as well as the actual and plotting those things(that have already been done)


def load_and_plot(n_neurons, n_epochs, learning_rate, future_days, stock_ticker, split):
    file_name = "NN/"+stock_ticker+"/"+str(n_neurons) + "_" + str(n_epochs) + "_" + \
        str(learning_rate) + "_" + str(future_days) + "_" + str(stock_ticker) + "_" + str(split)
    [pred, actual, dates_test] = pickle.load(
        open(file_name + ".p", "rb"))  # loading pickle file that was created from the stock_pred file

    # segments of the graph that you want to see
    beg_time = 0
    end_time = 8000
    dates_test=list(dates_test.values)
    pred = list(pred.flatten()[beg_time:end_time])
    actual = list(actual[beg_time:end_time])
    data = [{
        "date":pd.to_datetime(str(dates_test[i])).strftime("%Y-%m-%d"),
        "prediction":pred[i],
        "actual":actual[i]
    } for i in range(len(dates_test))]
    return data

# # file locational settings (look at purple)
# n_neurons = 256
# n_epochs = 1000
# learning_rate = 0.003
# future_days = 1
# split = 0.8
#
# # stock_ticker = "NASDAQ.AAPL"
# stock_ticker = "DIS"
#
# load_and_plot(n_neurons=n_neurons, n_epochs=n_epochs, learning_rate=learning_rate,
#               future_days=future_days, stock_ticker=stock_ticker, split=split)
