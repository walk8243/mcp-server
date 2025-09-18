import re

import pdfplumber

from .text_writer import TextWriter


class PDFReader:
    def __init__(self, pdf_path: str, text_writer: TextWriter):
        self.pdf_path = pdf_path
        self.text_writer = text_writer

    def read_pdf(self) -> None:
        with pdfplumber.open(self.pdf_path) as pdf:
            print(f"総ページ数: {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages):
                # 現在のページからテキストを抽出
                page_text = page.extract_text()

                if page_text:
                    self.text_writer.write_text(page_text)
