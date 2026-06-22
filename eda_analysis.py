import pandas as pd
from collections import Counter

df = pd.read_csv("traditional_pattern_dataset.csv")

print("전체 데이터 수")
print(len(df))

print("\n문양 종류 분포")
print(df["patern_type"].value_counts())

print("\n활용 분야 분포")
print(df["patern_usage"].value_counts())

print("\n시대 분포")
print(df["temporal"].value_counts())

# -------------------------
# 리스트 컬럼 빈도 계산
# -------------------------

def count_multi_values(column):

    counter = Counter()

    for value in df[column].dropna():

        items = str(value).split("|")

        items = [x.strip() for x in items if x.strip()]

        counter.update(items)

    return pd.DataFrame(
        counter.most_common(50),
        columns=[column, "count"]
    )

# 의미
meaning_df = count_multi_values("meaning")

# 감성
emotion_df = count_multi_values("emotion")

# 모티프
motif_df = count_multi_values("motif")

print("\n===== Meaning TOP 20 =====")
print(meaning_df.head(20))

print("\n===== Emotion TOP 20 =====")
print(emotion_df.head(20))

print("\n===== Motif TOP 20 =====")
print(motif_df.head(20))

# 저장
meaning_df.to_csv(
    "meaning_freq.csv",
    index=False,
    encoding="utf-8-sig"
)

emotion_df.to_csv(
    "emotion_freq.csv",
    index=False,
    encoding="utf-8-sig"
)

motif_df.to_csv(
    "motif_freq.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nEDA 결과 저장 완료")