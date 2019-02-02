import numpy as np
import csv


def convert_to_fahrenheit(celsius):
    return (1.8 * celsius + 32)


def read_from_csv(path):
    reader = csv.reader(open(path))
    data = list(reader)
    array = []
    for row in range(len(data)):
        buff = []
        for x in data[row]:
            try:
                buff.append(float(x))
                # print(float(x))
            except:
                buff.append(x)
        # print(buff)
        array.append(buff)
    return np.array(array)


if __name__ == "__main__":
    # data=pd.read_csv("info_day.csv")
    x = read_from_csv("info_day.csv")
    # print(x)
    for i in range(1, len(x)):
        x[i][1] = convert_to_fahrenheit(float(x[i][1]))
    np.savetxt("transformed.csv", x, delimiter=',')
    file.close()
