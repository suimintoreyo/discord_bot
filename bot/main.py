import os
import discord
import google.generativeai as genai

# 環境変数からトークンと API キーを取得
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API の設定
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Discord クライアントの設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')


@client.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author == client.user:
        return

    # ユーザーからのメッセージを Gemini API に送信
    prompt = message.content
    try:
        response = model.generate_content(prompt)
        await message.channel.send(response.text)
    except Exception as e:
        await message.channel.send("エラーが発生しました。")
        print(f"エラー: {e}")

# Discord ボットの起動
client.run(DISCORD_TOKEN)
