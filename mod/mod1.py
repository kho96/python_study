# mod1.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# main인 경우(mod1.py에서만)에만 실행, 
# 이걸 안하면 import한 경우 다 실행됨
if __name__ == "__main__": 
    print("mod1:" + str(add(1,2))) 
    print("mod1:" + str(add(3,4))) 
