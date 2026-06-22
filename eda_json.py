import os
import json
import pandas as pd
from glob import glob

# ==========================================
# 경로 설정
# ==========================================

BASE_DIR = "/Users/seohyeon/Desktop/shunny/personal_project/TraditionalPatterns/test/원천데이터"

json_files = glob(
    os.path.join(BASE_DIR, "**", "*.json"),
    recursive=True
)

print(f"\nJSON 파일 개수: {len(json_files)}")

rows = []

# ==========================================
# JSON -> DataFrame
# ==========================================

for idx, file_path in enumerate(json_files):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        contents = data.get("contents", {})
        image = contents.get("image", {})
        augmentation = contents.get("augmentation", {})

        rows.append({

            # 기본정보
            "identifier": data.get("identifier"),
            "title": data.get("title"),
            "description": data.get("description"),
            "classification_code": data.get("classification_code"),

            # 문양 정보
            "patern_type": contents.get("patern_type"),
            "patern_usage": contents.get("patern_usage"),
            "artifact_name": contents.get("artifact_name"),

            # 시대/재료
            "material": contents.get("material"),
            "temporal": contents.get("temporal"),
            "technique": contents.get("technique"),

            # 핵심 컬럼
            "meaning": "|".join(contents.get("meaning", [])),
            "motif": "|".join(contents.get("motif", [])),
            "form": "|".join(contents.get("form", [])),
            "emotion": "|".join(contents.get("emotion", [])),

            # 이미지
            "file_name": image.get("file_name"),
            "width": image.get("width"),
            "height": image.get("height"),

            # 색상
            "line_color": augmentation.get("line_color"),
            "background_color": augmentation.get("background_color")
        })

        if idx % 5000 == 0:
            print(f"{idx}개 처리 완료")

    except Exception as e:

        print("\n에러 발생")
        print(file_path)
        print(e)

# ==========================================
# DataFrame 생성
# ==========================================

df = pd.DataFrame(rows)

print("\n===== 데이터 미리보기 =====")
print(df.head())

print("\n===== 데이터 정보 =====")
print(df.info())

print("\n===== 총 데이터 수 =====")
print(len(df))

# ==========================================
# CSV 저장
# ==========================================

df.to_csv(
    "traditional_pattern_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\ntraditional_pattern_dataset.csv 저장 완료")