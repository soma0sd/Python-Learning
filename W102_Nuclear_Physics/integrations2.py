# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:40:13 2016
@author: soma0sd
"""
#from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def func_int(z, L, theta):
  return np.exp(-2*z/(L*np.sin(theta)))

class func_master:
  def __init__(self):
    self.theta_a = np.radians(51.3)  # radian
    self.theta_c = np.radians(28.3)  # radian
    self.T = 1.0  # nm
    self.L = 9.1  # nm

  def set_theta(self, a:float, c:float):
    self.theta_a = np.radians(a)
    self.theta_c = np.radians(c)

  def set_thickness(self, t: float, L: float):
    self.T = t
    self.L = L

  def _get_I(self, ta, tc, tha, thc):
    L = self.L
    val1 = integrate.quad(func_int, 0, ta, args=(L, tha))[0]
    val2 = integrate.quad(func_int, 0, tc, args=(L, thc))[0]
    val3 = np.exp(2*np.radians(ta)/(L*np.sin(np.radians(thc))))
    return val1/(val2*val3)

  def figure1(self, count=50):
    tha = self.theta_a
    thc = self.theta_c
    plt.xlabel(r'$t_c \mathrm{[nm]}$', size=15)
    plt.ylabel(r'$I_a/I_c$', size=15)
    plt.ylim(0, 60)
    plt.text(0.05, 50,
             '$T_{\mathrm{Fix}}=$'+str(self.T)+' $\mathrm{nm}$',
             horizontalalignment='left',
             verticalalignment='bottom',
             fontsize=20)
    ta = np.linspace(0, self.T, count)
    x = ta
    y = []
    for t1 in ta:
      val = self._get_I(t1, self.T-t1, tha, thc)
      y.append(val)
    plt.plot(x, y)
    ax = plt.twiny()
    ax.set_xlabel(r'$t_a \mathrm{[nm]}$', size=15)
    ax.set_xlim(self.T, 0)
    plt.show()

  def figure2(self, count=50):
    tha = self.theta_a
    thc = self.theta_c
    x, y = [], []
    ta = np.linspace(0, self.T, count)
    for t1 in ta:
      if t1 is 0 or t1 is self.T:
        continue
      val = self._get_I(t1, self.T-t1, tha, thc)
      x.append(t1/(self.T-t1))
      y.append(val)
    plt.plot(x, y)
    fit = np.polyfit(x[1:-1], y[1:-1], 1)
    form = 'Fit: $I_{ac}'+'= {:.3f}'.format(fit[1])+'t_{ac}'
    form += '+{:.3f}$'.format( fit[0])
    plt.text(count*0.05, max(y[1:-1])*0.85,
             form,
             horizontalalignment='left',
             verticalalignment='bottom',
             fontsize=20)
    plt.xlabel(r'$t_a / t_c$', size=15)
    plt.ylabel(r'$I_a/I_c$', size=15)
    plt.show()

  def figure3(self, count=50):
    tha = self.theta_a
    thc = self.theta_c
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ta = np.linspace(0, self.T/2, count)
    x = ta[1:-1]
    y = ta[1:-1]
    z = np.zeros((len(x), len(x)))
    for ix in range(len(x)):
      for iy in range(len(x)):
        val = self._get_I(x[iy], y[ix], tha, thc)
        z[ix][iy] = val
    u = ax.plot_surface(x, y, z,
                        rstride=count, cstride=count,
                        linewidth=0, antialiased=True)
    #fig.colorbar(u, shrink=0.5, aspect=3)
    ax.set_xlabel("$t_c$", size=15)
    ax.set_ylabel("$t_a$", size=15)
    ax.set_zlabel("$I_a/I_c$", size=10)
    plt.show()

c = func_master()
c.figure1(100)
c.figure2(20)
c.figure3()