import pytesseract
from PIL import Image
import os
# input_image_path = "inputs/images/test.png"  # Define the input image path
input_image_path = "inputs/images/test_text_image.png"  # Define the input image path

from src.modules.talk_to_image import ImageYOLOHandler, ImageOCRHandler, OpenAIImageTextExtractor
from src.core.config import DOC_LAYOUT_YOLO_MODEL_PATH

# # Test ImageHandler
# image_handler = ImageYOLOHandler(DOC_LAYOUT_YOLO_MODEL_PATH)
# process_result = image_handler.process_image(input_image_path)  # Use the variable
# print(process_result)

# Test OpenAIImageTextExtractor
openai_extractor = OpenAIImageTextExtractor()
openai_extraction_result = openai_extractor.process_image(input_image_path)  # Use the variable
print(openai_extraction_result)

# # Test ImageTextExtractor
# extractor = ImageOCRHandler()
# extraction_result = extractor.process_image(input_image_path)  # Use the variable
# print(extraction_result)


''' next steps would be to send the user query along with the extracted text from openai to the openai'''