import pandas as pd

from symbol_mapper import (
    get_symbolic_motifs
)


def clean_items(
    values
):

    result = []

    for value in values:

        if pd.isna(value):
            continue

        for item in str(value).split("|"):

            item = item.strip()

            if not item:
                continue

            if item.lower() == "nan":
                continue

            result.append(item)

    return list(
        dict.fromkeys(result)
    )


def generate_story(
    user_name,
    user_text,
    meaning_keywords,
    emotion_keywords,
    selected_df=None
):

    if not meaning_keywords and selected_df is not None:

        meaning_keywords = clean_items(
            selected_df["meaning"]
        )[:5]

    if not emotion_keywords and selected_df is not None:

        emotion_keywords = clean_items(
            selected_df["emotion"]
        )[:5]

    symbolic_motifs = get_symbolic_motifs(
        meaning_keywords
    )

    top_symbols = []

    for item in symbolic_motifs[:3]:

        if isinstance(item, tuple):
            top_symbols.append(item[0])
        else:
            top_symbols.append(item)

    if not top_symbols and selected_df is not None:

        top_symbols = clean_items(
            selected_df["motif"]
        )[:3]

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

    motif_text = (
        ", ".join(top_symbols)
        if top_symbols
        else "전통 상징"
    )

    story = f"""
## ✨ {user_name}님의 전통문양 이야기

{user_name}님은

"{user_text}"

라는 마음을 담고 싶어 하셨어요.

AI는 이 마음에서

**{meaning_text}**

의 의미를 발견했어요.

그리고 전통문양 데이터 분석을 통해

**{motif_text}**

상징을 함께 활용했어요.

이 문양은

'{meaning_text}'의 가치를 담고 있으며,

전체적으로 '{emotion_text}'의 분위기를 표현합니다.

한국 전통의 상징과
{user_name}님의 이야기가 만나

세상에 하나뿐인 전통문양으로 탄생했어요 🌿
"""

    return story