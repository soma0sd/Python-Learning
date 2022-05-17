# Sphinx를 이용한 문서화

[스핑크스(Sphinx)](https://www.sphinx-doc.org/en/master/index.html)는 파이썬 등으로 작성한 소스코드의 설명서를 온라인 문서(HTML), PDF 문서(LaTeX), E북(ePub) 등으로 만들 수 있게 만들어주는 파이썬 패키지입니다.

## 패키지 설치

```bash
pip install -U sphinx
pip install m2r2 sphinx-reload
```

## 시작하기

설치 후 소스로 사용할 디렉토리에 다음 명령을 실행하면 기본 파일 구조를 생성합니다.

```bash
sphinx-quickstart
```

명령 후 초기화에 필요한 몇 가지 질문이 있습니다.

```
> Separate source and build directories (y/n) [n]: 
```

`y`는 `source`와 `build`디렉토리로 내용을 분리하고, `n`은 소스 디렉토리가 없이 루트 디렉토리를 소스로 취급합니다.

```
> Project name:
> Author name(s):
```

프로젝트의 이름과 작성자를 입력합니다.

```
> Project release 
```

프로젝트의 버전(예: `1.0.8`)을 입력합니다.

```
> Project language [en]:
```

문서의 언어를 변경합니다. 지원하는 언어의 명칭과 종류는 [스핑크스 지원 언어 문서](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language)에 소개되어 있습니다.

모든 과정을 마쳤으면 다음 명령을 통해 웹페이지를 빌드합니다.

```bash
make html
```

빌드한 내용은 `_build/html` 혹은 `build/html`에 위치합니다. [sphinx-reload](#sphinx-reload)도구를 사용하여 빌드과정을 자동화 할 수 있습니다.

## 기본 파일 시스템

- `_static/`혹은 `source/_static/`: 웹페이지에 포함할 자바스크립트, 스타일시트, 이미지를 포함합니다.
- `_templates/`혹은 `source/_templates/`: 확장한 html형식으로 작성한 템플릿 조각입니다.
- `conf.py` 혹은 `source/conf.py`: 스핑크스 설정 파일입니다.
- `make.bat`과 `Makefile`: `make (html|dirhtml...)` 명령으로 간단하게 `sphinx-build`를 수행할 수 있게 해줍니다. 각각 윈도우용과 리눅스용 파일입니다.
- `index.rst`: 전체 문서의 진입점이 되는 문서 파일입니다.

`*.rst`는 reStructuredText라는 마크업 문서 작성 언어입니다. 스핑크스에서 소개하는 [reST 문법 문서](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)를 통해 익힐 수 있습니다.


## 확장과 도구

### 확장: m2r2

[m2r2](https://github.com/crossnox/m2r2) 패키지는 마크다운 문서를 rst 문서에 끼워넣을 수 있도록 하는 스핑크스의 확장 패키지입니다.

**마크다운을 포함한 rst 문서 내용:**

```rst
.. mdinclude:: index.md
   :start-line: 2
   :end-line: -2
```

포함할 파일을 `mdinclude` 명령으로 지정하고, `start-line`과 `end-line`속성으로 마크다운 문서의 일부만 가져올 수 있습니다.

`conf.py`의 `extensions`에 `'m2r2'`를 추가하여 사용할 수 있습니다.

### 확장: githubpages

[githubpages](sphinx.ext.githubpages)는 스핑크스에 기본적으로 포함되어 있는 확장입니다. 빌드할 때 `.nojekll`파일을 생성하고 `baseurl`를 설정합니다.

`conf.py`의 `extensions`에 `'sphinx.ext.githubpages'`를 추가하여 사용할 수 있습니다.

```python
extensions = [
    'sphinx.ext.githubpages',
    ...
]

html_baseurl='https://soma0sd.github.io/Python-Learning/'
```

### 도구: sphinx-reload

[sphinx-reload](https://github.com/prkumar/sphinx-reload)는 문서를 웹에 올리기 전에 미리 문서의 모습을 편리하게 확인할 수 있도록 하는 도구입니다. 웹 브라우저를 통해 빌드한 파일을 볼 수 있고 소스파일을 감시하다가 변경사항이 발생하면 자동으로 빌드를 실행하고 웹브라우저를 새로고칩니다.

```bash
sphinx-reload [--build-dir 빌드디렉토리] 소스디렉토리 [--watch 감시패턴 [PATTERN ...]]
```

현재 저장소의 경우(루트에서 실행):

```bash
sphinx-reload --build-dir $(pwd)/docs/ Sphinx/ --watch $(pwd)/**/*.md $(pwd)/**/*.rst $(pwd)/Sphinx/conf.py
```
