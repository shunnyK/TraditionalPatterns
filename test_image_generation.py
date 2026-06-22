from openai_image_generator import (
    generate_pattern_image,
    save_image
)

prompt = """
Korean traditional pattern

crane motif
lotus motif
peony motif

symbolizing:
longevity
happiness
prosperity

traditional Korean ornament
symmetrical composition
Joseon dynasty style
gold decorative line art
white background
high detail
"""

print("생성 시작...")

image_base64 = generate_pattern_image(
    prompt
)

save_image(
    image_base64,
    "test_pattern.png"
)

print("생성 완료!")