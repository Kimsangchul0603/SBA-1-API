class Calculator: # 생성자 함수, 객체 만드는 함수. 언더스코어 2개는 접근제한 의미
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def gob(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    calc = Calculator(6, 2) # num1 = 6, num2 = 2
    sumResult = calc.sum()
    minusResult = calc.minus()
    gobResult = calc.gob()
    divideResult = calc.divide()
    print('덧셈결과 : ', sumResult)
    print('뺄셈결과 : ', minusResult)
    print('곱셈결과 : ', gobResult)
    print('나눗셈결과 : ', divideResult)

    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3

    # 결론: 객체지향은 속성이 존재해야 한다. 속성을 정의하는 것은 __init__(속성)이다.