from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit
from core.pdf_loader import PDFLoader
from core.pdf_editor import PDFEditor
from core.pdf_writer import PDFWriter
import config

class Toolbar(QWidget):
    def __init__(self):
        super().__init__()

        self.loader = PDFLoader(config.PDF_PATH)
        self.doc = self.loader.load()

        self.edit_text_button = QPushButton("Edit Text")
        self.edit_text_button.clicked.connect(self.on_edit_text_button_click)

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Введите текст для замены")

        self.save_pdf_button = QPushButton("Save File")
        self.save_pdf_button.clicked.connect(self.on_save_pdf_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        layout.addWidget(self.edit_text_button)
        layout.addWidget(self.save_pdf_button)
        self.setLayout(layout)

    def on_edit_text_button_click(self):
        new_text = self.input_text.text()  
        editor = PDFEditor(self.doc)
        editor.replace_text(
            "Sergei Cheremnykh",  
            new_text,              
            config.ROBOTO_REGULAR_PATH
        )

    def     on_save_pdf_button_click(self):
        writer = PDFWriter(self.doc)
        writer.save(config.OUTPUT_PDF_PATH)
