#function01.py

# 함수 - 기능을 선언(정의) - 실행을 의미하지 않음
# define(선언하다, 정의하다)
# def 함수명():   -- js의 function 함수명() {} 과 유사한 형태
# 함수 정의하는 쪽에서는 arguments, 실행하는 쪽에서는 parameter... 하지만 둘다 파라미터라고 많이들 사용한다..

# 함수 정의(선언)
def add(a, b):
    print("a" + str(a))
    print("b" + str(b))
    return a + b

# 함수 실행(호출)
c = add(1, 2)
print(c)

# 매개변수의 이름을 지정해서 사용하는 방식, 장점 : 매개변수의 전달순서를 지키지 않아도 된다..!!
d = add(b = 3, a = 4)
print(d)

# 함수의 이름만 정해 놓고 작업은 나중에 하고 싶은 경우 -> pass 사용
def sub(a, b):
    pass

# 파라미터(매개변수) 갯수가 정해지지 않은 경우 (java:...)
# 파이썬 - 파라미터 이름 앞에 *을 사용함.

print("=" * 20)

def add_many(*a):
    print(a)
    sum = 0
    for num in a:
        sum += num
    return sum 
print(add_many(1))   
print(add_many(1,2))   
print(add_many(1,2,3))    

# 매개변수로 문자열, 숫자가 아닌 list, set, dictanry등 다양하게 사용가능함.
def test(a):
    return len(a)
print(test([2,3,4,5,6]))



def add_or_mul(choice, *args):
    print(choice)
    print(args)
    if choice == "add":
        result = 0
        for arg in args:
            result += arg
        return result
    elif choice == "mul":
        result = 1
        for arg in args:
            result *= arg
        return result
    
print(add_or_mul("add", 4,5,6))    
print(add_or_mul("mul", 4,5,6))  

# 키워드 매개변수 kwargs  
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a':1}
print_kwargs(a=1, b=2) # {'a':1, 'b':2}

# 함수의 리턴 값은 1개..

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) #(7, 12)
print(type(result)) # tuple

result_add, result_mul = add_and_mul(3,4)
print(result_add)
print(result_mul)

# return 값은 1개.. 
def add_and_div(a, b):
    return a+b
    return a/b # error

# 매개변수 초기값 설정
def say_myself(name, age, man=True):
    print("이름: %s" %name)
    print("나이: %d" %age)
    if man:
        print("남자")
    else:
        print("여자")
        
say_myself("홍길동", 20, True) 
say_myself("강감찬", 30)  # 매겨변수 초기값이 설정 된 경우, 넣지 않으면 default로 설정된 초기값으로 작동
say_myself("유관순", 15, False)      

# 주의사항 - 기본값 설정 매개변수는 제일 마지막에 위치해야함. 
# def say_yourself(name, man=True, age): # 컴파일에서 이미 error 
#       pass

# 변수의 유효 범위
v1 = 1 # 전역변수
def vartest(v1):
    v1 += 1     # 지역변수로 작용.. -> 함수가 종료되면 사라진다(지역변수..)
    print("def: %d" % v1)
vartest(v1) #2
print("out v1: %d" % v1) #1

def vartest2():
    global v1   # 전역변수를 함수 내에서 사용한다. (사용은 가능하지만 권장하지는 않음..)
    v1 += 1

vartest2()
print("out2 v1: %d" % v1) #2

# lambda식 (자바스크립트의 익명함수와 유사)
func2 = lambda a, b: a + b  # 한줄에서는 유리하지만, 권장하는 방식은 아님
print(func2(1,2 )) # 3
    