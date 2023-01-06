# while01.py

# while : 반복문

# 열번 찍어 안넘어 가는 나무 없다...
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit) 
    if treeHit == 10:
        print("나무 쓰러짐")
        
print("=" * 20)

# 사용자로 부터 입력값 : input() - 입력값은 글자로 취급
num = input("입력 : ")
print(num)
print(type(num)) # str => 글자 취급
iNum = int(num) # int() - 글자=>숫자 변환
print(iNum)
print(type(iNum)) # int() => 숫자로 변환됨
sNum = str(iNum) # str() => 글자로 변환
print(sNum)
print(type(sNum)) # str => 문자로 변환됨

# 실행중인 반복문 빠져나가기 -> break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d 잔입니다." % coffee)
    if coffee == 0:
        print("커피가 떨어졌습니다. 판매중지")
        break
print("=" * 20)

# 반복의 계속 - 하던 작업을 중단하고 다시 반복한다.
a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
    print(a)