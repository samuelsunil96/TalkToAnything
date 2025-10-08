import cv2
import os
import logging
from src.core.config import IMAGE_OUTPUT_DIR, DOC_LAYOUT_YOLO_MODEL_PATH
from src.services.image_detection import ImageDetector

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ImageHandler:
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
            output_path = self.detector.detect_and_annotate(image_path)
            logging.info("Processed image: %s", image_path)

        except Exception as e:
            logging.exception("An error occurred while processing the image: %s", e)
            return f"An error occurred: {str(e)}"

        return f"Image processed and saved to {output_path}"
    

'''next steps are to send this extracted text
 from the image to llm along with user query to answer the users question'''    
