import random
import matplotlib.pyplot

if __name__ == '__main__':
    dataFile = open("./Dbig.txt", "r")
    data = []
    for line in dataFile:
        xxy = line.split()
        data.append(xxy)
    random.shuffle(data)

    training_set_8192 = []
    training_set_2048 = []
    training_set_512 = []
    training_set_128 = []
    training_set_32 = []
    test_set = []

    i = 0
    for item in data:
        if i <= 31:
            training_set_32.append(item)
        if i <= 127:
            training_set_128.append(item)
        if i <= 511:
            training_set_512.append(item)
        if i <= 2047:
            training_set_2048.append(item)
        if i <= 8191:
            training_set_8192.append(item)
        if i > 8191:
            test_set.append(item)
        i = i + 1

    file1 = open('./D32.txt', 'w')
    for item in training_set_32:
        file1.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file1.close()

    file2 = open('./D128.txt', 'w')
    for item in training_set_128:
        file2.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file2.close()

    file3 = open('./D512.txt', 'w')
    for item in training_set_512:
        file3.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file3.close()

    file4 = open('./D2048.txt', 'w')
    for item in training_set_2048:
        file4.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file4.close()

    file5 = open('./D8192.txt', 'w')
    for item in training_set_8192:
        file5.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file5.close()

    file6 = open('./D1808.txt', 'w')
    for item in test_set:
        file6.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")
    file6.close()