import matplotlib.pyplot

if __name__ == '__main__':
    # Parse data
    dataFile = open("./D2048.txt", "r")
    x11 = []
    x21 = []
    x10 = []
    x20 = []
    for line in dataFile:
        xxy = line.split()
        print(xxy)
        if float(xxy[2]) == 1:
            x11.append(float(xxy[0]))
            x21.append(float(xxy[1]))
        else:
            x10.append(float(xxy[0]))
            x20.append(float(xxy[1]))

    matplotlib.pyplot.figure()
    matplotlib.pyplot.scatter(x11, x21)
    matplotlib.pyplot.scatter(x10, x20)
    matplotlib.pyplot.xlabel('x1')
    matplotlib.pyplot.ylabel('x2')
    matplotlib.pyplot.title('Dtest Scatter Plot')
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()

