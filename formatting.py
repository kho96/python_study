# formatting.py

# format 함수가 %s, %d 보다 이해하기가 쉽다..
a = "I eat {0} apples".format(3)
print(a)

b = "I eat {0} apples".format("five")
print(b)

number = 3
c = "I eat {0} apples".format(number)
print(c)

# 한개가 아닌 여러개의 값(데이터) 넣기
number = 10
day = "three"
d = ".....{0}....{1}".format(number,day)
print(d)

# 인덱스 대신 이름으로 넣는 방법 format(name=value)
e = "....{number}...{day}...".format(number=3, day="two")
print(e)

# 자릿수에 따른 정렬 (%10s)
f = "..{0:>10}..".format("hi") #전체 10자리를 잡아서 출력함(오른쪽 정렬 >)
print(f)
g = "..{0:<10}..".format("hi") #전체 10자리를 잡아서 출력(왼쪽 정렬 <)
print(g)
h = "..{0:^10}".format("hi") #가운데 정렬
print(h)

# 공백채우기
i = "...{0:=^10}...".format("hi")
print(i)
j = "...{0:!<10}...".format("hi")
print(j)

number = 3.141592
k = "...{0:0.4f}...".format(number) #소숫점이하 자릿수
print(k)
l = "...{0:10.4f}...".format(number)  #전체 10자리, 소숫점 이하 4자리
print(l)

# {, } 문자 표현
m = "...{{0}}".format("hi") # {{}}  문자로 인식함
print(m)

# f 문자열 포매팅 (3.6버전 이상)
name = "홍길동"
age = 30
n = f"나의 이름은 {name}입니다. 나이는 {age}살입니다."
print(n)

# f 문자열 포매팅에서 수식 표현
o = f"내년이면 {age+1}살이 됩니다."
print(o)

# 딕셔너리에서의 f 문자열.. 딕셔너리 = java에서 Map이라고 생각하자...(key, value)
p = {"name":"홍길동", "age":30} # 딕셔너리..(JS에서 JSON과 유사함)
q = f"나의 이름은 {p['name']}이고, 나이는 {p['age']}살입니다."
print(q)