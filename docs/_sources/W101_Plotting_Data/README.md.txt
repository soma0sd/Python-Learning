# 그래프 그리기

## 주어진 데이터로 그리기

`matplotlib`는 너무 복잡한 모듈과 설정을 가지고 있어서 수업에는 쉽고 단순한 인터페이스를 제공하는 `pyplot`모듈을 이용합니다.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [3, 1, 4]
plt.plot(x, y)
plt.show()
```

![그래프](./plotting_1.png)

위 예제를 실행하면 새로운 창에 그림과 같은 그래프를 포시합니다. 아나콘다(Anaconda)의 스파이더(Spyder) 편집기를 사용하거나 구글 코랩(colab) 등 주피터 노트북(Jupyter notebook)기반의 편집기에서 실행하는 경우 결과 표시 창에 그래프를 출력합니다.

[matplotlib](https://matplotlib.org/)의 예제(Example)과 튜토리얼(Tutorials) 문서들을 통해 다양한 그림을 작성하는 방법을 배울 수 있습니다.

