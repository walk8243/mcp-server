class TextWriter:
    def __init__(self, text_path: str):
        self.file = open(text_path, "w", encoding="utf-8")

    def __del__(self):
        self.file.close()

    def write_text(self, text: str) -> None:
        self.file.write(text)
