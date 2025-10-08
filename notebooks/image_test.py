import os
import cv2
from doclayout_yolo import YOLOv10

class ImageDetector:
    """Class to handle image detection using YOLOv10."""

    def __init__(self):
        """Initialize the detector with the pretrained YOLOv10 model."""
        filepath = "doclaymodel/doclayout_yolo_docstructbench_imgsz1024.pt"
        self.model = YOLOv10(filepath)

    def detect_and_annotate(self, image_path, output_path, imgsz=1024, conf=0.2, device="cpu"):
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


input_file = r'inputs/images/test.png'
output_dir = 'outputs/images'
def test_image_detector():
    """Test the ImageDetector class."""
    input_file = r'inputs/images/test.png'
    output_file = 'outputs/images/test_output.png'
    
    imgdet = ImageDetector()
    imgdet.detect_and_annotate(input_file, output_file)

    # Check if the output file was created
    assert os.path.exists(output_file), "Output file was not created."

test_image_detector()
