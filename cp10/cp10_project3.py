books = [
    {'제목': '개발자의 코드', '출판 연도': '2013.02.28', '출판사': 'A', '쪽수': 200, '추천유무': False},
    {'제목': '클린 코드', '출판 연도': '2013.03.04', '출판사': 'B', '쪽수': 584, '추천유무': True},
    {'제목': '빅데이터 마케팅', '출판 연도': '2014.07.02', '출판사': 'A', '쪽수': 296, '추천유무': True},
    {'제목': '구글드', '출판 연도': '2010.02.10', '출판사': 'B', '쪽수': 526, '추천유무': False},
    {'제목': '강의력', '출판 연도': '2013.12.12', '출판사': 'A', '쪽수': 248, '추천유무': True}
]
print("전체 책 목록")
for i in books:
    print(i)

many_page = [i['제목'] for i in books if i['쪽수'] > 250]
recommends = [i['제목'] for i in books if i['추천유무']]
all_pages = sum(i['쪽수'] for i in books)
pub_company = set(i['출판사'] for i in books)
print(f"\n쪽수가 250쪽 넘는책 리스트 : {many_page}")
print(f"내가 추천하는 책 리스트 : {recommends}")
print(f"내가 읽은 책 전체 쪽수 : {all_pages}")
print(f"내가 읽은 책의 출판사 목록 : {pub_company}")
