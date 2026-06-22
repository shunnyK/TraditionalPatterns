from PIL import Image


SIZE_PRESETS = {
    "정사각형 1024x1024": (1024, 1024),
    "스마트폰 배경화면 1080x1920": (1080, 1920),
    "노트북 배경화면 1920x1080": (1920, 1080),
    "A4 포스터 1240x1754": (1240, 1754),
    "B5 포스터 1031x1457": (1031, 1457)
}


def resize_image_for_download(
    image_path,
    preset_name,
    save_path
):

    target_width, target_height = SIZE_PRESETS[preset_name]

    image = Image.open(image_path).convert("RGB")

    # 원본 비율 유지하면서 target 영역 안에 맞춤
    image.thumbnail(
        (target_width, target_height)
    )

    # 흰 배경 캔버스 생성
    canvas = Image.new(
        "RGB",
        (target_width, target_height),
        "white"
    )

    # 가운데 배치
    x = (target_width - image.width) // 2
    y = (target_height - image.height) // 2

    canvas.paste(
        image,
        (x, y)
    )

    canvas.save(
        save_path,
        "PNG"
    )

    return save_path