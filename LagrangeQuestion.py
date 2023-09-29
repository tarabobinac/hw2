import numpy
import math
from scipy.interpolate import lagrange
from sklearn.metrics import mean_squared_error

numpy.random.seed(0)
a = 0
b = 2 * numpy.pi

x_train = numpy.sort(numpy.random.uniform(a, b, 100))
x_test = numpy.sort(numpy.random.uniform(a, b, 100))
y_test = numpy.sin(x_test)

noise = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]

for value in noise:
    y_train = numpy.sin(x_train + value)
    lagrange_interp = lagrange(x_train + value, y_train)

    train_predictions = lagrange_interp(x_train + value)
    test_predictions = lagrange_interp(x_test)

    train_mse = mean_squared_error(y_train, train_predictions)
    test_mse = mean_squared_error(y_test, test_predictions)

    print("MSE Training, epsilon of " + str(value) + ": " + str(math.log(train_mse, 2)))
    print("MSE Test, epsilon of " + str(value) + ": " + str(math.log(test_mse, 2)))