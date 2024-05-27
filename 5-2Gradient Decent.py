import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# 데이터 분포 그래프
plt.scatter(x, y)
plt.show()

# 기울기 와 y절편 값 초기화
a = 0
b = 0

# 학습률
lr = 0.03

# 반복 횟수
epochs = 2001

# x값 갯수 확인
n = len(x)

# 경사하강법 시작
for i in range(epochs):
    y_pred = a*x+b          # 예측값 구하는 식
    error = y - y_pred      # 실제 값과 비교한 오차

    a_diff = (2/n) * sum(-x *(error))       # 오차 함수를 a로 편미분한 값
    b_diff = (2/n) * sum(-(error))          # 오차 함수를 b로 편미분한 값

    # 학습률을 곱해서 기존의들 업데이트
    a = a -lr * a_diff
    b = b - lr * b_diff

    if i % 100 ==0:         # 100번 반복시 a, b 값 출력
        print("epoch=%.f, 기울기 = %.04f, 절편 = %.04f" % (i, a, b))

y_pred = a * x + b      # 최종 a,  b를 대입

# 그래프 그리기
plt.scatter(x, y)
plt.plot(x, y_pred, 'r')
plt.show()