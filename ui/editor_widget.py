from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView

class EditorWidget(QWidget):
    def __init__(self, pdf_path=None):
        super().__init__()

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.document = QPdfDocument(self)
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.document)

        layout.addWidget(self.pdf_view)
        
        if pdf_path:
            self.show_pdf(pdf_path)

    def show_pdf(self, pdf_path):
        status = self.document.load(pdf_path)