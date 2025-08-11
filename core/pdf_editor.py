import fitz  # PyMuPDF

class PDFEditor:
    def __init__(self, doc):
        self.doc = doc

    def replace_text(self, old_text, new_text, font_path, font_size=12):
        for page in self.doc:
            areas = page.search_for(old_text)
            for rect in areas:
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
                page.insert_text(
                    rect.tl,
                    new_text,
                    fontfile=font_path,
                    fontsize=12,
                    color=(0, 0, 0)
                )

