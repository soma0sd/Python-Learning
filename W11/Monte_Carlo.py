# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:29:41 2016
@author: soma0sd

주어진 확률분포함수를 이용해 몬테카를로 시뮬레이션 수행
"""
import numpy as np
from scipy import integrate as scint
from matplotlib import pyplot as plt

"""
가우시안(정규 분포) 함수
클래스에서 사용
"""
def gaussian(x, ratio, mu, sigma):
  sol = -(x-mu)**2/(2*(sigma**2))
  sol = np.exp(sol)
  sol *= 1/(sigma*np.sqrt(np.pi*2))
  return sol*ratio


class montecarlo:
  def __init__(self, channel: int, coeff: list):
    """
    @ channel: 채널 수
    @ coeff: 상수 [[ratio, mu, sigma], ...]
    """
    self.ch = channel
    self.coeff = coeff
    self.x = np.arange(0, self.ch+1, 1)

  def PDF(self, x=None):
    """
    확률밀도함수
    가우시안의 선형결합
    """
    data = 0
    if x is None:
      x = self.x
    for c in self.coeff:
      data += gaussian(x, c[0], c[1]*self.ch, c[2]*self.ch)
    return data

  def CDF(self):
    """
    누적확률밀도함수
    정석은 이것의 역함수를 만들어 랜덤으로 뽑아낸 수치에
    대응하는 값을 출력할 수 있도록 하는 것
    """
    data = []
    ratio = scint.quad(self.PDF, -np.inf, np.inf)[0]
    # [scipy.integrate.quad]는 적분값과 불확실성을 반환한다.
    # [numpy.inf]는 numpy 안에서 무한에 대응하는 심볼을 담고 있다.
    for x in self.x:
      data.append(scint.quad(self.PDF, 0, x))
    return np.array(data)/ratio

  def MC(self, signal: int):
    """
    몬테카를로 시행
    편법을 사용해서 각 채널에 따른 확률을 확률밀도 함수를 통해 부여하고
    그 확률에 따라 채널을 선택하게 한다.
    """
    ratio = np.sum(self.PDF())
    # 확률을 1로 Normalization하기 위해서 보정치를 구한다.
    return np.random.choice(self.x, signal, p=self.PDF()/ratio)
    # [numpy.random.choice]는 원소들 중에서 정해진 갯수를 뽑는 함수
    # p = array()를 이용해서 각 원소가 뽑힐 확률을 조정할 수 있다.
    # 주의: p에 들어가는 집합은 원소의 갯수와 같을 것
    # 주의: p에 들어있는 모든 확률값의 합이 1이 될 것


"""
메인 함수
초기변수 설정
"""
coeff = [[3, 0, 0.1], [1, 0.4, 0.05], [2, 0.6, 0.02]]
mc = montecarlo(100, coeff)

"""
계산값 Plot
"""
# [좌상] 확률밀도
ax = plt.subplot(221)
ax.plot(mc.x, mc.PDF())
ax.set_title('PDF')
# [우상] 누적확률밀도
ax = plt.subplot(222)
ax.plot(mc.x, mc.CDF())
ax.set_title('CDF')
# 몬테카를로 1000회 수행
ax = plt.subplot(223)
ax.hist(mc.MC(1000), bins=100)
ax.set_xlim(0, 100)
ax.set_xlabel('MC 1000')
# 몬테카를로 100000회 수행
ax = plt.subplot(224)
ax.hist(mc.MC(1E5), bins=100)
ax.set_xlim(0, 100)
ax.set_xlabel('MC 1E5')
