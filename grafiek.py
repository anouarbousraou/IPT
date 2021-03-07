import matplotlib.pyplot as plt
import csv
import matplotlib.patches as mpatches
import numpy as np



y = []
x = []

with open ("export_ipt.csv", "r") as data:

    reader = csv.DictReader(data)

    for row in reader:
        x.append(float(row.get("x")))
        y.append(float(row.get("y")))

with plt.style.context('seaborn-darkgrid'):
    ax = plt.subplot()
    legenda = mpatches.Patch(color='b', label='Portfolio of Gold fund & ETF on the MSCI ChinaIndex')
    plt.legend(handles=[legenda])
    ret_plt = ax.scatter(x, y, color='b')

    plt.plot(x,y,color='k')
    ax.set_ylim(ymin=0, ymax=15)
    ax.set_xlim(xmin=0, xmax=25)
  
    plt.xlabel("Standard Deviation in %")
    plt.ylabel("Return in %")

plt.savefig("test.png")