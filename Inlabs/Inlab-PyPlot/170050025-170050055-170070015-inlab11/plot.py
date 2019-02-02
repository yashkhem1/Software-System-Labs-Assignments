import matplotlib.pyplot as plt 
import numpy as np
# def line_plot():
x=[1,2,3,5,8,10]
y=[200,300,353,412,456,734]
plt.plot(x,y,color="green",label="Performance")
plt.xlabel("No. of clients")
plt.ylabel("Latency (in ms)")
plt.title("Performance Analysis")
plt.legend(loc=4)

plt.savefig("Performance.png")


labels = 'A', 'B', 'C', 'D', 'E',  'F'
sizes = np.array([50, 100, 28, 56, 230, 80])
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
def absolute_value(val):
    a  = np.int(np.round(val/100.*sizes.sum(), 0)) 
    return a
ax1.pie(sizes, labels=labels, autopct=absolute_value,
        shadow=False, startangle=90)
ax1.axis('equal')
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Data Analysis")
plt.legend(loc=0)
plt.savefig("Data.png")
