from symbol_mapper import (
    get_symbolic_motifs
)


def generate_creation_reason(
    user_name,
    user_text,
    meaning_keywords,
    emotion_keywords
):

    symbolic_motifs = get_symbolic_motifs(
        meaning_keywords
    )

    top_symbols = [
        motif
        for motif, score
        in symbolic_motifs[:3]
    ]

    meaning_text = ", ".join(
        meaning_keywords
    )

    emotion_text = ", ".join(
        emotion_keywords
    )

    symbol_text = ", ".join(
        top_symbols
    )

    reason = f"""
### 🌿 생성 이유

{user_name}님은

"{user_text}"

라는 마음을 담고 싶어 하셨어요.

AI는 이를 분석하여

'{meaning_text}'의 의미와
'{emotion_text}'의 감성을 추출했어요.

또한 22,000개의 전통문양 데이터를 분석한 결과,

'{meaning_text}'과 가장 자주 연결되는 전통 상징은

{symbol_text}

으로 나타났어요.

그래서 이번 문양은

{symbol_text}의 상징성을 바탕으로
새롭게 재해석된 전통문양이에요.

전통적인 의미는 유지하면서도
{user_name}님만의 감성을 담아
새로운 형태로 표현했어요 ✨
"""

    return reason