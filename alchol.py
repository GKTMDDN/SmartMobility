import streamlit as st
from PIL import Image

st.write("# 나의 칵테일 레시피 저장소") #글씨 크게 출력

# 목차 : 데킬라럼,리큐르전통주,보드카,브랜디진,위스키
add_selectbox = st.sidebar.selectbox(
    "목차",
    ("데킬라&럼", "리큐르&전통주", "보드카","브랜디&진","위스키")
)


if(add_selectbox == "데킬라&럼"): #데킬라 럼 선택시
    if st.button('다이커리'): #버튼생성
        st.image(Image.open('다이커리.jpg'),caption = '다이커리') #이미지 출력 및 캡션 생성
    if st.button('데킬라선라이즈'): #버튼생성
        st.image(Image.open('데킬라선라이즈.jpg'),caption = '데킬라선라이즈') #이미지 출력 및 캡션 생성
    if st.button('마가리타'): #버튼생성
        st.image(Image.open('마가리타.jpg'),caption = '마가리타') #이미지 출력 및 캡션 생성
    if st.button('마이타이1'): #버튼생성
        st.image(Image.open('마이타이1.jpg'),caption = '마이타이1') #이미지 출력 및 캡션 생성
    if st.button('마이타이2'): #버튼생성
        st.image(Image.open('마이타이2.jpg'),caption = '마이타이2') #이미지 출력 및 캡션 생성
    if st.button('바카디'): #버튼생성
        st.image(Image.open('바카디.jpg'),caption = '바카디') #이미지 출력 및 캡션 생성
    if st.button('블루하와이안'): #버튼생성
        st.image(Image.open('블루하와이안.jpg'),caption = '블루하와이안') #이미지 출력 및 캡션 생성
    if st.button('쿠바리브레'): #버튼생성
        st.image(Image.open('쿠바리브레.jpg'),caption = '쿠바리브레') #이미지 출력 및 캡션 생성
    if st.button('피나콜라다'): #버튼생성
        st.image(Image.open('피나콜라다.jpg'),caption = '피나콜라다') #이미지 출력 및 캡션 생성
elif(add_selectbox == "리큐르&전통주"): #리큐르 전통주 선택시
    if st.button('고창'): #버튼생성
        st.image(Image.open('고창.jpg'),caption = '고창') #이미지 출력 및 캡션 생성
    if st.button('그래스하퍼'): #버튼생성
        st.image(Image.open('그래스하퍼.jpg'),caption = '그래스하퍼') #이미지 출력 및 캡션 생성
    if st.button('금산'): #버튼생성
        st.image(Image.open('금산.jpg'),caption = '금산') #이미지 출력 및 캡션 생성
    if st.button('비오십이'): #버튼생성
        st.image(Image.open('비오십이.jpg'),caption = '비오십이') #이미지 출력 및 캡션 생성
    if st.button('슬로진피즈'): #버튼생성
        st.image(Image.open('슬로진피즈.jpg'),caption = '슬로진피즈') #이미지 출력 및 캡션 생성
    if st.button('준벅'): #버튼생성
        st.image(Image.open('준벅.jpg'),caption = '준벅') #이미지 출력 및 캡션 생성
    if st.button('진도'): #버튼생성
        st.image(Image.open('진도.jpg'),caption = '진도') #이미지 출력 및 캡션 생성
    if st.button('키르'): #버튼생성
        st.image(Image.open('키르.jpg'),caption = '키르') #이미지 출력 및 캡션 생성
    if st.button('푸스카페'): #버튼생성
        st.image(Image.open('푸스카페.jpg'),caption = '푸스카페') #이미지 출력 및 캡션 생성
    if st.button('풋사랑'): #버튼생성
        st.image(Image.open('풋사랑.jpg'),caption = '풋사랑') #이미지 출력 및 캡션 생성
    if st.button('힐링'): #버튼생성
        st.image(Image.open('힐링.jpg'),caption = '힐링') #이미지 출력 및 캡션 생성
