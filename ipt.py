import math
import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt

def get_gold_return():
    """
    Gets return for gold
    """

    gold_returns = []

    with open ("gold.csv", "r") as gold_data:

        gold_reader = csv.DictReader(gold_data)

        for row in gold_reader:
            gold_returns.append(float(row.get("Chg"))*100)

    return gold_returns

def calc_gold_mean():
    """
    Calculates the mean for gold returns
    """

    n = len(get_gold_return())

    mean = sum(get_gold_return()) / n

    return mean

def calc_gold_var():
    """
    Calculates the variance for gold returns
    """
    
    gold_variance = statistics.variance(get_gold_return())
    gold_stddev = math.sqrt(gold_variance)

    return gold_variance


def get_china_return():
    """
    Calculates the returns for China
    """

    china_returns = []

    with open ("china.csv", "r") as china_data:

        china_reader = csv.DictReader(china_data)

        for row in china_reader:
            china_returns.append(float(row.get("Chg"))*100)

    return china_returns

def calc_china_mean():
    """
    Calculates the mean for china returns
    """

    n = len(get_china_return())

    mean = sum(get_china_return()) / n

    return mean

def calc_china_var():
    """
    Calculates the variance for china returns
    """

    china_variance = statistics.variance(get_china_return())
    china_stddev = math.sqrt(china_variance)

    return china_variance

def calc_covar():
    """
    Calculates the covariance for Gold and China
    """
    cov = np.cov(get_china_return(), get_gold_return())
    return cov

# creates empty list for returns
y = []

# weight for gold and china
y_gold_w = 1
y_china_w = 0

# runs while gold weight is positive
while y_gold_w >= 0:

    # calculates the mean
    curr_mean = (calc_gold_mean() * y_gold_w) + (calc_china_mean() * y_china_w)
    
    # adds mean to list
    y.append(curr_mean)

    # changes weight, substracts 10% from gold and adds 10% to china
    y_gold_w -= 0.1
    y_china_w += 0.1

# creates empty list for standard deviation
x = []

# weight for gold and china
x_gold_w = 1
x_china_w = 0

# runs while gold weight is positive
while x_gold_w >= 0:

    # calculates standard deviation
    curr_stddev = math.sqrt((((x_gold_w ** 2) * calc_gold_var()) + ((x_china_w ** 2) * calc_china_var())) + 2 * x_gold_w * x_china_w * (calc_covar()[0][1]))
    
    # adds standard deviation to list
    x.append(curr_stddev)

    # changes weight, substracts 10% from gold and adds 10% to china
    x_gold_w -= 0.1
    x_china_w += 0.1


# plots the oppportunity set
ax = plt.subplot()
ret_plt = ax.scatter(x, y)
plt.plot(x,y)
plt.xlabel("Standard Deviation in %")
plt.ylabel("Return in %")

plt.savefig("plot.png")