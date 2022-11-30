# Python-Calculator

## 설명

파이썬의 GUI 라이브러리인 PyQt5를 이용하여 구현한 __윈도우용 계산기__

## 사용한 모듈

PyQt5 module

## Installation Require

```python
python --version 
3.8.10

pip3 install pyqt5
```

## 사용 방법

윈도우 계산기와 사용방법은 거의 유사하다. 

### 이항 연산자
`+`, `-` , `*`, `/`, `%` 로 이루어져있으며 연산을 위한 두가지 피연산자가 존재해야 동작한다. 

__입력__
<img width = "500px" src = "https://user-images.githubusercontent.com/78203399/204743269-625c4ee9-fc7d-4a4d-b2cf-4981ec5a4958.PNG" />

__결과__
<img width = "500px" src = "https://user-images.githubusercontent.com/78203399/204743843-1956ad67-211a-4c89-ac9b-12b9e4a6878e.PNG">

### 단항 연산자
`1/x`, `x²`, `√`로 이루어져있으며 입력값(피연산자) 하나에게만 적용되는 연산자입니다. 

__입력__
<img width = "500px" src = "https://user-images.githubusercontent.com/78203399/204745951-2abe0b81-d52c-45ce-be67-cabc91cdcac3.PNG">

__결과__
<img width = "500px" src = "https://user-images.githubusercontent.com/78203399/204746528-13733062-9c10-45e9-9aa8-b28eb5964cb2.PNG">

### 그 외 (CE, C)
값을 초기화 해주는 버튼입니다. 