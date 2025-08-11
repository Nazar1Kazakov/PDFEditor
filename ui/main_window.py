from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ui.editor_widget import EditorWidget
from ui.toolbar import Toolbar
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self, pdf_path=None):
        super().__init__()
        self.setWindowTitle("PDFEditor")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.toolbar = Toolbar()
        layout.addWidget(self.toolbar)
        
        self.editor_widget = EditorWidget()
        if pdf_path:
            self.editor_widget.show_pdf(pdf_path)
        layout.addWidget(self.editor_widget)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

