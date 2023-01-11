# mod7.py

# import mod6
# print(mod6.add(1,2)) # 현재 경로에 있는 파일 기준

import sys
print(sys.path) # ['경로1', ...] 리스트 형태로 저장되어 있다. sys에 mod6이없다.

# sys.path.append("G:/workspace/python/mymod")
# print(sys.path)

# 윈도우 검색창 -> 환경(시스템 환경변수) -> 환경변수 버튼 -> 시스템변수 PYTHONEPATH 에서 추가하고 싶은 경로 추가..
# -> mymod.mod6 할 필요 없이 자동으로 파일명만 기입하면 된다..

import mod6
print(mod6.add(1, 2)) # 3
print(mod6.sub(1, 2)) # -1

