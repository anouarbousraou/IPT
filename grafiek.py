import matplotlib.pyplot as plt
import csv


y = []
x = []

with open ("Book5.csv", "r") as data:

    reader = csv.DictReader(data)

    for row in reader:
        x.append(float(row.get("x")))
        y.append(float(row.get("y")))


ax = plt.subplot()
ax.set_title("Opportunity Set")
ret_plt = ax.scatter(x, y)
plt.plot(x,y)
plt.xlabel("Standard Deviation in %")
plt.ylabel("Return in %")

plt.savefig("test.png")