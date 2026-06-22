# keyword_mapper.py

# 사용자의 자연어 입력을 전통문양 데이터의 meaning / emotion / motif 키워드로 바꾸는 파일

meaning_dict = {
    # 가족 / 선물
    "부모님": ["장수", "행복"],
    "엄마": ["행복", "아름다움"],
    "아빠": ["장수", "권위"],
    "할머니": ["장수", "행복"],
    "할아버지": ["장수", "행복"],
    "가족": ["행복", "풍요"],
    "선물": ["행복", "길상"],

    # 생일 / 환갑 / 건강
    "생일": ["행복", "길상"],
    "환갑": ["장수", "행복"],
    "건강": ["장수"],
    "오래": ["장수"],
    "장수": ["장수"],
    "행복": ["행복"],

    # 사랑 / 연인 / 결혼
    "사랑": ["사랑", "행복"],
    "연인": ["사랑", "행복"],
    "커플": ["사랑", "행복"],
    "결혼": ["부부 금슬", "행복"],
    "부부": ["부부 금슬", "행복"],

    # 친구 / 우정
    "친구": ["우정", "행복"],
    "우정": ["우정"],
    "응원": ["소원성취", "행복"],

    # 성공 / 사업 / 개업
    "성공": ["번영", "소원성취"],
    "합격": ["소원성취"],
    "취업": ["소원성취", "번영"],
    "개업": ["번영", "풍요"],
    "사업": ["번영", "풍요"],
    "돈": ["풍요", "번영"],
    "부자": ["풍요", "번영"],

    # 보호 / 평안
    "보호": ["수호"],
    "지켜": ["수호"],
    "평안": ["길상", "행복"],
    "안정": ["길상", "행복"],

    # 전통 상징
    "복": ["길상", "행복"],
    "좋은일": ["길상", "행복"],
    "행운": ["길상"],
    "소원": ["소원성취"],
    "바람": ["소원성취"]
}


emotion_dict = {
    # 고급 / 우아
    "고급": ["고급스러운"],
    "고급스럽": ["고급스러운"],
    "우아": ["우아한"],
    "품격": ["고급스러운", "우아한"],

    # 깔끔 / 단순
    "깔끔": ["깔끔한"],
    "심플": ["단순한", "깔끔한"],
    "단순": ["단순한"],
    "미니멀": ["단순한", "깔끔한"],

    # 화려 / 장식
    "화려": ["화려한", "장식적인"],
    "장식": ["장식적인"],
    "풍성": ["풍성한"],

    # 전통 / 고전
    "전통": ["고전적인"],
    "고전": ["고전적인"],
    "한국적": ["고전적인", "조화로운"],

    # 부드러움 / 자연
    "부드러": ["부드러운"],
    "따뜻": ["부드러운", "조화로운"],
    "차분": ["조화로운", "소박한"],
    "자연": ["자연적인"],
    "소박": ["소박한"],

    # 현대 / 독특
    "현대": ["현대적인"],
    "트렌디": ["현대적인"],
    "독특": ["독특한"],
    "신비": ["신비한"],

    # 귀여움 / 활동성
    "귀여": ["귀여운"],
    "활동": ["활동적인"],
    "강렬": ["강한"],
    "강한": ["강한"]
}


motif_dict = {
    # 식물
    "꽃": ["꽃"],
    "연꽃": ["연꽃"],
    "매화": ["매화"],
    "국화": ["국화"],
    "모란": ["모란"],
    "잎": ["잎"],
    "덩굴": ["덩굴"],

    # 동물
    "학": ["학"],
    "나비": ["나비"],
    "박쥐": ["박쥐"],
    "새": ["새"],

    # 자연/기하
    "구름": ["구름"],
    "원": ["원"],
    "기하": ["기하문"],

    # 문자
    "문자": ["문자"],
    "복": ["문자"],
    "수": ["수자"]
}


def remove_duplicates(items):
    """리스트 중복 제거. 순서는 유지."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def extract_keywords(user_text):
    """
    사용자 자연어 문장에서 meaning / emotion / motif 키워드를 추출한다.
    GPT 없이 룰 기반으로 동작하는 MVP용 함수.
    """

    meaning_keywords = []
    emotion_keywords = []
    motif_keywords = []

    for key, values in meaning_dict.items():
        if key in user_text:
            meaning_keywords.extend(values)

    for key, values in emotion_dict.items():
        if key in user_text:
            emotion_keywords.extend(values)

    for key, values in motif_dict.items():
        if key in user_text:
            motif_keywords.extend(values)

    meaning_keywords = remove_duplicates(meaning_keywords)
    emotion_keywords = remove_duplicates(emotion_keywords)
    motif_keywords = remove_duplicates(motif_keywords)

    return {
        "meaning": meaning_keywords,
        "emotion": emotion_keywords,
        "motif": motif_keywords
    }


# 이 파일만 단독 실행했을 때 테스트용
if __name__ == "__main__":
    text = input("원하는 문양 설명을 입력하세요: ")

    result = extract_keywords(text)

    print("\n추출 결과")
    print("meaning:", result["meaning"])
    print("emotion:", result["emotion"])
    print("motif:", result["motif"])