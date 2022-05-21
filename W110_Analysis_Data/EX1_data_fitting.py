"""

온라인을 통해 나사의 연평균기온 데이터를 내려받고 해당 값에
다항식 피팅을 사용하여 근사합니다.

얻은 다항식 계수를 통해 지구 연평균 기온의 추세를 추정하거나
이후 값을 예측하는데 활용할 수 있습니다.

.. image:: EX1_data_fitting.png

예제는 1차 다항식과 9차 다항식을 사용했습니다.
주제와 상황에 따라 적당한 다항식 근사를 사용하는 방법도 고민해봅시다.

`EX1_data_fitting.py <EX1_>`_

.. _EX1: https://github.com/soma0sd/Python-Learning/blob/main/W110_Analysis_Data/EX1_data_fitting.py

.. literalinclude:: EX1_data_fitting.py
   :language: python
   :linenos:
   :lines: 24-

"""
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    """
    NASA로부터 1880년부터 2019년까지 월별 평균 기온 정보를 받아옵니다.
    이 함수는 웹 문서를 읽어오는 패키지인 requests를 사용하며
    csv는 쉼표와 줄바꿈문자를 이용해서 데이터를 구분하는 형식입니다.
    """
    import requests
    url = 'http://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.csv'
    data = str(requests.get(url).content)
    data = data.split('\\n')
    # \n은 줄바꿈문자. 온라인에서 정보를 받아와서 각 줄별로 리스트를 생성한다
    data = [row.split(',') for row in data]
    # 각 줄마다 쉼표로 분리해서 2차원 리스트를 만든다
    return (data[2:])[:-2]  # 데이터가 아닌 부분은 슬라이싱


if __name__ == "__main__":
    data = get_data()
    years = [int(row[0]) for row in data]
    tempr = [float(row[13]) for row in data]

    # 다항식 fitting - 1차
    fitsp = np.linspace(years[0], years[-1], 100)
    fit1 = np.poly1d(np.polyfit(years, tempr, 1))

    # 다항식 fitting - 9차
    fit9 = np.poly1d(np.polyfit(years, tempr, 9))

    # PLOT
    plt.figure(figsize=[5, 3])
    raw, = plt.plot(years, tempr, ':g')
    p1, = plt.plot(fitsp, fit1(fitsp), "--r")
    p9, = plt.plot(fitsp, fit9(fitsp), "--k")
    plt.legend([raw, p1, p9], ['rawdata', 'fit1', 'fit9'], bbox_to_anchor=(1, 0.4))

    # 만들어진 그래프 보기
    plt.show()

    # 만든 그래프 저장
    # plt.savefig("EX1_data_fitting.png")
