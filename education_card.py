from pattern_dictionary import (
    PATTERN_DICTIONARY
)


ADDITIONAL_PATTERN_DICTIONARY = {
    "나무": "생명력, 성장, 번영을 상징합니다.",
    "매화": "고결한 인품과 절개, 봄의 시작을 상징합니다.",
    "새": "기쁜 소식과 희망, 좋은 인연을 상징합니다.",
    "국화": "장수와 고결함을 상징합니다.",
    "구름": "길운과 복을 상징합니다.",
    "봉황": "평화와 번영, 고귀함을 상징합니다.",
    "모란": "부귀영화와 아름다움을 상징합니다.",
    "연꽃": "청렴함과 순수함을 상징합니다.",
    "거북": "장수와 건강을 상징합니다.",
    "학": "장수와 길상을 상징합니다.",
    "수자": "오래 살기를 바라는 장수의 의미를 상징합니다.",
    "만자": "길상과 복덕을 상징합니다.",
    "덩굴": "끊임없는 생명력과 번영을 상징합니다.",
    "박쥐": "복과 길상을 상징합니다.",
    "나비": "행복한 인연과 기쁨을 상징합니다.",
    "복숭아": "장수와 불로장생을 상징합니다.",
    "소나무": "절개와 장수, 변치 않는 생명력을 상징합니다.",
    "대나무": "절개와 곧은 마음, 지조를 상징합니다.",
    "물고기": "풍요와 다산, 길상을 상징합니다.",
    "용": "권위와 힘, 수호의 의미를 상징합니다.",
    "호랑이": "용맹함과 수호, 벽사의 의미를 상징합니다.",
    "사슴": "장수와 평안, 신성함을 상징합니다.",
    "해": "밝음과 생명력, 새로운 시작을 상징합니다.",
    "달": "풍요와 순환, 평온함을 상징합니다.",
    "별": "희망과 길운, 밝은 미래를 상징합니다.",
    "바위": "변하지 않는 믿음과 장수를 상징합니다.",
    "파도": "생명력과 흐름, 역동성을 상징합니다.",
    "산": "안정과 보호, 굳건함을 상징합니다.",
    "꽃": "아름다움과 기쁨, 번영을 상징합니다.",
    "열매": "풍요와 결실, 번영을 상징합니다.",
    "잎": "생명력과 성장, 자연의 조화를 상징합니다."
}


def clean_items(
    text
):

    items = []

    for item in str(text).split("|"):

        item = item.strip()

        if not item:
            continue

        if item.lower() == "nan":
            continue

        items.append(item)

    return items


def make_education_card(
    selected_df
):

    motifs = []

    for _, row in selected_df.iterrows():

        motifs.extend(
            clean_items(
                row["motif"]
            )
        )

    motifs = list(
        dict.fromkeys(motifs)
    )

    result = "## 📖 전통문양 해설 카드\n\n"

    for motif in motifs[:10]:

        description = PATTERN_DICTIONARY.get(
            motif
        )

        if description is None:

            description = ADDITIONAL_PATTERN_DICTIONARY.get(
                motif,
                "전통문화 속에서 길상과 아름다움을 표현하는 상징 요소입니다."
            )

        result += (
            f"**{motif}**\n"
            f"- {description}\n\n"
        )

    return result