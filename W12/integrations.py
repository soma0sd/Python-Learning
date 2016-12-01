# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:32:08 2016
@author: soma0sd
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

"""
전역 함수
func_int: 적분안의 공통함수 [exp(-2 z / L sin(Theta_c))]
func_master: I_a/I_c 계산 클래스
"""
def func_int(z, L, theta):
  return np.exp(-2*z/(L*np.sin(theta)))


class func_master:
  def __init__(self):
    self.theta_a = None
    self.theta_c = None
    self.t_a = None
    self.t_c = None
    self.L = None

  def _f_get_theta(self, low, high, count):
    if high is None:
      return np.array([np.radians(low)])
    else:
      low, high = np.radians(low), np.radians(high)
      return np.linspace(low, high, count)

  def _f_get_value(self, low, high, count):
    if high is None:
      return np.array([low])
    else:
      return np.linspace(low, high, count)

  def set_theta_a(self, low, high=None, count=50):
    self.theta_a = self._f_get_theta(low, high, count)

  def set_theta_c(self, low, high=None, count=50):
    self.theta_c = self._f_get_theta(low, high, count)

  def set_t_a(self, low, high=None, count=50):
    self.t_a = self._f_get_value(low, high, count)

  def set_t_c(self, low, high=None, count=50):
    self.t_c = self._f_get_value(low, high, count)

  def set_L(self, low, high=None, count=50):
    self.L = self._f_get_value(low, high, count)

  def plot2D(self):
    L = self.L
    t_a = self.t_a
    t_c = self.t_c
    th_a = self.theta_a
    th_c = self.theta_c
    for t1 in t_a:
      I = []
      val1 = integrate.quad(func_int, 0, t1, args=(L, th_a))[0]
      print(val1)
      val3 = np.exp(2*np.radians(t1)/(L*np.sin(np.radians(th_c))))
      for t2 in t_c:
        val2 = integrate.quad(func_int, 0, t2, args=(L, th_c))[0]
        I.append(val1/(val2*val3))
      plt.plot(t_c, I)


d = func_master()
d.set_L(9.1)
d.set_t_a(0.1, 0.9, 1)
d.set_t_c(0.9, 0.1, 100)
d.set_theta_a(51.3)
d.set_theta_c(28.3)
