# 파이썬 시작하기

## 파이썬 설치하기

### 윈도우 10/11

[파이썬 재단](https://www.python.org/)의 웹페이지에서 최신 버전의 설치 파일을 내려받는 방법도 있지만 [마이크로소프트 스토어](https://apps.microsoft.com/store/search/python)를 사용하여 설치하는 방법이 좋습니다. 여러 이유가 있지만 너무 많은 패키지를 설치했거나 패키지 사이의 충돌 원인을 알수 없을 경우 앱 설정을 통해 간편하게 초기화 할 수 있기 때문입니다.

### 리눅스: 우분투 및 데비안

터미널에서 다음 명령을 실행합니다.

```bash
# 패키지 목록 업데이트
sudo apt update
# 선택
sudo apt upgrade
# 파이썬과 가상환경 생성 패키지 설치
sudo apt-get install python3 python3-venv
```

설치 후 버전 확인을 통해 설치한 파이썬을 확인합니다.

```bash
python3 --version
```

## 파이썬 가상환경

```bash
python3 -m venv {생성할 가상환경 이름}
```

```bash
python3 -m venv .pyenv
```

현재 디렉토리 아래 `.pyenv`라는 이름으로 가상환경 디렉토리가 생성됩니다. 이제 만든 가상환경을 활성화합니다.

**윈도우(파워쉘):**

```ps1
./.pyenv/bin/Activate.ps1
```

**리눅스(Bash):**

```bash
source .pyenv/bin/Activate.ps1
```

성공적으로 활성화 된 경우, 만든 가상환경 이름이 프롬프트의 제일 앞에 등장하게 됩니다.