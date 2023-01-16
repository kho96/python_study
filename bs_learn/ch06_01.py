# ch06_01.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

with urlopen("http://www.naver.com") as response:
    # print(response.status) #200(HTTP OK, 정상적으로 응답함) - status : 상태 코드
    html = response.read()
    # print(html)
    soup = BeautifulSoup(html, "html.parser") #html 전개 -> html.parser, 위에서 받은 text를 DOM형태로 만들어줌(뷰티풀수프)
    # print(soup.prettify()) # 눈에 보이게 쉽게 하기 위해 prettify()
    # print(soup.div) # 첫번째로 찾은 한개만 나옴
    # print(soup.div["id"]) # 첫번째로 찾은 div의 id 속성의 값을 찾아냄
    # print(soup.div.a.span.string) # text-node 얻어내기..
    
    # all_a = soup.find_all("a") # 모든 a에 대해서 찾아낸다.. -> List로 나옴
    # print(all_a[:2]) # 0번째와 1번째 a를 가져옴..
    # for a in all_a[:2]:
    #     print(a.span.string) # a태그의 span태그르 찾아 text-node를 얻어냄
    
    # 속성으로 찾기..
    elims = soup.find_all(attrs={"class" : "title elss"}) # 클래스 속성의 값이 "title elss"인 것을 찾아냄 
    print(elims) # List형태
    for elim in elims[0:2]:
        print(elim.string) # text만 가져옴
    
    