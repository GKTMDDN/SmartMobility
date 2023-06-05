import streamlit as st
from PIL import Image

st.write('# Hi! Welcome to My App!')

st.write('반갑습니다. 저의 웹에 오신 것을 환영합니다')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '말', '토끼', '코끼리'))

st.write('내가 좋아하는 동물은',option,'입니다')
st.write(f'좋아하는 동물은 {option} 입니다.')

txt = st.text_area('자신을 소개해보세요', '''
                   
    ''')
st.write('입력한 내용은: ', txt)

age = st.slider('나이를 선택하세요.', 0, 130, 25)
st.write("저의 나이는", age, '입니다.')

st.write('# 체질량 계산기')
st.success('체질량 지수: 몸무게/((키/100)^2)')
height = st.number_input('키를 입력하세요(cm)',100,230,170,5)
st.write('당신의 키는', height, 'cm 입니다.')

weight = st.number_input('몸무게를 입력하세요(kg)',40,150,60,5)
st.write('당신의 몸무게는', weight, '입니다.')

BMI = weight/((height/100)**2)
if st.button('계산'):
    st.write('당신의 BMI 지수는',round(BMI,2),'입니다.')

if st.button('당신의 몸은!'):
    if (BMI<=18.5):
        st.warning('저체중입니다.')
    elif(BMI <=23):
        st.success('정상입니다.')
        st.balloons()
    elif(BMI<=25):
        st.warning('과체중입니다.')
    else:
        st.error('비만입니다.')
        
        


image = Image.open('vegetable.jpg')

st.image(image, caption='vegetable')