# -*- coding: utf-8 -*-
"""
오일러 방법으로 자유낙하 하는 물체를 근사한다.
"""
import numpy
import matplotlib.pyplot as plt
import ode_tools as tools

# 변수 정의
N = 1000 # 스탭의 수
x0 = 0   # 초기 위치
v0 = 15  # 초기 속도
t  = 3   # 운동 시간

# 변수 초기화
dt = t/float(N-1)  # 시간 간격
time = numpy.linspace(0, t, N)


def FreeFall(state, time):
    """
    자유낙하하는 물체의 미분량을 출력하는 함수
    state는 현재의 (위치 x, 속도 v)가 담겨있는 벡터
    출력은 (현재속도 v, 가속도 g)
    """
    v = state[1]
    g = -9.8
    return numpy.array([v, g])

# 계산한 데이터를 담을 y 생성
y = numpy.zeros([N, 2])
# 데이터에 초기값 입력
y[0, 0] = x0
y[0, 1] = v0

# 오일러 방법을 사용하여 데이터 y를 채운다.
for j in range (N - 1):
    y[j+1] = tools.euler(y[j], time[j], dt, FreeFall)
xdata = [y[j, 0] for j in range(N)]
vdata = [y[j, 1] for j in range(N)]

# matplotlib을 사용하여 그래프 출력
plt.plot(time, xdata, label="position")
plt.plot(time, vdata, label="velocity")
plt.xlabel ("time")
plt.ylabel ("position, velocity")
plt.grid()
plt.legend()
plt.show()


