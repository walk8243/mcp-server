from .include import include_pdf


def main():
    print("Hello from athletics!")
    print("PDFをテキストに変換しています...")

    # PDFをテキストに変換
    extracted_text = include_pdf()

    if extracted_text:
        print("変換が完了しました！")
    else:
        print("変換に失敗しました。")


if __name__ == "__main__":
    main()
