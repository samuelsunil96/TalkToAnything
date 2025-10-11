from src.modules.talk_to_image import ImageHandler
from src.core.config import DOC_LAYOUT_YOLO_MODEL_PATH

def main():
    image_handler = ImageHandler(DOC_LAYOUT_YOLO_MODEL_PATH)
    result = image_handler.process_image("inputs/images/test.png")
    print(result)

if __name__ == "__main__":
    main()