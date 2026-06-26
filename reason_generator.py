print("reason_generator loaded")
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

            meaning_keywords.extend(
                str(meaning).split("|")
            )

        meaning_keywords = list(
            dict.fromkeys(meaning_keywords)
        )[:5]

    if not emotion_keywords and selected_df is not None:

        emotion_keywords = []

        for emotion in selected_df["emotion"]:

            emotion_keywords.extend(
                str(emotion).split("|")
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

{symbol_text}의 상징성을 바탕으로
새롭게 재해석된 전통문양이에요.

전통적인 의미는 유지하면서도
{user_name}님만의 감성을 담아
새로운 형태로 표현했어요 ✨
"""

    return reason