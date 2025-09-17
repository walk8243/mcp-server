from spire.pdf import PdfDocument, PdfTextExtractor, PdfTextExtractOptions
import re

PDF_PATH = "files/rulebook.pdf"

def include_pdf():
    """
    PDFファイルを読み込んでテキストファイルに変換して保存する
    """
    try:
        # PDFドキュメントを読み込む
        pdf_document = PdfDocument()
        pdf_document.LoadFromFile(PDF_PATH)
        
        # テキスト抽出オプションを設定
        options = PdfTextExtractOptions()
        options.IsExtractAllText = True
        
        # テキストを抽出
        extracted_text = ""
        print(pdf_document.Pages.Count)
        for i in range(pdf_document.Pages.Count):
            page = pdf_document.Pages[i]
            # PdfTextExtractorのインスタンスを作成
            text_extractor = PdfTextExtractor(page)
            
            # 現在のページからテキストを抽出
            page_text = text_extractor.ExtractText(options)
            
            # Spire.PDFの警告メッセージを除去
            page_text = page_text.replace("Evaluation Warning : The document was created with Spire.PDF for Python.", "")
            # 複数の空白行を単一の空白行に置換
            page_text = re.sub(r'\n\s*\n\s*\n+', '\n\n', page_text)
            
            extracted_text += page_text
            extracted_text += "\n\n"  # ページ間の区切り
        
        # テキストファイルとして保存
        output_path = "files/rulebook.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        print(f"PDFをテキストに変換しました: {output_path}")
        print(f"抽出されたテキストの長さ: {len(extracted_text)} 文字")
        
        # PDFドキュメントを閉じる
        pdf_document.Close()
        
        return extracted_text
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None
