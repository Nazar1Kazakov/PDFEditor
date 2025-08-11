import fitz

class PDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> fitz.Document:
        return fitz.open(self.file_path)
