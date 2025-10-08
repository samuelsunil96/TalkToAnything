import os
import cv2
import uuid
from doclayout_yolo import YOLOv10
from src.core.config import DOC_LAYOUT_YOLO_MODEL_PATH, IMAGE_OUTPUT_DIR

class ImageDetector:
    """Class to handle image detection using YOLOv10."""

    def __init__(self):
        """Initialize the detector with the pretrained YOLOv10 model."""
        self.model = YOLOv10(DOC_LAYOUT_YOLO_MODEL_PATH)


    def detect_and_annotate(self, image_path, imgsz=1024, conf=0.2, device="cpu"):
            """Perform detection on the image and save the annotated result."""
            output_filename = f"output_{uuid.uuid4()}.png"
            output_path = os.path.join(IMAGE_OUTPUT_DIR, output_filename)
            output_path = os.path.normpath(output_path)
            """Perform detection on the image and save the annotated result."""
            # Perform prediction
            det_res = self.model.predict(
                image_path,
                imgsz=imgsz,
                conf=conf,
                device=device
            )

            # Annotate and save the result
            annotated_frame = det_res[0].plot(pil=True, line_width=5, font_size=20)
            cv2.imwrite(output_path, annotated_frame)
            return output_path

if __name__ == "__main__":
    detector = ImageDetector()
    test_image_path = "inputs/images/test.png"
    output_path = detector.detect_and_annotate(test_image_path)
    print(f"Annotated image saved at: {output_path}")
