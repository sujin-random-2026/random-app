import random
import streamlit as st

# 1. 웹페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 2. 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 추천받아 보세요.")

# 3. 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "국밥",
    "햄버거",
    "파스타",
    "비빔밥",
    "칼국수",
    "떡볶이",
    "마라탕",
    "샌드위치",
    "쌀국수",
    "부대찌개",
    "카레라이스",
]

st.divider()

# 4. 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  # 리스트에서 랜덤으로 1개 선택
  selected_menu = random.choice(lunch_menus)

  # 시각적 효과 (풍선 날리기)
  st.balloons()

  # 결과 출력
  st.success(f"오늘의 추천 메뉴는 **'{selected_menu}'** 입니다! 맛있게 드세요! 😋")
