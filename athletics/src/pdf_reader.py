import pdfplumber
from pdfplumber.ctm import CTM
from pdfplumber.page import Page

from .text_writer import TextWriter


OUTSIDE = 30

class PDFReader:
    def __init__(self, pdf_path: str, text_writer: TextWriter):
        self.pdf_path = pdf_path
        self.text_writer = text_writer

    def read_pdf(self) -> None:
        with pdfplumber.open(self.pdf_path) as pdf:
            print(f"総ページ数: {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages[25:]):
                cropped_page = page.crop((OUTSIDE, OUTSIDE, page.width - OUTSIDE, page.height - OUTSIDE))

                # 現在のページからテキストを抽出
                page_text = cropped_page.extract_text()
                page_text = self.__replace_control_characters(page_text)

                if page_text:
                    self.text_writer.write_text(page_text)

    def test_page(self) -> None:
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[25]
            # page = pdf.pages[16]
            cropped_page = page.crop((OUTSIDE, OUTSIDE, page.width - OUTSIDE, page.height - OUTSIDE))
            # page_text = cropped_page.extract_text()
            # self.text_writer.write_text(page_text)
            self._print_page_image(cropped_page)
            # self._print_page_chars(page.within_bbox((0, 0, page.width, page.height)))
            # self._print_page_rects(page)

    def _print_page_chars(self, page: Page) -> None:
        char_list = page.chars
        if char_list:
            for char in char_list:
                my_char_ctm = CTM(*char['matrix'])
                matrix = {
                    'scale_x': my_char_ctm.scale_x,
                    'scale_y': my_char_ctm.scale_y,
                    'skew_x': my_char_ctm.skew_x,
                    'skew_y': my_char_ctm.skew_y,
                    'translation_x': my_char_ctm.translation_x,
                    'translation_y': my_char_ctm.translation_y,
                    'top': char['top'],
                    'bottom': char['bottom'],
                    'left': char['x0'],
                    'right': char['x1'],
                    'fontname': char['fontname'],
                    'size': char['size'],
                    'adv': char['adv'],
                }
                self.text_writer.write_text(f"{char['text']} => {str(matrix)}\n")

    def _print_page_rects(self, page: Page) -> None:
        rect_list = page.rects
        if rect_list:
            for rect in rect_list:
                self.text_writer.write_text(f"{str(rect)}\n")

    def _print_page_image(self, page: Page) -> None:
        image = page.to_image(resolution=300)
        image.save(f"files/pages_{page.page_number}.png")

    def __replace_control_characters(self, text: str) -> str:
        """制御文字を削除する

        Args:
            text (str): 制御文字を削除するテキスト

        Returns:
            str: 制御文字が削除されたテキスト
        """
        return text.replace("\x01", "").replace("\x02", "").replace("\x03", "").replace("\x04", "").replace("\x05", "").replace("\x06", "").replace("\x07", "").replace("\x08", "")
