print('주민등록번호 분석기 프로그램입니다.')

resident_number = input('주민번호를 입력하세요: ')

# 생년월일탐색

birth_year = resident_number[0:2]
birth_month = resident_number[2:4]
birth_day = resident_number[4:6]
sex = resident_number[7]
area = resident_number[8:10]
area = int(area)

#성별 비교하기
if sex == '1' or sex == '3':
    sex = '남자'
elif sex == '2' or sex == '4':
    sex = '여자'
else:
    sex = '중성'


#주민번호에서 정보 출력
print(f"생년월일 : {birth_year}년 {birth_month}월 {birth_day}일 ")
print(f"성별 : {sex}")

#지역 비교하기
if 0 <= area <=8:
    print('출생지: 서울특별시')
elif 9 <= area <= 12:
    print('출생지: 부산광역시')
elif 13 <= area <= 15:
    print('출생지: 인천광역시')
elif 16 <= area <= 25:
    print('출생지: 경기도')
elif 26 <= area <= 34:
    print('출생지: 강원도')
elif 35 <= area <= 39:
    print('출생지: 충청북도')
elif area == 40:
    print('출생지: 대전광역시')
elif 41 <= area <= 43:
    print('출생지: 충청남도')
elif area == 44 or area == 96:
    print('출생지: 세종특별자치시')
elif 48 <= area <= 54:
    print('출생지: 전라북도')
elif 55 <= area <= 66:
    print('출생지: 전라남도')
elif area == 55 or area == 56:
    print('출생지: 광주광역시')
elif 67 <= area <= 70:
    print('출생지: 대구광역시')
elif 71 <= area <= 81:
    print('출생지: 경상북도')
elif 82 <= area <= 84 or 86 <= area <= 90:
    print('출생지: 경상남도')
elif area == 85:
    print('출생지: 울산광역시')
elif 91 <= area <= 95:
    print('출생지: 제주특별자치도')
else:
    print('출생지 정보가 없거나 틀렸습니다. 관계당국에 연락하세요.')
