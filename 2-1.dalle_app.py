import base64
import io
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(override=True)
from PIL import Image

#  - gpt api key를 로딩하고, OPENAI 객체 생성
openai_key = os.environ.get("OPENAI_API_KEY")

#  - 객체변수 클라이언트 생성하고 객체 변수를 통해서 그림을 그려달라고 요청
client = OpenAI(
    api_key = openai_key
)

#  openai key 값 프린트 해보기
#    -모델, 프롬프트(system, user: textarea -> value)

# 실제 이미지 값을 json으로 return으로 받음
def get_image(input_text):
    res = client.images.generate(
            model = "dall-e-3",
            prompt = input_text,
            size = "1024x1024",
            quality = "standard",
            response_format='b64_json',
            n = 1)

    res = res.data[0].b64_json # DALLE로부터 Base64 형태의 이미지를 얻음.
    image_data = base64.b64decode(res) # Base64로 쓰여진 데이터를 이미지 형태로 변환
    image = Image.open(io.BytesIO(image_data)) # '파일처럼' 만들어진 이미지 데이터를 컴퓨터에서 볼 수 있도록 Open
    return image
    # 함수가 실행되고 그냥 끝나버리기 때문에 return을 해줘서 url값을 나중에 사용하게 함

# 1. 사용자에게 보여지는 부분 구현
#  - Title
st.title("그림 그리는 AI 화가 서비스")
#  - 이미지 표시
st.image("images/robot_painter.jpg", width= 300)
#  - 설명 Text
st.caption("Tell me the picture you want, I'll draw it for you !")
st.caption("원하는 이미지의 설명을 영어로 적어보세요.")
#  - 설명area: 영어로 그림그리기 설명 프롬프트 입력
input_text = st.text_area("그림 설명을 넣어주세요",height=200)
#  - 버튼: 그림을 요청하기 > gpt한테
#  2. 버튼 클릭하면, 사용자 이벤트
if st.button("Painting"):
    # textarea에 입력한 내용이 있는지 체크(text)
    if input_text:
        # 있다면
        # openai에 그림을 그려달라는 메시지를 보내
        # ---------------------------------------------------------
        image = get_image(input_text)
        st.image(image, width=300)
        # ---------------------------------------------------------
    else:
        # 없다면
        # 글 입력 요청글을 보내
        st.write("텍스트 박스에 그림을 그릴 설명을 영어로 넣으세요")
#  - gpt로부터 받은 이미지를 화면에 출력











