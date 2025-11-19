# Docker

## 使い方

### Claude Desktopへの設定方法

```json
{
  "mcpServers": {
    "docker-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",          // 標準入力を繋ぐために必須
        "--rm",        // 終了時にコンテナを削除
        "my-mcp-server" // ビルドしたイメージ名
      ]
    }
  }
}
```

## 開発者向け

### 依存関係の更新時

1. `pyproject.toml`を更新したら、以下で`requirements.txt`を再生成します。

   ```
   uv export --format requirements-txt > requirements.txt
   ```

2. pipを使う場合は、生成された`requirements.txt`から依存関係をインストールできます。

   ```
   pip install -r requirements.txt
   ```
