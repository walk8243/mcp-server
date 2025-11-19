# ベースイメージ
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# 重要: 標準出力のバッファリングを無効化 (MCPの通信がスムーズになります)
ENV PYTHONUNBUFFERED=1

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY src/ src/

# 実行コマンド
# エントリーポイントを設定しておくと、docker run時に引数を渡しやすいです
ENTRYPOINT ["python", "src/server.py"]
