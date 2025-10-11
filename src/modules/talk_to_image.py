from abc import ABC, abstractmethod
import pytesseract
from PIL import Image
import os
import logging
from src.core.config import IMAGE_OUTPUT_DIR, DOC_LAYOUT_YOLO_MODEL_PATH, IMAGE_TEXT_OUTPUT_DIR
from src.services.llm_service import OpenAIService  # Import OpenAIService
import openai  # Make sure to install the OpenAI library
from src.services.image_detection import ImageDetector

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BaseImageProcessor(ABC):
    """Abstract base class for image processing."""

    @abstractmethod
    def process_image(self, output_dir, image_path):
        """Process an image and save the result."""
        pass


class ImageYOLOHandler(BaseImageProcessor):
    """Class to handle image processing using YOLO."""

    def __init__(self, DOC_LAYOUT_YOLO_MODEL_PATH):
        self.detector = ImageDetector()
        logging.info("ImageHandler initialized with model: %s", DOC_LAYOUT_YOLO_MODEL_PATH)

    def process_image(self, image_path, output_dir=IMAGE_OUTPUT_DIR):
        """Process an image and save the annotated result."""
        if not os.path.exists(image_path):
            logging.error("Image not found: %s", image_path)
            return "Image not found."

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info("Output directory created: %s", output_dir)

        try:
            # 1. Run the YOLO Model
            output_path = self.detector.detect_and_annotate(image_path)  # Use the provided image_path
            logging.info("Processed image: %s", image_path)

        except Exception as e:
            logging.exception("An error occurred while processing the image: %s", e)
            return f"An error occurred: {str(e)}"

        return f"Image processed and saved to {output_path}"
    

class OpenAIImageTextExtractor(BaseImageProcessor):
    """Class to extract text from images using OpenAI API."""

    def __init__(self):
        self.service = OpenAIService()

    def process_image(self, image_path):
        """Extract text from the image using OpenAI API."""
        try:
            # Assuming the image is sent to the OpenAI API for text extraction
            return self.service.send_image(image_path)  # Use the OpenAIService to get text
        except Exception as e:
            logging.exception("An error occurred while extracting text: %s", e)
            return f"An error occurred: {str(e)}"

class ImageOCRHandler(BaseImageProcessor):
    """Class to handle text extraction from images using pytesseract."""

    def __init__(self, output_dir=IMAGE_TEXT_OUTPUT_DIR):
        self.output_dir = output_dir
        self.extracted_text = ""

    def process_image(self, image_path):
        """Extract text from the image and save it to a file."""
        try:
            image = Image.open(image_path)  # Use the provided image_path
            self.extracted_text = pytesseract.image_to_string(image)  # Extract text

            # Ensure the output directory exists
            os.makedirs(self.output_dir, exist_ok=True)

            # Write the extracted text to a file
            output_file_path = os.path.join(self.output_dir, "extracted_text.txt")
            with open(output_file_path, "w") as text_file:
                text_file.write(self.extracted_text)

            return f"Image processed and text saved to {output_file_path}"

        except Exception as e:
            logging.exception("An error occurred while extracting text: %s", e)
            return f"An error occurred: {str(e)}"

