import streamlit as st


# 1. 사용자에게 보여지는 부분 구현
#  - Title
st.title("그림 그리는 AI화가 서비스")
#  - 이미지 표시
st.image("images/robot_painter.jpg", caption="robot_painter.jpg")
#  - 설명 Text
st.caption("Tell me the picture you want, I'll draw it for you !")
st.caption("원하는 이미지의 설명을 영어로 적어보세요.")
#  - 설명area: 영어로 그림그리기 설명 프롬프트 입력
text = st.text_area("")
#  - 버튼: 그림을 요청하기 > gpt한테
st.button("Painting")


#  2. 버튼 클릭하면, 사용자 이벤트
#  - gpt api key를 로딩하고, OPENAI 객체 생성
#  - 객체변수 클라이언트 생성하고 객체 변수를 통해서 그림을 그려달라고 요청
#    -모델, 프롬프트(system, user: textarea -> value)
#  - gpt로부터 받은 이미지를 화면에 출력



