import numpy
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dataFile = open("./D8192.txt", "r")
train_data = []
for line in dataFile:
    xxy = []
    for element in line.split():
        xxy.append(float(element))
    train_data.append(xxy)
    xxy = []
dataFile.close()

dataFile = open("./D1808.txt", "r")
test_data = []
for line in dataFile:
    xxy = []
    for element in line.split():
        xxy.append(float(element))
    test_data.append(xxy)
    xxy = []
dataFile.close()

x_train = train_data[:, :-1]
y_train = train_data[:, -1]
x_test = test_data[:, :-1]
y_test = test_data[:, -1]

clf = DecisionTreeClassifier(criterion='entropy', splitter='best')
clf.fit(x_train, y_train)

n = clf.tree_.node_count
y_pred = clf.predict(x_test)

err = 1 - accuracy_score(y_test, y_pred)

print("Number of nodes: " + str(n))
print("Error: " + str(err))