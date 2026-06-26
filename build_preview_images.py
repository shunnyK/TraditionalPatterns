import os
import pandas as pd
from PIL import Image


CSV_PATH = "traditional_pattern_dataset.csv"
SOURCE_DIR = "test"
OUTPUT_DIR = "assets/preview_images"

PREVIEW_SIZE = (500, 500)
IMAGE_QUALITY = 75


def normalize_filename(name):
    return str(name).strip()


def main():
    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    df = pd.read_csv(
        CSV_PATH
    )

    file_names = set(
        df["file_name"]
        .dropna()
        .astype(str)
        .map(normalize_filename)
    )

    print(f"CSV 기준 이미지 파일 수: {len(file_names)}")

    image_map = {}

    for root, dirs, files in os.walk(SOURCE_DIR):

        for file in files:

            normalized_file = normalize_filename(
                file
            )

            if normalized_file in file_names:

                image_map[normalized_file] = os.path.join(
                    root,
                    file
                )

    print(f"원본 폴더에서 찾은 이미지 수: {len(image_map)}")

    success_count = 0
    fail_count = 0

    for file_name, src_path in image_map.items():

        dst_path = os.path.join(
            OUTPUT_DIR,
            file_name
        )

        if os.path.exists(dst_path):
            continue

        try:
            image = Image.open(
                src_path
            ).convert("RGB")

            image.thumbnail(
                PREVIEW_SIZE
            )

            image.save(
                dst_path,
                "JPEG",
                quality=IMAGE_QUALITY,
                optimize=True
            )

            success_count += 1

        except Exception as e:

            print(
                f"실패: {file_name} / {e}"
            )

            fail_count += 1

    print(f"미리보기 이미지 생성 완료: {success_count}개")
    print(f"실패: {fail_count}개")


if __name__ == "__main__":
    main()