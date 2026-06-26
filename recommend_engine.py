import os
import pandas as pd
from keyword_mapper import extract_keywords
df = pd.read_csv("traditional_pattern_dataset.csv")

# 중복 문양 제거
df = df.drop_duplicates(subset=["identifier"]).reset_index(drop=True)

def score_pattern(row, meaning_keywords, emotion_keywords, motif_keywords):
    score = 0

    meaning = str(row["meaning"]).split("|")
    emotion = str(row["emotion"]).split("|")
    motif = str(row["motif"]).split("|")
    description = str(row["description"])

    for keyword in meaning_keywords:
        if keyword in meaning:
            score += 5
        if keyword in description:
            score += 1

    for keyword in emotion_keywords:
        if keyword in emotion:
            score += 4
        if keyword in description:
            score += 1

    for keyword in motif_keywords:
        if keyword in motif:
            score += 3
        if keyword in description:
            score += 1

    return score

def recommend_patterns(meaning_keywords, emotion_keywords, motif_keywords=None, top_n=3):

    if motif_keywords is None:
        motif_keywords = []

    # 원본 데이터 보호
    temp_df = df.copy()

    temp_df["score"] = temp_df.apply(
        lambda row: score_pattern(
            row,
            meaning_keywords,
            emotion_keywords,
            motif_keywords
        ),
        axis=1
    )

    result = (
        temp_df[temp_df["score"] > 0]
        .sort_values(by="score", ascending=False)
        .head(top_n)
    )

    return result

def find_image_path(file_name):
    import glob
    import re

    BASE_DIR = "assets/preview_images"

    file_name = str(file_name).strip()

    # 1. 파일명 그대로 찾기
    exact_path = os.path.join(
        BASE_DIR,
        file_name
    )

    if os.path.exists(exact_path):
        return exact_path

    # 2. 확장자 제거 후 찾기
    file_stem = os.path.splitext(file_name)[0]

    candidates = glob.glob(
        os.path.join(
            BASE_DIR,
            file_stem + ".*"
        )
    )

    if candidates:
        return candidates[0]

    # 3. 파일명 안의 숫자 추출 후 S00xxxx 패턴으로 찾기
    numbers = re.findall(
        r"\d+",
        file_name
    )

    for number in numbers:

        number = number[-6:]
        padded = number.zfill(6)

        patterns = [
            f"*S{padded}*",
            f"*S0{padded}*",
            f"*{padded}*",
            f"*{number}*"
        ]

        for pattern in patterns:

            candidates = glob.glob(
                os.path.join(
                    BASE_DIR,
                    pattern
                )
            )

            if candidates:
                return candidates[0]

    return None

def make_reason(row, user_name, meaning_keywords, emotion_keywords, motif_keywords):

    row_meaning = str(row["meaning"]).split("|")
    row_emotion = str(row["emotion"]).split("|")
    row_motif = str(row["motif"]).split("|")

    matched_meaning = [m for m in meaning_keywords if m in row_meaning]
    matched_emotion = [e for e in emotion_keywords if e in row_emotion]

    meaning_text = (
        ", ".join(matched_meaning)
        if matched_meaning
        else ", ".join(row_meaning[:2])
    )

    emotion_text = (
        ", ".join(matched_emotion)
        if matched_emotion
        else ", ".join(row_emotion[:2])
    )

    motif_text = ", ".join(row_motif)

    description = str(row["description"])

    # 너무 길면 잘라주기
    if len(description) > 180:
        description = description[:180] + "..."

    reason = f"""
✨ {user_name}님을 위한 전통문양 이야기

이 문양은 {motif_text}을(를) 바탕으로 만들어진 전통문양이에요.

'{meaning_text}'의 의미를 담고 있고,
전체적으로 '{emotion_text}'의 분위기가 느껴져요.

📖 전통 해설

{description}

{user_name}님이 담고 싶었던 마음을
한국 전통의 아름다움으로 표현하기에 잘 어울리는 문양이에요 🌿
"""

    return reason

if __name__ == "__main__":
    user_name = input("이름을 입력해주세요: ")
    user_text = input("\n원하는 문양을 설명해주세요: ")

    keywords = extract_keywords(user_text)

    meaning_keywords = keywords["meaning"]
    emotion_keywords = keywords["emotion"]
    motif_keywords = keywords["motif"]

    print("\n추출된 키워드")
    print("meaning:", meaning_keywords)
    print("emotion:", emotion_keywords)
    print("motif:", motif_keywords)

    results = recommend_patterns(
        meaning_keywords=meaning_keywords,
        emotion_keywords=emotion_keywords,
        motif_keywords=motif_keywords
    )

    print("\n추천 결과")
    for idx, row in results.iterrows():
        print("=" * 50)
        print("문양명:", row["title"])
        print("문양종류:", row["patern_type"])
        print("의미:", row["meaning"])
        print("감성:", row["emotion"])
        print("모티프:", row["motif"])
        print("이미지파일:", row["file_name"])
        image_path = find_image_path(row["file_name"])
        print("이미지경로:", image_path)
        print("점수:", row["score"])
        print("추천 해설:", make_reason(row, user_name, meaning_keywords, emotion_keywords, motif_keywords))