elif(add_selectbox == "보드카"): #보드카 선택시
    if st.button('모스코뮬'): #버튼생성
        st.image(Image.open('모스코뮬.jpg'),caption = '모스코뮬') #이미지 출력 및 캡션 생성
    if st.button('블랙러시안'): #버튼생성
        st.image(Image.open('블랙러시안.jpg'),caption = '블랙러시안') #이미지 출력 및 캡션 생성
    if st.button('블러디메리'): #버튼생성
        st.image(Image.open('블러디메리.jpg'),caption = '블러디메리') #이미지 출력 및 캡션 생성
    if st.button('시브리즈'): #버튼생성
        st.image(Image.open('시브리즈.jpg'),caption = '시브리즈') #이미지 출력 및 캡션 생성
    if st.button('애플마티니'): #버튼생성
        st.image(Image.open('애플마티니.jpg'),caption = '애플마티니') #이미지 출력 및 캡션 생성
    if st.button('코스모폴리탄'): #버튼생성
        st.image(Image.open('코스모폴리탄.jpg'),caption = '코스모폴리탄') #이미지 출력 및 캡션 생성
    if st.button('키스오브화이어'): #버튼생성
        st.image(Image.open('키스오브화이어.jpg'),caption = '키스오브화이어') #이미지 출력 및 캡션 생성
    if st.button('하베이웰뱅거'): #버튼생성
        st.image(Image.open('하베이웰뱅거.jpg'),caption = '하베이웰뱅거') #이미지 출력 및 캡션 생성
elif (add_selectbox == "브랜디&진"): #브랜디 진 선택시
    if st.button('네그로니'): #버튼생성
        st.image(Image.open('네그로니.jpg'),caption = '네그로니') #이미지 출력 및 캡션 생성
    if st.button('드라이마티니'): #버튼생성
        st.image(Image.open('드라이마티니.jpg'),caption = '드라이마티니') #이미지 출력 및 캡션 생성
    if st.button('롱아일랜드아이스티1'): #버튼생성
        st.image(Image.open('롱아일랜드아이스티1.jpg'),caption = '롱아일랜드아이스티1') #이미지 출력 및 캡션 생성
    if st.button('롱아일랜드아이스티2'): #버튼생성
        st.image(Image.open('롱아일랜드아이스티2.jpg'),caption = '롱아일랜드아이스티2') #이미지 출력 및 캡션 생성
    if st.button('브랜디알렉산더'): #버튼생성
        st.image(Image.open('브랜디알렉산더.jpg'),caption = '브랜디알렉산더') #이미지 출력 및 캡션 생성
    if st.button('사이드카'): #버튼생성
        st.image(Image.open('사이드카.jpg'),caption = '사이드카') #이미지 출력 및 캡션 생성
    if st.button('싱가폴슬링'): #버튼생성
        st.image(Image.open('싱가폴슬링.jpg'),caption = '싱가폴슬링') #이미지 출력 및 캡션 생성
    if st.button('에프리콧'): #버튼생성
        st.image(Image.open('에프리콧.jpg'),caption = '에프리콧') #이미지 출력 및 캡션 생성
    if st.button('허니문'): #버튼생성
        st.image(Image.open('허니문.jpg'),caption = '허니문') #이미지 출력 및 캡션 생성
elif(add_selectbox == "위스키"): #위스키 선택시
    if st.button('뉴욕'): #버튼생성
        st.image(Image.open('뉴욕.jpg'),caption = '뉴욕') #이미지 출력 및 캡션 생성
    if st.button('러스티네일'): #버튼생성
        st.image(Image.open('러스티네일.jpg'),caption = '러스티네일') #이미지 출력 및 캡션 생성
    if st.button('맨하탄'): #버튼생성
        st.image(Image.open('맨하탄.jpg'),caption = '맨하탄') #이미지 출력 및 캡션 생성
    if st.button('올드패션드'): #버튼생성
        st.image(Image.open('올드패션드.jpg'),caption = '올드패션드') #이미지 출력 및 캡션 생성
    if st.button('위스키사워'): #버튼생성
        st.image(Image.open('위스키사워.jpg'),caption = '위스키사워') #이미지 출력 및 캡션 생성