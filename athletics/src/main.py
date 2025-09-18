from .include import include_pdf


def main():
    print("Hello from athletics!")
    print("PDFをテキストに変換しています...")

    # PDFをテキストに変換
    try:
        include_pdf()
        print("変換が完了しました！")
    except Exception as e:
        print(f"変換に失敗しました: {str(e)}")


if __name__ == "__main__":
    main()
