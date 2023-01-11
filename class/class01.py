# class01.py

# 클래스에 정의된 함수의 첫번째 파라미터는 무조건 self를 지정하게 되어있다.
class Calculator:
    # result = 0 이건 static이다
    # 생성자, self - java에서의 this라고 이해하면 편함.,  def__init__(self)
    def __init__(self):
        self.result = 0 # 필드에 해당함.(객체의 전역변수)
    
    # 메서드
    def add(self, num):
        self.result += num
        return self.result
    
# new 연산자는 없다
calc1 = Calculator()
calc2 = Calculator()
print(calc1.result) #0
print(calc2.result) #0
calc1.add(1)
calc1.add(2)
print(calc1.result) #3 값이 유지가 된다.
calc2.add(3)
calc2.add(4)
print(calc2.result)
