# class03.py

class Family:
    lastname = "김"
    
print(Family.lastname) #김
f1 = Family()
f2 = Family()
print(f1.lastname) #김
print(f2.lastname) #김

print("=" * 20)

f1.lastname = "박" #f1의 객체 변수 lastname을 생성하고 값을 할당
print(Family.lastname) # 김
print(f1.lastname)  # 박
print(f2.lastname) # 김
    