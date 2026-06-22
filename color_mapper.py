# 디자이너 모드에서 영어뿐 아니라 한국어로 색상 입력 가능하도록!

COLOR_MAP = {

    # 빨강 계열
    "빨강": "red",
    "빨간색": "red",
    "진빨강": "dark red",
    "연빨강": "light red",

    # 분홍 계열
    "분홍": "pink",
    "분홍색": "pink",
    "연분홍": "light pink",
    "진분홍": "hot pink",

    # 주황 계열
    "주황": "orange",
    "주황색": "orange",

    # 노랑 계열
    "노랑": "yellow",
    "노란색": "yellow",
    "연노랑": "light yellow",
    "황금색": "gold",

    # 초록 계열
    "초록": "green",
    "초록색": "green",
    "연초록": "light green",
    "진초록": "dark green",

    # 한국 전통 색
    "옥색": "jade green",
    "비취색": "jade green",
    "청록색": "turquoise",

    # 파랑 계열
    "파랑": "blue",
    "파란색": "blue",
    "하늘색": "sky blue",
    "남색": "navy blue",
    "청색": "royal blue",

    # 보라 계열
    "보라": "purple",
    "보라색": "purple",
    "연보라": "lavender",
    "자주색": "magenta",

    # 갈색 계열
    "갈색": "brown",
    "베이지": "beige",

    # 무채색
    "흰색": "white",
    "아이보리": "ivory",
    "검정": "black",
    "검은색": "black",
    "회색": "gray",
    "은색": "silver"
}


def translate_colors(color_text):

    colors = [
        c.strip()
        for c in color_text.split(",")
    ]

    translated = []

    for color in colors:

        translated.append(
            COLOR_MAP.get(
                color,
                color
            )
        )

    return ", ".join(translated)