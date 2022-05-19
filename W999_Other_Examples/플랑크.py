import requests
import matplotlib as mpl
import numpy as np

h = 6.626e-34  # 플랑크 상수
c = 3.0e+8  # 광속
k = 1.38e-23  # 볼츠만 상수

wave_len_min = 1E-9
wave_len_max = 1E-5

wave = np.arange(wave_len_min, wave_len_max, wave_len_min)


def planck(T):
    global wave, h, c, k
    term_sub = h*c/(wave*k*T)
    term1 = 2.0*h*(c**2)/(wave**5)
    term2 = 1/(np.e**term_sub - 1)
    inten = term1*term2
    return inten


def plot(T, color):
    global wave, pot
    data = planck(T)
    pot.plot(wave*1E9, data, c=color, label=T)


def gen_color(lenth):
    gap = int(255/lenth)
    greens = [hex(i).replace("0x", "") for i in range(0, 255, gap)]
    colors = ["#FF{}00".format(i.upper()) for i in greens]
    return colors

imgurl = requests.get("https://github.com/soma0sd/python-study/raw/master/demos/img01.png")
with open("img.png", "wb") as f:
    f.write(imgurl.content)
img = mpl.image.imread('img.png')
plt = mpl.pyplot
fig = plt.figure()
fig.figimage(img, resize=True)
pot = fig.add_subplot(111)
pot.patch.set_alpha(0.5)

#plt.semilogy()
#plt.semilogx()

colors = gen_color(15)
for i in range(100, 1500, 100):
    plot(i, colors[int(i/100)])


plt.title("Planck's law", fontsize=15)
plt.xlabel("Wave Lenth [nm]", fontsize=12)
plt.ylabel("intensity", fontsize=12)
plt.legend()
