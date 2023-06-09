import easyocr

class OCR:
    def __init__(self):
        self.reader = easyocr.Reader(['en']) 

    def perform_ocr(self, image):
        results = self.reader.readtext(image, detail=0, paragraph=True)  # Set detail, paragraph parameters
        extracted_text = " ".join(results)  # Join into a single string
        return extracted_text
