import sys
from core.pdf_loader import PDFLoader
from core.pdf_editor import PDFEditor
from core.pdf_writer import PDFWriter
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
import config


app = QApplication(sys.argv)
window = MainWindow(pdf_path=config.PDF_PATH)
window.show()
sys.exit(app.exec())
