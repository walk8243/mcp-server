# Athletics MCP Server

陸上競技のルールブックの情報をRAG（Retrieval-Augmented Generation）技術を活用してMCPサーバーとして提供するプロジェクトです。

## 概要

このプロジェクトは、陸上競技の公式ルールブックに記載されている情報を構造化し、MCP（Model Context Protocol）サーバーとして提供することで、AIアシスタントが陸上競技に関する正確な情報を取得できるようにします。

## 機能

- 陸上競技のルールブックの情報をRAG化
- MCPサーバーとしての情報提供
- 陸上競技に関する質問への正確な回答

## 技術スタック

- Python 3.13+
- uv（パッケージ管理）
- MCP（Model Context Protocol）
- RAG（Retrieval-Augmented Generation）

## セットアップ

1. リポジトリをクローン
```bash
git clone https://github.com/walk8243/mcp-server.git
cd athletics
```

2. 依存関係をインストール
```bash
uv sync
```

3. サーバーを起動
```bash
uv run -m src.main
```

## 開発

### コードフォーマットとリント

プロジェクトでは以下のツールを使用してコードの品質を保っています：

#### isort（インポート文の整理）
```bash
uv run isort src/
```

#### black（コードフォーマット）
```bash
uv run black src/
```

#### flake8（リント）
```bash
uv run flake8 src/
```

### 開発時の推奨ワークフロー

1. コードを編集
2. isortでインポート文を整理
3. blackでコードをフォーマット
4. flake8でリントを実行
5. 問題がなければコミット

## 使用方法

MCPクライアントからこのサーバーに接続し、陸上競技に関する質問を行うことで、ルールブックに基づいた正確な情報を取得できます。

## 開発状況

現在開発中です。基本的なプロジェクト構造は整っており、今後以下の機能を実装予定です：

- 陸上競技ルールブックデータの取り込み
- RAGシステムの実装
- MCPサーバー機能の実装
- テストケースの追加

## ライセンス

MIT

## 貢献

プルリクエストやイシューの報告を歓迎します。
