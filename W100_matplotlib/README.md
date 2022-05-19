# matplotlib 시작하기

## 그래프 패키지 설치하기

[matplotlib](https://matplotlib.org/)은 파이썬을 위한 시각화 도구입니다. 각종 그래프와 그림, 다이얼로그등을 다루는 것을 목적으로 합니다. 추가로 설치하는 [NumPy](https://numpy.org/)와 [SciPy](https://scipy.org/)는 수치해석, 통계, 과학 등을 위한 각종 함수와 데이터형을 제공합니다.

여기서는 파이썬으로 그래프를 그리는데 필요한 패키지를 설치하고 패키지가 제대로 설치되었는지 확인하도록 합니다.

앞으로의 실습에 필요한 `matplotlib`과 `numpy`, `scipy`를 설치합니다. 구글 코랩(Google Colab)이나 아나콘다(Anaconda)를 사용하는 경우, 이 패키지들은 미리 설치되어 있으니 굳이 설치할 필요가 없습니다.

PIP 설치 및 업그레이드

```bash
python3 -m pip install --upgrade matplotlib numpy scipy
```

아나콘다(Anaconda) 설치 및 업그레이드: 보통은 기본으로 설치되어 있습니다.

```bash
conda install --upgrade matplotlib numpy scipy
```

리눅스 설치

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-matplotlib python3-numpy python3-scipy
```

[NumPy](https://numpy.org/)는 수치해석 및 행렬연산을 위한 다양한 도구와 새로운 자료형 등을 제공합니다. [NumPy 설명서](https://numpy.org/doc/stable/)를 통해서 상세한 기능들을 살펴볼 수 있습니다. [SciPy](https://scipy.org/)는 과학을 위한 특수함수 및 통계 등을 제공합니다. [SciPy 설명서](https://docs.scipy.org/doc/scipy/reference/)를 통해서 상세한 설명을 살펴볼 수 있습니다.


## 그래프 작성 패키지: matplotlib

## 수학 기능 확장 도구: numpy

## 과학용 함수 및 도구: scipy
