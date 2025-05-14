# Discord Chat Bot (python)

Discordでチャットボットを実装するためのシステムです。

現在開発中のため、ローカル環境での実行を情報提供します。

## 環境構築

### 必須環境

* Python 3.10 以降をインストール

### セットアップ手順

1. Python をインストール

2. リポジトリーをクローン:

   ```bash
   git clone <repository-url>
   ```

   `<repository-url>`：リポジトリのURLを入力

3. Python の仮想環境を作成:

   ```bash
   python -m venv <venv-name>
   ```

   `<venv-name>`：作成する仮想環境の名前を入力（例: venv）

4. 仮想環境をアクティブ化:

   * Windows:

     ```bash
     .\<venv-name>\Scripts\activate
     ```

     `<venv-name>`：作成した仮想環境の名前
   * macOS/Linux:

     ```bash
     source <venv-name>/bin/activate
     ```

     `<venv-name>`：作成した仮想環境の名前

5. 依存関係をインストール:

   ```bash
   pip install -r requirements.txt
   ```

6. `.env` ファイルを作成し、以下を記載:

   ```env
   DISCORD_TOKEN=set_your_bot_token
   GEMINI_API_KEY=set_your_api_key
   ```

   `set_your_bot_token`：Discord Botのトークンを入力
   `set_your_api_key`：Gemini APIキーを入力

### API キーの取得方法

* Discord Bot Token: ([https://discord.com/developers/applications](https://discord.com/developers/applications)) でアプリケーションを作成し、Bot を追加して Token を発行
* Gemini API Key: ([https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)) より発行

獲得したキーを `.env` に記載してください

---

## 開発メモ

* `requirements.txt` を生成:

  ```bash
  pip freeze > requirements.txt
  ```

* `requirements.txt` を適用:

  ```bash
  pip install -r requirements.txt
  ```

## 参考文献

* Python: ([https://discordpy.readthedocs.io/ja/stable/](https://discordpy.readthedocs.io/ja/stable/))
* Node.js: ([https://discord.js.org/docs/packages/discord.js/14.19.3](https://discord.js.org/docs/packages/discord.js/14.19.3))

---
