import discord
import os
import random
from flask import Flask
from threading import Thread
import time

# Flaskのアプリケーションインスタンスを作成（gunicornが実行するWebサーバー）
app = Flask(__name__) 

# グローバルフラグ：Botが起動を試みたかを示す
bot_start_attempted = False

# -----------------
# Discord Bot本体の起動関数
# -----------------
def run_discord_bot():
    global bot_start_attempted

    # 環境変数からトークンを取得
    TOKEN = os.getenv("DISCORD_TOKEN")
    
    # 元のコードで使用されていた Intents.all() を使用
    client = discord.Client(intents=discord.Intents.all())

    # --- お友達の Bot のロジックの移植 ---
    
    @client.event
    async def on_ready():
        # ログ出力（元のコードのまま）
        print(f'We have logged in as {client.user}')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # ここから下の if/elif ロジックは元のコードから完全に移植されています
        
        # 応答メッセージが大量にあるため、処理効率を考慮し、
        # 元のコードの if, if, elif, if... の構造を可能な限り再現します。
        
        content = message.content

        # 最初の長い if ブロック
        if content == 'ンァーッ' or content == 'んぁーっ' or content == 'ﾝｧｰｯ' or content == 'んぁーっ！' or content == 'ンァーッ！' or content == 'ﾝｧｰｯ！' or content == 'ﾝｧｰｯ!' or content == 'ｱｰｲｷｿ' or 'それいいよ' in content or 'ソレいいよ' in content or 'マスネ' in content or 'ﾏｽﾈ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 2番目の if ブロック
        if content == 'いいよこいよ' or content == 'んぁー' or content == 'ンァー' or content == 'ﾝｧｰ' or content == 'ﾝｧー' or content == 'ンァｰ' or content == 'んぁｰ' or content == 'ﾝｧｰ！' or content == 'ﾝｧｰ!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 3番目の if ブロック 
        if content == '114514' or content == 'いきすぎい' or content == 'イキスギイ' or content == 'いきすぎい！' or content == 'イキスギイ！' or content == 'いきすぎ' or content == 'イキスギ' or content == 'ｲｷｽｷﾞ' or content == 'いきすぎ！' or content == 'イキスギ！' or content == 'ｲｷｽｷﾞ！' or content == 'ｲｷｽｷﾞ!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 4番目の if ブロック
        if content == '１１４５１４' or '下北沢' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 5番目の if ブロック
        if 'あくしろよ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 6番目の if ブロック
        if '頭に来ますよ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 8番目の if ブロック
        if '810' in content or '８１０' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 9番目の if ブロック
        if '野獣' in content or 'やじゅう' in content or 'いきすぎ' in content or 'イキスギ' in content or 'ｲｷｽｷﾞ' in content or '田所' in content or '364' in content or '３６４' in content or 'みろよ' in content or '見ろよ' in content or 'いんみゅ' in content or '淫夢' in content or '真夏' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 10番目の if ブロック
        if content == '191919' or content == 'いくいくいく' or content == '１９１９１９' or 'ｲｷｽｷﾞｨ' in content or 'イキスギィ' in content or 'いいよ、こいよ' in content or content == 'いいよ！こいよ！' or content == 'いいよ、こいよ！':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 11番目の if ブロック
        if 'これもうわかんね' in content:
            await message.channel.send('このへんがセクシー♪')
            
        # 12番目の if ブロック
        if content == 'エロい' or content == 'えろい':
            await message.channel.send('暴れんなよ♪')
            
        # 13番目の if ブロック
        if 'アイスティ' in content:
            await message.channel.send('これもうわかんねえな')
            
        # 14番目の if ブロック
        if '多少は' in content:
            await message.channel.send('まあ多少はね？')
            
        # 15番目の if ブロック
        if 'すここい歌' in content:
            await message.channel.send('YAJU&U！')
            
        # 16番目の if ブロック
        if content == 'YAJU' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 17番目の if ブロック
        if 'one one four five one four' in content or content == 'one one four five! one four!':
            await message.channel.send('いいよこいよ♪')

        if 'そうだよ' in content or 'そだよ' in content:
            await message.channel.send('そうだよ（便乗）')
        if 'ますね' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
    
    # --- Botの実行 ---
    if TOKEN:
        try:
            # 元のコードにあった client.run(TOKEN) のみを実行
            client.run(TOKEN)
        except Exception as e:
            print(f"Discord Bot 起動失敗: {e}")
    else:
        print("エラー: Botトークンが設定されていません。")

# -----------------
# Webサーバーのエンドポイント (gunicornがアクセスする場所)
# -----------------
@app.route('/')
def home():
    global bot_start_attempted
    
    # Botがまだ起動を試みていない場合のみ、Botを別スレッドで起動
    if not bot_start_attempted:
        print("Webアクセスを検知。Discord Botの起動を試みます...")
        bot_start_attempted = True
        
        # Botを別スレッドで起動
        Thread(target=run_discord_bot).start()
        
        return "Discord Bot is initializing..."
    
    # Bot起動試行済みの場合は、Renderのヘルスチェックに応答
    return "Bot is alive!"
