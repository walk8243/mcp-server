import re

import pdfplumber

PDF_PATH = "files/rulebook.pdf"


def include_pdf():
    """
    PDFファイルを読み込んでテキストファイルに変換して保存する
    """
    try:
        # PDFドキュメントを読み込む
        with pdfplumber.open(PDF_PATH) as pdf:
            # テキストを抽出
            extracted_text = ""
            print(f"総ページ数: {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages):
                # 現在のページからテキストを抽出
                page_text = page.extract_text()

                if page_text:
                    # 複数の空白行を単一の空白行に置換
                    page_text = re.sub(r"\n\s*\n\s*\n+", "\n\n", page_text)
                    extracted_text += page_text
                    extracted_text += "\n\n"  # ページ間の区切り

        # テキストファイルとして保存
        output_path = "files/rulebook.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)

        print(f"PDFをテキストに変換しました: {output_path}")
        print(f"抽出されたテキストの長さ: {len(extracted_text)} 文字")

        return extracted_text

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None
