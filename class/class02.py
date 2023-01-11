# class02.py

class FourCal:
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first # this.xx = xx  와 같다.
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# calc = FourCal()
# print(type(calc)) # class
# calc1 = FourCal()
# calc2 = FourCal()
# calc1.setdata(3, 4)
# calc2.setdata(5, 6)
# print(calc1)
# print(calc2)
calc3 = FourCal(3,4)
print(calc3.add()) # setdata를 하지 않으면 에러가 생김 -> 생성자에서 파라미터를 받을 수 있게 만들어서 실행한다.
    
# 상속 - ()안에 상속받을 클래스를 넣는다.
class MoreFourCal(FourCal):
    def pow(self):
        # 제곱 ** 
        result = self.first ** self.second
        return result
calc = MoreFourCal(3, 4)
print(calc.add()) # 7
print(calc.pow()) # 81

# 오버라이드
class SafeFourCal(FourCal):
    # FourCal에 정의된 div()를 재정의(오버라이드)
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

calc2 = SafeFourCal(4,0)
# print(calc2.div()) # error.. division by zero (오버라이드 하기전)
print(calc2.div())