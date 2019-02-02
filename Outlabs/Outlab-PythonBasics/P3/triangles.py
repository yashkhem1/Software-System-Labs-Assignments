#! python3


def area(x1, y1, x2, y2, x3, y3):
    psum = x1 * y2 + x2 * y3 + x3 * y1
    nsum = x1 * y3 + x3 * y2 + x2 * y1
    diff = psum - nsum
    return 0.5 * abs(diff)


if __name__ == "__main__":
    buff = input("Enter the first coordinate :")
    [x1, y1] = buff.split(" ")
    buff = input("Enter the second coordinate :")
    [x2, y2] = buff.split(" ")
    buff = input("Enter the third coordinate :")
    [x3, y3] = buff.split(" ")
    buff = input("Emter coordinates of the key :")
    [xk, yk] = buff.split(" ")

    areaTotal = area(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
    area1 = area(int(x3), int(y3), int(x2), int(y2), int(xk), int(yk))
    area2 = area(int(x1), int(y1), int(x3), int(y3), int(xk), int(yk))
    area3 = area(int(x2), int(y2), int(x1), int(y1), int(xk), int(yk))

    if areaTotal == area1 + area2 + area3:
        print('INSIDE')
    else:
        print('OUTSIDE')
