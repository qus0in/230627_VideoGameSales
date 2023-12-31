import streamlit as st
import common

common.page_config()

st.title("Video Game Sales")
st.caption("""
"Video Game Sales" (비디오 게임 판매 데이터):
이 데이터셋은 전 세계적으로 발매된 비디오 게임의 판매 정보를 담고 있습니다.
게임 플랫폼, 장르, 출시 연도 등을 기반으로 다양한 시각화를 통해
비디오 게임 시장 동향과 인기 게임을 분석할 수 있습니다.
""")
st.image("img/welcome.png")

