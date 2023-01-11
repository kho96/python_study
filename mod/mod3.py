# mod3.py

# mod1.py로 부터 add함수 가져오기
# from mod1 import add, sub #mod1.add-> add로 사용하겠다.
from mod1 import * # mod1의 함수들을 다 가져오겠다.
print(add(4,4)) # 8
print(sub(3,5)) # -2

print(__name__) # __main__
# -> 실행파일