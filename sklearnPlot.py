import matplotlib.pyplot

if __name__ == '__main__':
    n = [32, 128, 512, 2048, 8192]
    err_n = [0.1742, 0.0852, 0.0387, 0.0387, 0.0138]
    #err_n = [0.0985, 0.0835, 0.0277, 0.0221, 0.0133]
    matplotlib.pyplot.figure(figsize=(8, 6))
    matplotlib.pyplot.plot(n, err_n, color='black')
    matplotlib.pyplot.xlabel('n')
    matplotlib.pyplot.ylabel('err_n')
    matplotlib.pyplot.title('own alg err_n')
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show()