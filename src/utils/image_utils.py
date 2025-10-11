import base64

def encode_image(image_path):
    """Encode an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_image_input(base64_image):
    """Return input payload for image text extraction."""
    return [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Please extract the text from this image."},
                {"type": "input_image", "image_url": f"data:image/jpeg;base64,{base64_image}"},
            ],
        }
    ]