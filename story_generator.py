from symbol_mapper import (
    get_symbolic_motifs
)


def generate_story(
    user_name,
    user_text,
    meaning_keywords,
    emotion_keywords
):

    symbolic_motifs = get_symbolic_motifs(
        meaning_keywords
    )

    top_symbols = []

    for item in symbolic_motifs[:3]:

        if isinstance(item, tuple):
            top_symbols.append(item[0])
        else:
            top_symbols.append(item)

    meaning_text = ", ".join(
        meaning_keywords
    )

    emotion_text = ", ".join(
        emotion_keywords
    )

    motif_text = ", ".join(
        top_symbols
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