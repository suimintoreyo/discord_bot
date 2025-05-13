# Discord Chat Bot

ディスコードでチャットボットを実装するためのシステムです。

現在、開発中のため、ローカル環境での実行となる。

## 環境構築

言語のインストール

**1.** python をどうにかインストール

**2.** repository クローンコマンド:
```git clone <リポジトリーのURL>```

**3.** python 仮想環境作成コマンド:
```python -m venv <仮想環境名>```

**4.** 仮想環境アクティブ化コマンド:
```venv\Scripts\activate```


**5.** requirement.txt 適応コマンド:
```pip install -r requirements.txt```

**6.** .env ファイルを作成し、下記コードを記入

```
# "=" の後に Discord bot のトークンと Gemini APIキーをそれぞれセットする
DISCORD_TOKEN=set_your_bot_token
GEMINI_API_KEY=set_your_api_key
```

### envのキーの取得方法
**Discord Dvelopers** (https://discord.com/developers/applications) より Discord bot を作成し、tokenを取得する。

token を .env 環境変数ファイルへ適切な箇所へペーストする。

**Google AI Studio** (https://aistudio.google.com/app/apikey) より Gemini API key を取得する。

api key を .env 環境変数ファイルへ適切な箇所へペーストする。

<!--
discord botを下記URLより作成し、tokenを取得する。

: https://discord.com/developers/applications

gemini api keyを下記URLより取得

: https://aistudio.google.com/app/apikey


それぞれ取得キーを .env 環境変数ファイルへ適切な箇所へペーストする  
-->

## Devs memo

- requirement.txt 生成コマンド:
```pip freeze > requirements.txt```

- requirement.txt 適応コマンド:
```pip install -r requirements.txt```
### Document
**python**
discordpy document (https://discordpy.readthedocs.io/ja/stable/)

**node.js**
discord.js document (https://discord.js.org/docs/packages/discord.js/14.19.3)


---
