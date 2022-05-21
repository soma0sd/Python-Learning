# 파이썬 시작하기

## 파이썬 설치하기: Windows

[파이썬 재단](https://www.python.org/)의 웹페이지에서 최신 버전의 설치 파일을 내려받는 방법도 있지만 [마이크로소프트 스토어](https://apps.microsoft.com/store/search/python)를 사용하여 설치하는 방법이 좋습니다. 여러 이유가 있지만 너무 많은 패키지를 설치했거나 패키지 사이의 충돌 원인을 알수 없을 경우 앱 설정을 통해 간편하게 초기화 할 수 있기 때문입니다.

설치가 끝나면 시작 버튼에서 마우스 오른쪽 버튼을 눌러 **Windows 터미널**을 실행한 후 설치한 파이썬 버전을 확인합니다.

```ps1
python3 --version
```

## 파이썬 설치하기: Ubuntu

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

## WSL 사용하기

WSL(Windows Subsystem for Linux; 리눅스용 윈도우 하위 시스템)은 윈도우 환경에서 리눅스를 사용할 수 있도록 해주는 편리한 기능입니다. 윈도우를 사용하면서 리눅스 환경의 개발을 익히는데 도움됩니다.

시작 버튼에서 마우스 오른쪽 버튼을 눌러 **Windows 터미널(관리지)**를 실행한 뒤, 다음 명령을 실행합니다.

```ps1
wsl --install
```

환경 구성과 리눅스(기본값은 우분투 20.04)설치까지 자동으로 수행합니다. 설치가 끝난 뒤 PC를 재시작하면 자동으로 터미널이 열리고 여기서 UNIX 유저이름과 비밀번호를 설정합니다.

## 파이썬 가상환경 생성

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

# 비주얼 스튜디오 코드

[비주얼 스튜디오 코드(Visual Studio Code; VSCode)](https://code.visualstudio.com/)는 가볍게 사용할 수 있는 소스코드 편집기입니다. 낮은 사양의 랩톱에서도 원활하게 작업할 수 있으며, 다양한 언어를 지원합니다. 또한 많은 추가기능과 확장 도구를 설치하여 기능을 확장 할 수 있습니다. [다운로드 페이지](https://code.visualstudio.com/#alt-downloads)를 방문하여 설치관리자를 내려받아 설치합니다.

이외에도 [아나콘다(ANACONDA)](https://www.anaconda.com/)나 [파이참(PyCharm)](https://www.jetbrains.com/ko-kr/pycharm/) 등 많은 파이썬 배포판과 통합 개봘환경이 있습니다.

## VSCode: WSL 원격 개발

윈도우에서 리눅스를 사용하는(WSL) 경우, VSCode에 원격 개발 확장을 설치합니다.

- [원격 개발(Remote Development)](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

# 파이썬 자습서

[파이썬 공식문서](https://docs.python.org/ko/3/)는 기여자들의 참여를 통해 대부분 한국어로 번역되어 있습니다. 기초 문법과 개념 등을 이곳에서 살펴볼 수 있습니다.
