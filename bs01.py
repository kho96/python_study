# bs01.py

# 문서 - https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
# 설치 - pip install beautifulsoup4 - 데이터 처리
# 설치 - pip install requests - 요청

from bs4 import BeautifulSoup

# 요청하고 응답 받은 데이터라고 가정
html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
'''
# 특징 - css 셀렉트 방식 사용
soup = BeautifulSoup(html_doc)
# print(soup.prettify()) # 문서를 보기 좋은 형태 출력(들여쓰기)
# print("=" * 50)
# print(soup.title) # <title>The Dormouse's story</title>, title의 전체부분
# print(soup.title.name) # 태그명: title, .name - 태그명
# print(soup.title.string) # The Dormouse's story, .string - text값
# print(soup.title.parent.name) # head, .parent - 부모, .parent.name - 부모의 태그
# print(soup.p) # 전체 p 중에서 첫번째 p
# print(soup.p["class"]) # ['title'], p의 클래스
# print(soup.a) # 전체 a 중에서 첫번째 a
# print(soup.find_all("a")) # 모든 a를 찾아서 리스트 형태로 출력 []
# for e in soup.find_all("a"):
#     print(e)

# print(soup.find(id="link3"))

# 링크 페이지 얻어오기
# a_list = soup.find_all("a")
# for a in a_list:
#     href = a.get("href") # a["href"], href값만 받아내기
#     print(href)

# 텍스트 노드(문자열)만 얻어오기
# print(soup.get_text()) # 태그는 보이지 않고 모든 문자열 출력

# index.html 읽기
# python의 경우 file읽기를 할 때, encoding이 깨짐 --> encoding="utf-8"로 설정하면 깨지지 않음.(쓰기도 동일)
# with open("index.html", "r", encoding="utf-8") as f: 
#     html_doc = f.read()
#     soup = BeautifulSoup(html_doc)
#     print(soup.title)
    
# 요청 데이터 읽기
import requests

rData = requests.get("http://www.naver.com")
# print("=" * 30)
# print(rData) # <Response [200]> 200: 정상처리 되었다.(가공되지 않음..)
# print(rData.text) # 위에서 받은 rData를 사람이 볼 수 있게 만드는 것이 .text
soup = BeautifulSoup(rData.text)
print(soup.head) # <title>NAVER</title>
