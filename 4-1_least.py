import numpy as np

x = np.array([2, 4, 6, 8])      #공부한 시간
y = np.array([81, 93, 91, 97])  # 점수

mx = np.mean(x)     # 공부한시간 평균
my = np.mean(y)     # 점수 평균

print("x평균 : ", mx)   
print("y평균 : ", my)

# 기울기 구하는 공식의 분모 구하는 공식
divisor = sum([(i - mx)**2 for i in x])      # (x - x평균)**2의 합

# 기울기 구하는 공식의 분자 구하는 공식 함수
def top(x, mx, y, my):      #(x - x평균)(y - y평균)의 합
    d =0
    for i in range(len(x)):
        d+= (x[i] - mx) * (y[i]- my)
    return d

dividend = top(x, mx, y, my)

print("분모 : ", divisor)
print("분자 : ", dividend)

a = dividend / divisor      # 기울기 구하기

b = my - (mx*a)     # y절편 구하기

print("기울기 a = ", a)
print("y 절편 b = ", b)