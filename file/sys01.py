# sys01.py

import sys #sys 모듈을 사용하려면 import해야함

args = sys.argv[1:]
print(args)

for arg in args:
    print(arg)