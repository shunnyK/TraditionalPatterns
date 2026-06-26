import pandas as pd
from symbol_mapper import (
    get_symbolic_motifs
)


def generate_creation_reason(
    user_name,
    user_text,
    meaning_keywords,
    emotion_keywords,
    selected_df=None
):

    if not meaning_keywords and selected_df is not None:

        meaning_keywords = []

        for meaning in selected_df["meaning"]:

            if pd.isna(meaning):
                continue

        meaning_keywords.extend(
            [
            x.strip()
            for x in str(meaning).split("|")
            if x.strip() and x.strip().lower() != "nan"
            ]
        )
        meaning_keywords = list(
            dict.fromkeys(meaning_keywords)
        )[:5]

    if not emotion_keywords and selected_df is not None:

        emotion_keywords = []

        for emotion in selected_df["emotion"]:

            if pd.isna(emotion):
                continue

            emotion_keywords.extend(
                [
                    x.strip()
                    for x in str(emotion).split("|")
                    if x.strip() and x.strip().lower() != "nan"
                ]
            )

        emotion_keywords = list(
            dict.fromkeys(emotion_keywords)
        )[:5]

    symbolic_motifs = get_symbolic_motifs(
        meaning_keywords
    )

    top_symbols = [
        motif
        for motif, score
        in symbolic_motifs[:3]
    ]

    meaning_text = (
        ", ".join(meaning_keywords)
        if meaning_keywords
        else "전통적인 아름다움"
    )

    emotion_text = (
        ", ".join(emotion_keywords)
        if emotion_keywords
        else "고유하고 품격 있는"
    )

    symbol_text = (
        ", ".join(top_symbols)
        if top_symbols
        else "추천된 전통 상징"
    )

    reason = f"""

    ### 🌿 생성 이유

    {user_name}님은

    "{user_text}"

    라는 마음을 담고 싶어 하셨어요.

    AI는 이를 분석하여

    '{meaning_text}'의 의미와
    '{emotion_text}'의 감성을 반영했어요.

    또한 22,000개의 전통문양 데이터를 바탕으로

    '{meaning_text}'과 연결될 수 있는 전통 상징을 참고했어요.

    이번 문양은

    '{meaning_text}'의 가치를 담고 있으며,
    전체적으로 '{emotion_text}'의 분위기를 표현합니다.

    한국 전통의 상징과 {user_name}님의 이야기가 만나
    세상에 하나뿐인 전통문양으로 탄생했어요 🌿
    """

    return reason