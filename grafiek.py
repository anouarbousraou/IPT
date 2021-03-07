import matplotlib.pyplot as plt
import csv
import matplotlib.patches as mpatches


y = []
x = []

with open ("export_ipt.csv", "r") as data:

    reader = csv.DictReader(data)

    for row in reader:
        x.append(float(row.get("x")))
        y.append(float(row.get("y")))


ax = plt.subplot()
legenda = mpatches.Patch(color='r', label='Portfolio of Gold fund & ETF on the MSCI ChinaIndex')
plt.legend(handles=[legenda])
ret_plt = ax.scatter(x, y, color='r')
plt.plot(x,y,color='b')
plt.xlabel("Standard Deviation in %")
plt.ylabel("Return in %")

plt.savefig("test.png")