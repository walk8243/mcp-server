from .pdf_reader import PDFReader
from .text_writer import TextWriter

PDF_PATH = "files/rulebook.pdf"
OUTPUT_PATH = "files/rulebook.txt"


def include_pdf():
    """
    PDFファイルを読み込んでテキストファイルに変換して保存する
    """
    text_writer = TextWriter(OUTPUT_PATH)
    pdf_reader = PDFReader(PDF_PATH, text_writer)

    # PDFドキュメントを読み込む
    pdf_reader.read_pdf()
    
    # pdf_reader.test_page()
