머신러닝 = 기계학습 = ML(==Deep Learning)

ML: 지도, 비지도, 강화
ML Process 4: 
    1. preprocessing
    2. modeling
    3. running
    4. evaluation

ML Algorithm

1. 퍼셉트론(perceptron) -> 뉴런(neuron)
2. 회귀
3. 분류
4. SVM
5. Dtree
6. kmean
7. PCA
8. R-forest -> RF
9. NLP
10. Deep learning -> DL

여기까지가 chap 13입니다.
외워주세요.
마치 지도를 외우듯이...
Tensorflow

---------------

비지니스 로직 - service
processing 하는 파일명
    processing
    modeling
    learning, evaluation
    완성되면 submit(파일로 저장)

# 외부에 있는 파이썬 파일(.py)를 import 해야 속성, 기능을 사용할 수 있다.
# 내부에서는 이것을 인스턴스화(instance) 해야 한다.
# ex) entity = Entity()
# 이 때 소문자 entity는 인스턴스라 하고 객체로 정의한다.
# 대문사 Entity는 클래스
# 라운드 브레이스가 있는 Entity()는 생성자라고 한다.
# 결론..객체지향에서는 속성과 기능을 호출하는 구조로 두가지 방식 있는데
# calc = Calculator() 있다고 하면
# calc는 인스턴스 객체가 되고
# calculator는 클래스 객체(스태틱)라고 한다..
# calc.sum()하면 인스턴스 호출바식 = 다이나믹
# Calculator.sum() 하면 클래스 호출방식 = 스태틱 이라 한다.

from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service() 

데이터 폴더 있으면 지도 학습, 없으면 비지도 학습

----------------------------------

페이로드(컴퓨팅): 전송되는 데이터, 모든 컴퓨터 및 언어 영역에서 사용

this.fname = payload ~> setter 할당연산자(=) 있으면 setter
this.fname 만 있으면  ~> getter 할당연산자(=) 없으면 getter

======================================
# 메타데이터 = 스키마 = feature = variables, property
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# row, 행, 인스턴스, raw 데이터
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C

========================================
0차원 - 스칼라, 변수
1차원 - 벡터, 배열(array)
2차원 - 매트릭스

차원 (dim)

variable x=3 스칼라, 0 차원
array [] = {1, 2, 3} 벡터, 1차원이 되고, array 내부에서 variable은 element가 된다.
matrix [[]] {(1, 2, 3), (4, 5, 6)} 매트릭스, 2차원 dataframe

=============================

지도학습에서 반드시 해야 할 일은 dataset을 생성하는 것이다.
그 때 dataset은 반드시 train, test 두가지 형태로 작성한다. p. 149



