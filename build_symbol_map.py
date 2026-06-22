import pandas as pd
import json
from collections import Counter

# --------------------------
# 데이터 로드
# --------------------------

df = pd.read_csv(
    "traditional_pattern_dataset.csv"
)

symbol_map = {}

# --------------------------
# meaning -> motif 빈도 계산
# --------------------------

for _, row in df.iterrows():

    meanings = str(
        row["meaning"]
    ).split("|")

    motifs = str(
        row["motif"]
    ).split("|")

    # motif 정리
    motifs = [
        m.strip()
        for m in motifs
        if m.strip()
        and m.strip().lower() != "nan"
    ]

    for meaning in meanings:

        meaning = meaning.strip()

        # 빈 값 제거
        if meaning == "":
            continue

        if meaning.lower() == "nan":
            continue

        if meaning not in symbol_map:

            symbol_map[meaning] = Counter()

        symbol_map[meaning].update(
            motifs
        )

# --------------------------
# TOP5 + 빈도 저장
# --------------------------

final_map = {}

for meaning, counter in symbol_map.items():

    final_map[meaning] = dict(
        counter.most_common(5)
    )

# --------------------------
# 저장
# --------------------------

with open(
    "symbol_map.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        final_map,
        f,
        ensure_ascii=False,
        indent=4
    )

print("symbol_map.json 생성 완료")