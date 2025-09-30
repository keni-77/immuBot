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
        if content == 'やりますねぇ' or content == 'ンァーッ' or content == 'んぁーっ' or content == 'ﾝｧｰｯ' or content == 'んぁーっ！' or content == 'ンァーッ！' or content == 'ﾝｧｰｯ！' or content == 'ﾝｧｰｯ!' or content == 'ｱｰｲｷｿ' or content == 'あーそれいいよ' or content == 'あーソレいいよ' or content == 'ああそれいいよ' or content == 'ああソレいいよ' or content == 'ああーそれいいよ' or content == 'ああーソレいいよ' or content == 'やりますね～' or content == 'やりますねぇ～' or content == 'やりますねえ～' or content == 'やりますね～！' or content == 'やりますねぇ～！' or content == 'やりますねえ～！' or content == 'ヤリマスネ' or content == 'ﾔﾘﾏｽﾈ' or content == 'ヤリマスネ！' or content == 'ﾔﾘﾏｽﾈ！' or content == 'ヤリマスネェ' or content == 'ﾔﾘﾏｽﾈｪ' or content == 'ヤリマスネエ' or content == 'ﾔﾘﾏｽﾈｴ' or content == 'ヤリマスネェ！' or content == 'ﾔﾘﾏｽﾈｪ！' or content == 'ﾔﾘﾏｽﾈｪ!' or content == 'ヤリマスネエ！' or content == 'ﾔﾘﾏｽﾈｴ！' or content == 'ﾔﾘﾏｽﾈｪ!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 2番目の if ブロック
        if content == 'いいよこいよ' or content == 'んぁー' or content == 'ンァー' or content == 'ﾝｧｰ' or content == 'ﾝｧー' or content == 'ンァｰ' or content == 'んぁｰ' or content == 'ﾝｧｰ！' or content == 'ﾝｧｰ!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 3番目の elif ブロック (元のコードでここだけ elif)
        elif content == '114514' or content == 'いきすぎい' or content == 'イキスギイ' or content == 'いきすぎい！' or content == 'イキスギイ！' or content == 'いきすぎ' or content == 'イキスギ' or content == 'ｲｷｽｷﾞ' or content == 'いきすぎ！' or content == 'イキスギ！' or content == 'ｲｷｽｷﾞ！' or content == 'ｲｷｽｷﾞ!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 4番目の if ブロック
        if content == '１１４５１４' or content =='下北沢' or content == '下北沢大学' or content == '下北沢大学！' or content == '下北沢大学!' or content == '下北沢大学？' or content == '下北沢大学?' or content == '下北沢！' or content == '下北沢!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 5番目の if ブロック
        if content == 'ありますねぇ' or content == 'あくしろよ':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 6番目の if ブロック
        if content == 'やりますねえ' or content == '頭に来ますよ！！' or content == '頭に来ますよ!!' or content == '頭にきますよ！！' or content == '頭にきますよ!!':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 7番目の if ブロック
        if content == 'ありますねえ':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 8番目の if ブロック
        if content == '810':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 9番目の if ブロック
        if content == '８１０' or content == '野獣先輩' or content == '野獣先輩！' or content == 'やじゅうせんぱい' or content == 'やじゅうせんぱい！' or content == 'いきすぎぃ' or content == 'いきすぎぃ！' or content == 'イキスギィ！' or content == 'ｲｷｽｷﾞｨ！' or content == '田所' or content == '田所浩二' or content == '田所浩二！' or content == '田所！' or content == 'ｲｷｽｷﾞｨ!' or content == '８１０先輩' or content == '810先輩' or content == '810先輩！' or content == '８１０先輩！' or content == '364364' or content == '３６４３６４' or content == 'みろよみろよ' or content == '見ろよ見ろよ' or content == '見ろよ、見ろよ' or content == 'みろよ、みろよ' or content == '見ろよ、見ろよ！' or content == 'みろよ、みろよ！' or content == 'いんみゅちゅう' or content == '木下先輩' or content == '淫夢' or content == '真夏の夜' or content == '真夏の夜の淫夢' or content == '淫夢厨' or content == '淫夢！' or content == '真夏の夜！' or content == '真夏の夜の淫夢！' or content == '美女と野獣' or content == '美女と野獣！' or content == '野獣！' or content == '野獣' or content == '木下先輩！':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 10番目の if ブロック
        if content == '191919' or content == 'いくいくいく' or content == '１９１９１９' or content == '木下' or content == 'ｲｷｽｷﾞｨ' or content == 'イキスギィ' or content == 'いいよ、こいよ' or content == 'いいよこいよ！'or content == 'いいよ！こいよ！'or content == 'いいよ、こいよ！' or content == 'やりますね' or content == 'やりますねぇ！' or content == 'やりますねえ！':
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
            
        # 11番目の if ブロック
        if content == 'これもうわかんねぇな' or content == 'これもうわかんねえな':
            await message.channel.send('このへんがセクシー♪')
            
        # 12番目の if ブロック
        if content == 'エロい' or content == 'えろい':
            await message.channel.send('暴れんなよ♪')
            
        # 13番目の if ブロック
        if content == 'アイスティーしかなかったけどいいかな' or content == 'アイスティしかなかったけどいいかな' or content == 'アイスティーしかなかったけどいいかな？' or content == 'アイスティしかなかったけどいいかな？':
            await message.channel.send('これもうわかんねえな')
            
        # 14番目の if ブロック
        if content == 'まあ、多少はね' or content == 'ま、多少はね' or content == 'ま、多少はね？' or content == 'まあ、多少はね？' or content == 'ま多少はね' or content == 'まあ多少はね' or content == 'ま多少はね？' or content == 'まあ多少はね？':
            await message.channel.send('お待たせ♡')
            
        # 15番目の if ブロック
        if content == 'すここい歌' or content == 'すここい歌♪':
            await message.channel.send('YAJU＆U！')
            
        # 16番目の if ブロック
        if content == 'YAJU&U' or content == 'YAJU&U!' or content == 'YAJU＆U！' or content == 'YAJU&U！' or content == 'YAJU＆U!':
            await message.channel.send('野獣先輩～♪')
            
        # 17番目の if ブロック
        if content == 'one one four five one four' or content == 'one one four five! one four!' or content == 'one one four five one four!':
            await message.channel.send('い～よ、こいよ♪')
        if (message.content.includes("Discord")):
            await message.channel.send('テスト')
            
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
