import streamlit as st
import os
import pandas as pd
import plotly.express as px
from reason_generator import (
    generate_creation_reason
)
from openai_image_generator import (
    generate_pattern_image,
    save_image
)

from recommend_engine import (
    recommend_patterns,
    make_reason,
    find_image_path
)

from color_recommender import (
    recommend_colors,
    format_colors_for_prompt
)

from education_card import (
    make_education_card
)

from story_generator import (
    generate_story
)

from symbol_visualizer import (
    get_symbol_relationships
)

from color_mapper import (
    translate_colors
)

from image_resizer import (
    resize_image_for_download,
    SIZE_PRESETS
)

from keyword_mapper import extract_keywords
from prompt_builder import build_generation_prompt


# ----------------------------------
# 페이지 설정
# ----------------------------------

st.set_page_config(
    page_title="HeritageAI",
    page_icon="🏯",
    layout="wide"
)


# ----------------------------------
# 제목
# ----------------------------------

st.title("🏯 HeritageAI")
st.subheader("AI 기반 개인 맞춤형 전통문양 생성 서비스")

st.write(
    """
원하는 감정이나 목적을 입력하면 AI가 전통문양 데이터를 분석해서
어울리는 전통문양을 추천하고, 선택한 문양의 의미와 감성을 바탕으로
새로운 개인 맞춤형 전통문양 생성 프롬프트를 만들어드려요 😀
"""
)


# ----------------------------------
# 사용자 입력
# ----------------------------------

user_name = st.text_input(
    "이름을 입력해주세요",
    placeholder="예: 홍길동"
)

user_text = st.text_area(
    "어떤 마음을 담고 싶은지 자유롭게 적어주세요",
    placeholder="""
예시)
부모님 환갑 선물로 드릴 건데
건강하게 오래 사셨으면 좋겠고
고급스럽고 우아한 느낌이면 좋겠어요.
"""
)

user_mode = st.radio(
    "사용 모드를 선택해주세요",
    ["일반 사용자 모드", "디자이너 모드"],
    horizontal=True
)

purpose = st.selectbox(
    "활용 목적을 선택해주세요",
    [
        "선물용",
        "교육용",
        "브랜드 디자인",
        "관광 상품",
        "인테리어 소품"
    ]
)

purpose_descriptions = {

    "선물용":
    """
    🎁 선물 받는 사람의 마음을 담아
    감성적이고 의미 있는 전통문양을 생성합니다.

    추천 상황
    - 부모님 환갑 선물
    - 결혼 축하 선물
    - 기념일 선물
    """,

    "교육용":
    """
    📖 전통 상징과 의미가 잘 드러나는 문양을 생성합니다.

    추천 상황
    - 학교 수업
    - 문화유산 교육
    - 전통문양 학습 자료

    특징
    - 상징이 명확하게 표현됨
    - 의미 해설에 적합
    """,

    "브랜드 디자인":
    """
    🎨 로고와 패키지 디자인에 활용하기 좋은 형태로 생성합니다.

    추천 상황
    - 브랜드 로고
    - 패키지 디자인
    - 기업 굿즈

    특징
    - 단순화된 형태
    - 상징성 강조
    """,

    "관광 상품":
    """
    🏯 관광 기념품과 문화상품에 적합한 문양을 생성합니다.

    추천 상황
    - 엽서
    - 텀블러
    - 키링
    - 에코백

    특징
    - 장식성 강조
    - 전통미 강조
    """,

    "인테리어 소품":
    """
    🪴 공간을 꾸미기 좋은 심미적인 문양을 생성합니다.

    추천 상황
    - 액자
    - 포스터
    - 벽장식

    특징
    - 균형감 있는 구성
    - 고급스러운 분위기
    """
}

with st.expander(
    f"📌 {purpose}은(는) 어떤 문양을 생성하나요?"
):
    st.write(
        purpose_descriptions[purpose]
    )



custom_colors = ""

designer_style = ""

if user_mode == "디자이너 모드":

    custom_colors = st.text_input(
        "원하는 색상을 입력해주세요",
        placeholder="""
        예:
        하늘색, 연노랑, 옥색, navy blue
        남색, 자주색
        #6A4C93
"""
    )

    designer_style = st.radio(
        "디자인 스타일",
        [
            "미니멀",
            "고급스러운",
            "현대적",
            "전통적",
            "화려한"
        ],
        horizontal=True
    )

# ----------------------------------
# 추천 버튼
# ----------------------------------

if st.button("전통문양 추천받기"):

    if not user_name:
        st.warning("이름을 입력해주세요.")
        st.stop()

    if not user_text:
        st.warning("설명을 입력해주세요.")
        st.stop()

    # ------------------------------
    # 키워드 추출
    # ------------------------------

    keywords = extract_keywords(user_text)

    meaning_keywords = keywords["meaning"]
    emotion_keywords = keywords["emotion"]
    motif_keywords = keywords["motif"]

    st.success("분석 완료!")

    st.write("### 추출된 키워드")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("의미")
        st.write(meaning_keywords)

    with col2:
        st.write("감성")
        st.write(emotion_keywords)

    with col3:
        st.write("모티프")
        st.write(motif_keywords)

    # ------------------------------
    # 추천
    # ------------------------------

    results = recommend_patterns(
        meaning_keywords,
        emotion_keywords,
        motif_keywords,
        top_n=3
    )

    # 추천 결과를 session_state에 저장
    st.session_state["results"] = results
    st.session_state["user_name"] = user_name
    st.session_state["user_text"] = user_text
    st.session_state["meaning_keywords"] = meaning_keywords
    st.session_state["emotion_keywords"] = emotion_keywords
    st.session_state["motif_keywords"] = motif_keywords
    st.session_state["user_mode"] = user_mode
    st.session_state["custom_colors"] = custom_colors
    st.session_state["purpose"] = purpose
    st.session_state["designer_style"] = designer_style

