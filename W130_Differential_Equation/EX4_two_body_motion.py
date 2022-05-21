"""

.. image:: EX4_two_body_motion.png

`EX4_two_body_motion.py <EX4_>`_

.. _EX4: https://github.com/soma0sd/Python-Learning/blob/main/W104_Differential_Equation/EX4_two_body_motion.py

.. literalinclude:: EX4_two_body_motion.py
   :language: python
   :linenos:
   :lines: 15-

"""
import numpy as np
import matplotlib.pyplot as plt

x1, y1   = [-1], [ 0]; m1 = 6   # 입자 1의 초기위치와 질량
x2, y2   = [ 1], [ 2]; m2 = 4   # 입자 2의 초기위치와 질량
vx1, vy1 =  [0.5],  [-0.5]  # 입자 1의 속력
vx2, vy2 =  [-0.5], [0.5]  # 입자 2의 속력

dt = 0.1                # 시간 간격
t  = np.arange(0, 14, dt) # 시간 공간

def force():
    global m1, m2, x1, y1, x2, y2
    """
    두 입자 사이에 미치는 힘
    출력: Fx, Fy
    """
    r2 = (x2[-1]-x1[-1])**2 + (y2[-1]-y1[-1])**2
    Th = np.arctan2(y2[-1]-y1[-1], x2[-1]-x1[-1])
    F  = m1*m2/r2
    Fx = F*np.cos(Th)
    Fy = F*np.sin(Th)
    return Fx, Fy

if __name__ == "__main__":
    """
    벌렛을 사용하여 두 입자의 궤도를 그린다.
    """
    lw = np.linspace(0, 10, len(t)-1)
    for _t in t:
        Fx, Fy = force()
        x1.append(x1[-1] + vx1[-1]*dt + 0.5*Fx*dt*dt/m1)
        y1.append(y1[-1] + vy1[-1]*dt + 0.5*Fy*dt*dt/m1)
        x2.append(x2[-1] + vx2[-1]*dt - 0.5*Fx*dt*dt/m2)
        y2.append(y2[-1] + vy2[-1]*dt - 0.5*Fy*dt*dt/m2)
        nFx, nFy = force()
        vx1.append(vx1[-1] + 0.5*dt*(Fx+nFx)/m1)
        vy1.append(vy1[-1] + 0.5*dt*(Fy+nFy)/m1)
        vx2.append(vx2[-1] - 0.5*dt*(Fx+nFx)/m2)
        vy2.append(vy2[-1] - 0.5*dt*(Fy+nFy)/m2)

    plt.figure(figsize=(5,5))
    for _lw, _x1, _y1, _x2, _y2 in zip(lw,x1,y1,x2,y2):
        plt.plot(_x1, _y1, ".r", ms=_lw)
        plt.plot(_x2, _y2, ".b", ms=_lw)
    plt.savefig("EX4_two_body_motion.png", bbox_inches='tight')
