class PDFWriter:
    def __init__(self, doc):
        self.doc = doc

    def save(self, output_path: str):
        self.doc.save(output_path)
        self.doc.close()
