import os
import base64

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


print("API KEY FOUND:",

      os.getenv("OPENAI_API_KEY") is not None)

def generate_pattern_image(prompt):

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json

    return image_base64


def save_image(image_base64, save_path):

    image_bytes = base64.b64decode(
        image_base64
    )

    with open(save_path, "wb") as f:
        f.write(image_bytes)

    return save_path