# ----------------------------------
# 추천 결과 출력
# ----------------------------------

if "results" in st.session_state:

    results = st.session_state["results"]
    user_name = st.session_state["user_name"]
    user_text = st.session_state["user_text"]
    meaning_keywords = st.session_state["meaning_keywords"]
    emotion_keywords = st.session_state["emotion_keywords"]
    motif_keywords = st.session_state["motif_keywords"]
    user_mode = st.session_state["user_mode"]
    custom_colors = st.session_state["custom_colors"]
    purpose = st.session_state["purpose"]
    designer_style = st.session_state["designer_style"]
    
    
    st.divider()
    st.header("✨ 추천 전통문양 TOP 3")

    selected_rows = []

    for rank, (_, row) in enumerate(results.iterrows(), start=1):

        st.divider()
        st.subheader(f"TOP {rank} · {row['title']}")

        image_path = find_image_path(row["file_name"])

        col1, col2 = st.columns([1, 2])

        with col1:
            if image_path:
                st.image(
                    image_path,
                    use_container_width=True
                )
            else:
                st.warning("이미지를 찾을 수 없습니다.")

        with col2:
            st.write(f"**문양 종류:** {row['patern_type']}")
            st.write(f"**의미:** {row['meaning']}")
            st.write(f"**감성:** {row['emotion']}")
            st.write(f"**모티프:** {row['motif']}")

            st.write(
                make_reason(
                    row,
                    user_name,
                    meaning_keywords,
                    emotion_keywords,
                    motif_keywords
                )
            )

            selected = st.checkbox(
                f"{row['title']} 생성에 참고하기",
                key=f"select_{row['identifier']}"
            )

            if selected:
                selected_rows.append(row)
                
    # ----------------------------------
    # 전통 상징 관계 분석
    # ----------------------------------

    relationships = get_symbol_relationships(
        meaning_keywords
    )

    if relationships:

        st.divider()

        st.header("📊 전통 상징 관계 분석")

        st.write(
            """
            입력하신 의미와 연결된 전통 상징을
            22,000건 전통문양 데이터에서 분석한 결과입니다.
            """
        )

        for meaning, motifs in relationships.items():

            st.subheader(
                f"🔎 '{meaning}'을 상징하는 대표 전통문양"
            )

            chart_df = pd.DataFrame(
                motifs,
                columns=[
                    "전통상징",
                    "빈도"
                ]
            )

            chart_df = chart_df.sort_values(
                by="빈도",
                ascending=False
            )


            fig = px.bar(
                chart_df,
                x="빈도",
                y="전통상징",
                orientation="h",
                text="빈도"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                height=350,
                xaxis_title="등장 빈도",
                yaxis_title="",
                showlegend=False,
                yaxis={
                    "categoryorder": "total ascending"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# ------------------------------
# 선택 문양 기반 생성 프롬프트
# ------------------------------

    st.divider()
    st.header("🎨 개인 맞춤형 전통문양 생성")
    
    download_size = st.selectbox(
        "다운로드 크기 선택",
        list(SIZE_PRESETS.keys())
    )

    if len(selected_rows) == 0:

        st.info("생성에 참고할 문양을 1개 이상 선택해주세요.")

    else:

        selected_df = pd.DataFrame(selected_rows)
        
        recommended_colors = recommend_colors(selected_df)
        
        if user_mode == "디자이너 모드" and custom_colors:
            
            translated_colors = translate_colors(
                custom_colors
            )
            
            color_text = (
                f"Use designer-specified colors: "
                f"{translated_colors}"
            )
        else:
            color_text = format_colors_for_prompt(recommended_colors)
        
        st.write("### 🎨 추천 전통 색상")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("선 색상")
            st.write(recommended_colors["line_colors"])
            
            
        with col2:
            st.write("배경 색상")
            st.write(recommended_colors["background_colors"])

        generation_prompt = build_generation_prompt(
            selected_df,
            user_text,
            meaning_keywords,
            emotion_keywords,
            purpose,
            designer_style,
            color_text
    )

        with st.expander("생성 프롬프트 보기"):

            st.code(generation_prompt)

        if st.button("🎨 전통문양 생성하기"):

            with st.spinner("AI가 전통문양을 생성하고 있어요..."):

                image_base64 = generate_pattern_image(
                    generation_prompt
                )

                image_path = save_image(
                    image_base64,
                    "generated_pattern.png"
                )
                
                resize_image_path = resize_image_for_download(
                    image_path,
                    download_size,
                    "download_pattern.png"
                )

                st.success("전통문양 생성 완료!")

                st.image(
                image_path,
                caption=f"{user_name}님만의 전통문양",
                use_container_width=True
                )
                
                with open(resize_image_path, "rb") as file:
                    st.download_button(
                        label="생성된 전통문양 다운로드",
                        data=file,
                        file_name=f"{user_name}_traditional_pattern.png",
                        mime="image/png"
                    )

            # --------------------------
            # 생성 이유 설명
            # --------------------------

                st.markdown(
                    generate_creation_reason(
                        user_name,
                        user_text,
                        meaning_keywords,
                        emotion_keywords
                    )
                )
                
                st.markdown(
                    make_education_card(
                        selected_df
                    )
                )
                
                st.markdown(
                    generate_story(
                        user_name,
                        user_text,
                        meaning_keywords,
                        emotion_keywords
                    )
                )