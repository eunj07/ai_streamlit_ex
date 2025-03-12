import streamlit as st

hungry = st.slider("배고픔 정도", 0, 130, 25)
st.write("나는 지금 ", hungry, "만큼 배고파")