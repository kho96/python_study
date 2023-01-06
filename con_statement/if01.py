#if01.py

# 조건문 - 조건에 ()가 없다. {}도 없다. :을 사용, 들여쓰기(강제)

# money = True
money = False
if money:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")
    
print("=" * 10) # 조건문가 관계없이 출력된다.    

# 비교연산자(>,<,==,!=,>=,<=) java와 동일함..
money = 2000
if money >= 2000:
    print("택시를 탄다")
else:
    print("걸어간다.")

print("=" * 10)

# 관계 연산자 (and, or, not) java와는 다르게 기호가 아님.
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 탄다")    
else:
    print("걸어간다.")    
    
print("=" * 10)  

# 원소 유무 판단 - in, not in

pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시를 탈 수 있다.")
else:
    print("걸어간다.")
    
print("=" * 10)          

# 조건에서 코드를 생략하고 싶은 경우 - pass 사용, pass를 사용하지 않고 비워두면 오류
if "money" not in pocket:
    pass
else:
    print("택시를 타라")
    
print("=" * 10)  
    
# elif - else if에 해당함.
pocket = ["paper", "cellphone", "card"]
if "money" in pocket:
    print("택시를 타라")
elif "card" in pocket:
    print("택시를 타세요")
else: print("걸어가") # 실행 문장(코드)이 한줄인 경우 들여쓰기 생략하고 옆에 사용 가능함.

print("=" * 10) 

# 조건부 표현식.... 변수 = 조건문이 참인 경우 값 if 조건문 else 조건문이 거짓인 경우의 값
score = 60
result = "success" if score >= 60 else "failure"
print(result)