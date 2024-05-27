import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = 3
b = 76

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

def predict(x):
    return a*x + b

predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간 = %.f, 실제 점수 = %.f, 예측점수 = %.f" % (x[i], y[i], predict(x[i])))

n = len(x)
def mse(y, y_pred):
    return (1/n) * sum((y - y_pred)**2)

print("평균 제곱 오차" + str(mse(y, predict_result)))