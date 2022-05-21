import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 4, 0.5)    # r의 범위
x = np.linspace(0, 1, 100)  # x의 범위

def logistic(x, r):
    return x*r*(1-x)

plt.rc('font', family='serif')        # 글자체를 셰리프로
plt.xlabel(r"$x_{i}$", fontsize=16)   # x 축 이름 설정
plt.ylabel(r"$x_{i+1}$", fontsize=16) # y축 이름 설정
"""
pyplot.plot의 label 옵션: 지정한 문자열을 그래프 이름으로 한다.
각 그래프 이름은 pyplot.legend()로 표시할 수 있다.
"""
for _r in r:
    plt.plot(x, logistic(x, _r), label="r:{:.1f}".format(_r))
plt.legend()              # 범례 표시
plt.savefig("0414-01-x_vs_x1.png", bbox_inches='tight')  # 그림 파일로 저장
