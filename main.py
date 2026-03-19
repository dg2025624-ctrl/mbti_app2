import streamlit as st

st.set_page_config(page_title="MBTI 나라 추천", page_icon="🌍")

st.title("🌍 MBTI 나라 추천 ✈️")
st.write("성격에 맞는 나라 + 이유 + 명소까지 확인해보세요! 😎")

mbti = st.selectbox(
    "🧠 MBTI 선택",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

countries = {

"INTJ":{
"name":"🇩🇪 독일",
"capital":"베를린",
"population":"약 8,300만 명",
"food":"소시지, 슈니첼",
"fact":"체계적인 사회 시스템",
"reason":"논리적이고 계획적인 INTJ는 효율적인 독일 문화와 잘 맞아요!",
"flag":"https://flagcdn.com/w320/de.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Brandenburg_Gate_Berlin.jpg/800px-Brandenburg_Gate_Berlin.jpg"
},

"ISTP":{
"name":"🇦🇺 호주",
"capital":"캔버라",
"population":"약 2,600만 명",
"food":"바비큐",
"fact":"자연과 액티비티 천국",
"reason":"자유롭고 활동적인 ISTP는 호주의 야외 라이프와 찰떡!",
"flag":"https://flagcdn.com/w320/au.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Sydney_Opera_House_Sails.jpg/800px-Sydney_Opera_House_Sails.jpg"
},

"ENFP":{
"name":"🇪🇸 스페인",
"capital":"마드리드",
"population":"약 4,700만 명",
"food":"파에야",
"fact":"열정적인 문화",
"reason":"활발한 ENFP는 축제와 자유로운 분위기의 스페인과 잘 맞아요!",
"flag":"https://flagcdn.com/w320/es.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Sagrada_Familia_01.jpg/800px-Sagrada_Familia_01.jpg"
},

"ISTJ":{
"name":"🇯🇵 일본",
"capital":"도쿄",
"population":"약 1억 2,500만 명",
"food":"스시",
"fact":"질서와 규칙",
"reason":"책임감 강한 ISTJ는 체계적인 일본 문화와 잘 맞습니다!",
"flag":"https://flagcdn.com/w320/jp.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Mount_Fuji.jpg/800px-Mount_Fuji.jpg"
}

}

if st.button("✈️ 추천 받기"):

    if mbti not in countries:
        st.warning("⚠️ 현재 일부 MBTI만 예시로 구현되어 있습니다!")
    else:
        c = countries[mbti]

        st.balloons()

        st.subheader(f"🎉 추천 나라: {c['name']}")

        st.image(c["flag"], width=150, caption="국기 🚩")

        st.write(f"🏙 수도: {c['capital']}")
        st.write(f"👥 인구: {c['population']}")
        st.write(f"🍽 음식: {c['food']}")
        st.write(f"⭐ 특징: {c['fact']}")

        st.success(f"💡 추천 이유\n👉 {c['reason']}")

        st.image(c["place"], caption="📍 대표 명소", use_column_width=True)

st.divider()
st.caption("💡 MBTI 기반 재미용 추천입니다!")
