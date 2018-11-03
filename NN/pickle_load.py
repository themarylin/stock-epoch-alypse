from matplotlib import pyplot as plt
import pickle
import numpy as np

# loading the predictions as well as the actual and plotting those things(that have already been done)


def load_and_plot(n_neurons, n_epochs, learning_rate, future_days, stock_ticker):
    file_name = str(n_neurons) + "_" + str(n_epochs) + "_" + \
        str(learning_rate) + "_" + str(future_days) + "_" + str(stock_ticker)
    [pred, actual, dates_test] = pickle.load(
        open(file_name + ".p", "rb"))  # loading pickle file that was created from the stock_pred file
    print(pred.shape)
    print(type(pred.flatten()))
    print(type(dates_test))
    # segments of the graph that you want to see
    # beg_time = 0
    # end_time = 8000

    dates_test = range(0, pred.flatten()[beg_time:end_time].shape[0])

    print(dates_test)
    # plt.plot(dates_test[beg_time:end_time],
    #         pred.flatten()[beg_time:end_time], 'r')
    # plt.plot(dates_test[beg_time:end_time], actual[beg_time:end_time], 'b')

    plt.plot(dates_test,  pred.flatten()[beg_time:end_time], 'r')
    plt.plot(dates_test, actual[beg_time:end_time], 'b')
    # plt.plot(x, y)
    plt.show()


# file locational settings (look at purple)
n_neurons = 256
n_epochs = 1000
learning_rate = 0.003
future_days = 1
#
# stock_ticker = "NASDAQ.AAPL"
stock_ticker = "NYSE.DIS"

load_and_plot(n_neurons=n_neurons, n_epochs=n_epochs, learning_rate=learning_rate,
              future_days=future_days, stock_ticker=stock_ticker)
