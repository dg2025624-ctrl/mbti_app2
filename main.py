# mbti_app2
import streamlit as st

st.set_page_config(page_title="MBTI 나라 추천", page_icon="🌍")

st.title("🌍 MBTI로 알아보는 추천 나라 ✈️")
st.write("당신의 MBTI에 어울리는 나라와 국기를 보여드립니다! 🚩")

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
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
"desc":"체계적이고 계획적인 당신에게 딱 맞는 나라!",
"flag":"https://flagcdn.com/w320/de.png"
},

"INTP":{
"name":"🇫🇮 핀란드",
"desc":"조용하고 사색적인 환경을 좋아하는 당신!",
"flag":"https://flagcdn.com/w320/fi.png"
},

"ENTJ":{
"name":"🇺🇸 미국",
"desc":"도전과 성공을 중시하는 리더형!",
"flag":"https://flagcdn.com/w320/us.png"
},

"ENTP":{
"name":"🇬🇧 영국",
"desc":"토론과 아이디어를 즐기는 창의적인 당신!",
"flag":"https://flagcdn.com/w320/gb.png"
},

"INFJ":{
"name":"🇨🇦 캐나다",
"desc":"배려와 조화를 중요시하는 따뜻한 성향!",
"flag":"https://flagcdn.com/w320/ca.png"
},

"INFP":{
"name":"🇳🇿 뉴질랜드",
"desc":"자연과 감성을 사랑하는 당신!",
"flag":"https://flagcdn.com/w320/nz.png"
},

"ENFJ":{
"name":"🇰🇷 한국",
"desc":"사람과 관계 중심의 따뜻한 리더!",
"flag":"https://flagcdn.com/w320/kr.png"
},

"ENFP":{
"name":"🇪🇸 스페인",
"desc":"열정과 자유를 사랑하는 당신!",
"flag":"https://flagcdn.com/w320/es.png"
},

"ISTJ":{
"name":"🇯🇵 일본",
"desc":"질서와 책임감을 중요시하는 성향!",
"flag":"https://flagcdn.com/w320/jp.png"
},

"ISFJ":{
"name":"🇨🇭 스위스",
"desc":"안정과 평화를 중시하는 당신!",
"flag":"https://flagcdn.com/w320/ch.png"
},

"ESTJ":{
"name":"🇸🇬 싱가포르",
"desc":"효율과 규칙을 중시하는 리더!",
"flag":"https://flagcdn.com/w320/sg.png"
},

"ESFJ":{
"name":"🇮🇹 이탈리아",
"desc":"사람들과 어울리는 걸 좋아하는 당신!",
"flag":"https://flagcdn.com/w320/it.png"
},

"ISTP":{
"name":"🇦🇺 호주",
"desc":"자유롭고 활동적인 라이프스타일!",
"flag":"https://flagcdn.com/w320/au.png"
},

"ISFP":{
"name":"🇫🇷 프랑스",
"desc":"감성과 예술을 사랑하는 당신!",
"flag":"https://flagcdn.com/w320/fr.png"
},

"ESTP":{
"name":"🇧🇷 브라질",
"desc":"에너지 넘치고 도전적인 성향!",
"flag":"https://flagcdn.com/w320/br.png"
},

"ESFP":{
"name":"🇹🇭 태국",
"desc":"즐거움과 현재를 중시하는 당신!",
"flag":"https://flagcdn.com/w320/th.png"
}

}

if st.button("✈️ 나라 추천 받기"):
    country = countries[mbti]

    st.balloons()

    st.subheader(f"🎉 추천 나라: {country['name']}")
    st.write(country["desc"])

    st.image(country["flag"], width=200, caption="국기 🚩")

st.divider()
st.caption("💡 MBTI 성향을 기반으로 재미있게 매칭한 나라 추천입니다!")
