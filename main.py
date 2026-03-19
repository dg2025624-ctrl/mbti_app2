import streamlit as st

st.set_page_config(page_title="MBTI 나라 추천", page_icon="🌍")

st.title("🌍 MBTI 나라 추천 ✈️")
st.write("당신의 성격에 맞는 나라와 명소를 확인해보세요! 😎")

mbti = st.selectbox(
    "🧠 MBTI 선택",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

def show_image(url):
    try:
        st.image(url, use_column_width=True)
    except:
        st.image("https://via.placeholder.com/800x500.png?text=Image+Not+Available")

countries = {

"INTJ":{"name":"🇩🇪 독일","capital":"베를린","population":"8300만","food":"소시지","fact":"체계적인 사회",
"reason":"논리적이고 전략적인 성향이 독일과 잘 맞음",
"place_name":"브란덴부르크 문",
"flag":"https://flagcdn.com/w320/de.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Brandenburg_Gate_Berlin.jpg/800px-Brandenburg_Gate_Berlin.jpg"},

"INTP":{"name":"🇫🇮 핀란드","capital":"헬싱키","population":"550만","food":"연어","fact":"교육 강국",
"reason":"조용하고 깊이 있는 사고를 선호",
"place_name":"헬싱키 대성당",
"flag":"https://flagcdn.com/w320/fi.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Helsinki_Cathedral.jpg/800px-Helsinki_Cathedral.jpg"},

"ENTJ":{"name":"🇺🇸 미국","capital":"워싱턴 D.C.","population":"3.3억","food":"햄버거","fact":"경제 대국",
"reason":"목표 지향적이고 리더형",
"place_name":"자유의 여신상",
"flag":"https://flagcdn.com/w320/us.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Statue_of_Liberty_7.jpg/800px-Statue_of_Liberty_7.jpg"},

"ENTP":{"name":"🇬🇧 영국","capital":"런던","population":"6700만","food":"피쉬앤칩스","fact":"토론 문화",
"reason":"아이디어와 토론을 즐김",
"place_name":"빅벤",
"flag":"https://flagcdn.com/w320/gb.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Big_Ben_2012.jpg/800px-Big_Ben_2012.jpg"},

"INFJ":{"name":"🇨🇦 캐나다","capital":"오타와","population":"3900만","food":"푸틴","fact":"자연 풍부",
"reason":"타인을 배려하는 성향",
"place_name":"나이아가라 폭포",
"flag":"https://flagcdn.com/w320/ca.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Niagara_Falls_2.jpg/800px-Niagara_Falls_2.jpg"},

"INFP":{"name":"🇳🇿 뉴질랜드","capital":"웰링턴","population":"500만","food":"양고기","fact":"자연 아름다움",
"reason":"감성적이고 자연을 사랑",
"place_name":"밀포드 사운드",
"flag":"https://flagcdn.com/w320/nz.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Milford_Sound.jpg/800px-Milford_Sound.jpg"},

"ENFJ":{"name":"🇰🇷 한국","capital":"서울","population":"5100만","food":"김치","fact":"IT 강국",
"reason":"사람 중심의 리더형",
"place_name":"경복궁",
"flag":"https://flagcdn.com/w320/kr.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Gyeongbokgung.jpg/800px-Gyeongbokgung.jpg"},

"ENFP":{"name":"🇪🇸 스페인","capital":"마드리드","population":"4700만","food":"파에야","fact":"열정 문화",
"reason":"자유롭고 활발한 성격",
"place_name":"사그라다 파밀리아",
"flag":"https://flagcdn.com/w320/es.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Sagrada_Familia_01.jpg/800px-Sagrada_Familia_01.jpg"},

"ISTJ":{"name":"🇯🇵 일본","capital":"도쿄","population":"1.25억","food":"스시","fact":"질서 사회",
"reason":"책임감과 규칙 중시",
"place_name":"후지산",
"flag":"https://flagcdn.com/w320/jp.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Mount_Fuji.jpg/800px-Mount_Fuji.jpg"},

"ISFJ":{"name":"🇨🇭 스위스","capital":"베른","population":"870만","food":"치즈","fact":"평화 국가",
"reason":"안정과 조화를 중시",
"place_name":"마테호른",
"flag":"https://flagcdn.com/w320/ch.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Matterhorn.jpg/800px-Matterhorn.jpg"},

"ESTJ":{"name":"🇸🇬 싱가포르","capital":"싱가포르","population":"590만","food":"칠리크랩","fact":"금융 중심",
"reason":"효율성과 질서를 중시",
"place_name":"마리나 베이 샌즈",
"flag":"https://flagcdn.com/w320/sg.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Marina_Bay_Sands.jpg/800px-Marina_Bay_Sands.jpg"},

"ESFJ":{"name":"🇮🇹 이탈리아","capital":"로마","population":"5900만","food":"피자","fact":"문화 중심",
"reason":"사교적이고 따뜻한 성격",
"place_name":"콜로세움",
"flag":"https://flagcdn.com/w320/it.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseum.jpg/800px-Colosseum.jpg"},

"ISTP":{"name":"🇦🇺 호주","capital":"캔버라","population":"2600만","food":"바비큐","fact":"자연 활동",
"reason":"자유롭고 실용적인 성향",
"place_name":"시드니 오페라하우스",
"flag":"https://flagcdn.com/w320/au.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Sydney_Opera_House_Sails.jpg/800px-Sydney_Opera_House_Sails.jpg"},

"ISFP":{"name":"🇫🇷 프랑스","capital":"파리","population":"6500만","food":"크루아상","fact":"예술 국가",
"reason":"감성과 미적 감각",
"place_name":"에펠탑",
"flag":"https://flagcdn.com/w320/fr.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Tour_Eiffel.jpg/800px-Tour_Eiffel.jpg"},

"ESTP":{"name":"🇧🇷 브라질","capital":"브라질리아","population":"2.1억","food":"슈하스코","fact":"열정 문화",
"reason":"도전적이고 활동적",
"place_name":"예수상",
"flag":"https://flagcdn.com/w320/br.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Cristo_Redentor.jpg/800px-Cristo_Redentor.jpg"},

"ESFP":{"name":"🇹🇭 태국","capital":"방콕","population":"7000만","food":"팟타이","fact":"관광 강국",
"reason":"즐거움과 자유 추구",
"place_name":"왓 프라깨우",
"flag":"https://flagcdn.com/w320/th.png",
"place":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Wat_Phra_Kaew.jpg/800px-Wat_Phra_Kaew.jpg"}
}

if st.button("✈️ 추천 받기"):

    c = countries[mbti]

    st.balloons()

    st.subheader(f"🎉 추천 나라: {c['name']}")

    st.image(c["flag"], width=120)

    st.write(f"🏙 수도: {c['capital']}")
    st.write(f"👥 인구: {c['population']}")
    st.write(f"🍽 음식: {c['food']}")
    st.write(f"⭐ 특징: {c['fact']}")

    st.success(f"💡 추천 이유: {c['reason']}")

    st.markdown(f"### 📸 {c['place_name']}")
    show_image(c["place"])

st.divider()
st.caption("💡 MBTI 기반 재미용 추천 앱")
