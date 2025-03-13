from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
import base64
from io import BytesIO
from PIL import Image

load_dotenv(override=True)

# Open AI API 키 설정
openai_key = os.getenv('OPENAI_API_KEY')

# OpenAI 클라이언트 생성
client = OpenAI(api_key=openai_key)

def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # PNG 형식으로 변환
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# 이미지 파일을 분석하여 설명을 반환하는 함수
def ai_describe1(image):
    try:
        base64_image = encode_image(image)  # 이미지를 Base64로 변환
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "이 이미지에 대해서 자세하게 설명해 주세요."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
                    ],
                }
            ],
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"오류 발생: {str(e)}"

def ai_describe2(image_url):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "이 이미지에 대해서 자세하게 설명해 주세요."},
            {"type": "image_url",
                "image_url": {"url": image_url,},
            },
        ],
        }
    ],
    max_tokens=1024,
    )
    result = response.choices[0].message.content
    print("결과 >> ", result)
    return result


st.title("AI 도슨트: 이미지를 설명해드려요!")

tab1, tab2 = st.tabs(["이미지 파일 업로드", "이미지 URL 입력"])

with tab1:
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 업로드된 이미지 표시
        st.image(uploaded_file, width=300)
        
        # 이미지 설명 요청 버튼
        if st.button("해설1"):
            image = Image.open(uploaded_file)  # PIL 이미지 열기
            
            # GPT-4V를 이용한 이미지 분석 수행
            result = ai_describe1(image)
            st.success(result)




with tab2:
    input_url = st.text_area("여기에 이미지 주소를 입력하세요", height=70)

# st.button()을 클릭하는 순간 st.button()의 값은 True가 되면서 if문 실행
    if st.button("해설2"):

        # st.text_area()의 값이 존재하면 input_url의 값이 True가 되면서 if문 실행
        if input_url:
            try:
                # st.image()는 기본적으로 이미지 주소로부터 이미지를 웹 사이트 화면에 생성됨
                st.image(input_url, width=300)
                
                # describe() 함수는 GPT4V의 출력 결과를 반환함
                result = ai_describe2(input_url)

                # st.success()는 텍스트를 웹 사이트 화면에 출력하되, 초록색 배경에 출력
                st.success(result)
            except:
                st.error("요청 오류가 발생했습니다!")
        else:
            st.warning("텍스트를 입력하세요!")