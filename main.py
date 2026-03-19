import streamlit as st

st.set_page_config(page_title="MBTI 나라 추천", page_icon="🌍")

st.title("🌍 MBTI로 알아보는 추천 나라 ✈️")
st.write("당신의 MBTI에 어울리는 나라 + 상세 정보까지 확인해보세요! 🎒")

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
"capital":"베를린",
"population":"약 8,300만 명",
"food":"소시지, 슈니첼",
"fact":"유럽 최대 경제 대국, 체계적인 사회",
"flag":"https://flagcdn.com/w320/de.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/4/4f/Brandenburg_Gate_Berlin.jpg"
},

"INTP":{
"name":"🇫🇮 핀란드",
"capital":"헬싱키",
"population":"약 550만 명",
"food":"연어 요리, 루이스레빵",
"fact":"세계 최고 수준 교육, 행복지수 높음",
"flag":"https://flagcdn.com/w320/fi.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/6/6e/Helsinki_Cathedral.jpg"
},

"ENTJ":{
"name":"🇺🇸 미국",
"capital":"워싱턴 D.C.",
"population":"약 3억 3천만 명",
"food":"햄버거, 스테이크",
"fact":"세계 최대 경제 대국",
"flag":"https://flagcdn.com/w320/us.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/a/a1/Statue_of_Liberty_7.jpg"
},

"ENTP":{
"name":"🇬🇧 영국",
"capital":"런던",
"population":"약 6,700만 명",
"food":"피쉬 앤 칩스",
"fact":"산업혁명의 시작 국가",
"flag":"https://flagcdn.com/w320/gb.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/c/cd/Big_Ben_2012.jpg"
},

"INFJ":{
"name":"🇨🇦 캐나다",
"capital":"오타와",
"population":"약 3,900만 명",
"food":"푸틴",
"fact":"넓은 자연과 높은 삶의 질",
"flag":"https://flagcdn.com/w320/ca.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/a/a5/Niagara_Falls_2.jpg"
},

"INFP":{
"name":"🇳🇿 뉴질랜드",
"capital":"웰링턴",
"population":"약 500만 명",
"food":"양고기 요리",
"fact":"자연경관이 매우 아름다움",
"flag":"https://flagcdn.com/w320/nz.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/3/3e/Milford_Sound.jpg"
},

"ENFJ":{
"name":"🇰🇷 한국",
"capital":"서울",
"population":"약 5,100만 명",
"food":"김치, 비빔밥",
"fact":"빠른 성장과 IT 강국",
"flag":"https://flagcdn.com/w320/kr.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/6/6e/Gyeongbokgung.jpg"
},

"ENFP":{
"name":"🇪🇸 스페인",
"capital":"마드리드",
"population":"약 4,700만 명",
"food":"파에야",
"fact":"열정적인 문화와 축제",
"flag":"https://flagcdn.com/w320/es.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/9/9a/Sagrada_Familia_01.jpg"
},

"ISTJ":{
"name":"🇯🇵 일본",
"capital":"도쿄",
"population":"약 1억 2,500만 명",
"food":"스시, 라멘",
"fact":"질서와 기술 강국",
"flag":"https://flagcdn.com/w320/jp.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/1/12/Mount_Fuji_from_Hotel_Mt_Fuji_1997-10-20.jpg"
},

"ISFJ":{
"name":"🇨🇭 스위스",
"capital":"베른",
"population":"약 870만 명",
"food":"치즈 퐁듀",
"fact":"중립국, 높은 삶의 질",
"flag":"https://flagcdn.com/w320/ch.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Matterhorn_from_Domh%C3%BCtte_-_2.jpg"
},

"ESTJ":{
"name":"🇸🇬 싱가포르",
"capital":"싱가포르",
"population":"약 590만 명",
"food":"칠리크랩",
"fact":"아시아 금융 중심지",
"flag":"https://flagcdn.com/w320/sg.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/a/a4/Marina_Bay_Sands_in_the_evening_-_20101120.jpg"
},

"ESFJ":{
"name":"🇮🇹 이탈리아",
"capital":"로마",
"population":"약 5,900만 명",
"food":"피자, 파스타",
"fact":"예술과 문화의 중심",
"flag":"https://flagcdn.com/w320/it.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/d/de/Colosseo_2020.jpg"
},

"ISTP":{
"name":"🇦🇺 호주",
"capital":"캔버라",
"population":"약 2,600만 명",
"food":"바비큐",
"fact":"자연과 액티비티 천국",
"flag":"https://flagcdn.com/w320/au.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/4/40/Sydney_Opera_House_Sails.jpg"
},

"ISFP":{
"name":"🇫🇷 프랑스",
"capital":"파리",
"population":"약 6,500만 명",
"food":"크루아상, 와인",
"fact":"예술과 낭만의 나라",
"flag":"https://flagcdn.com/w320/fr.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg"
},

"ESTP":{
"name":"🇧🇷 브라질",
"capital":"브라질리아",
"population":"약 2억 1천만 명",
"food":"슈하스코",
"fact":"열정적인 축구 문화",
"flag":"https://flagcdn.com/w320/br.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/9/97/Cristo_Redentor_-_Rio.jpg"
},

"ESFP":{
"name":"🇹🇭 태국",
"capital":"방콕",
"population":"약 7천만 명",
"food":"팟타이",
"fact":"관광과 음식 문화 발달",
"flag":"https://flagcdn.com/w320/th.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/a/a1/Wat_Phra_Kaew.jpg"
}

}

if st.button("✈️ 나라 추천 받기"):

    c = countries[mbti]

    st.balloons()

    st.subheader(f"🎉 추천 나라: {c['name']}")

    st.image(c["flag"], width=150, caption="국기 🚩")

    st.write(f"🏙 수도: {c['capital']}")
    st.write(f"👥 인구: {c['population']}")
    st.write(f"🍽 대표 음식: {c['food']}")
    st.write(f"⭐ 특징: {c['fact']}")

    st.image(c["place"], caption="📍 대표 명소")

st.divider()
st.caption("💡 MBTI 성향 기반으로 재미있게 만든 나라 추천 앱입니다!")
