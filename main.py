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
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    intents.message_content = True  # メッセージ内容の受信を有効化
    intents.messages = True  # メッセージの受信を有効化
    

    
    @client.event
    async def on_ready():
        # ログ出力（元のコードのまま）
        print(f'We have logged in as {client.user}')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        servers = len(client.guilds)
        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name=f'導入されているサーバー数：{servers}'))
        content = message.content

        if 'ンァ' in content or 'んぁ' in content or 'ﾝｧ' in content or 'んあ' in content or 'ンア' in content or 'ﾝｱ' in content or 'いきそ' in content or 'イキソ' in content or 'ｲｷｿ' in content or 'それいいよ' in content or 'ソレいいよ' in content or 'KMR' in content or 'MUR' in content or 'TDN' in content or 'TON' in content or 'HTN' in content or 'DB' in content or 'TNOK' in content or 'DRVS' in content or 'NSOK' in content or 'KBTIT' in content or 'OGMM' in content or 'KYN' in content or 'NKTIDKSG' in content or 'AKYS' in content or 'TKNUC' in content or 'SGW' in content or 'ONDISK' in content or 'TRN' in content or 'KBS' in content or 'ECZN' in content or '下北沢' in content or '114514' in content or '１１４５１４' in content or 'くしろよ' in content or '810' in content or '８１０' in content or '野獣' in content or 'やじゅう' in content or 'いきすぎ' in content or 'イキスギ' in content or 'ｲｷｽｷﾞ' in content or '田所' in content or '364' in content or '３６４' in content or 'みろよ' in content or '見ろよ' in content or '191919' in content or 'いくいくいく' in content or '１９１９１９' in content or 'ますね' in content or 'マスネ' in content or 'ﾏｽﾈ' in content or 'いんむ' in content or 'いんみゅ' in content or 'インミュ' in content or '真夏' in content or 'まなつ' in content or 'おなしゃす' in content or 'オナシャス' in content or 'せんせんしゃ' in content or 'センセンシャ' in content or '菅野美穂' in content or 'カンノミホ' in content or 'かんのみほ' in content or 'でますよ' in content or '出ますよ' in content or 'くいあらためて' in content or '悔い改めて' in content or '見とけよ' in content or 'みとけよ' in content or 'まずいですよ' in content or '小並感' in content or 'ありがとナス' in content or 'ヨツンヴァイ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
        if 'いいよ' in content and 'こいよ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
        elif 'いいよ' in content and 'それ' not in content and 'ソレ' not in content:
            await message.channel.send('こいよ！')
        if 'みたいな' in content or '見たいな' in content:
            await message.channel.send('見たけりゃ見せてやるよ！（震え声）')
        if ('みて' in content or '見て' in content) and 'ない' in content:
            await message.channel.send('嘘つけ絶対見てたゾ')
        if '頭' in content and 'ますよ' in content:
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
        if 'ありますか' in content:
            await message.channel.send('ありますあります')
        if 'とかって' in content or 'やりますか' in content:
            await message.channel.send('やりますねぇ！やりますやります')
        if '痛い' in content:
            await message.channel.send('痛いですねこれは痛い（冷静）')
        if '王道' in content and ('ゆく' in content or '征く' in content):
            if 'ソープ' in content:
                await message.channel.send('（王者の風格）')
            else:
                await message.channel.send('ソープ系ですか')
        if 'じゃけん' in content and 'ましょ' in content:
            await message.channel.send('おっ、そうだな（適当）')
        if 'お' in content and 'そうだな' in content:
            await message.channel.send('あっそうだ　おいKMRァ！（唐突）')
        if 'あ' in content and 'そうだ' in content:
            await message.channel.send('おいKMRァ！（唐突）')
        if 'お' in content and 'てるか' in content:
            await message.channel.send('バッチェ冷えてますよ')
        if 'お待たせ' in content or 'おまたせ' in content:
            await message.channel.send('アイスティしかなかったんだけどいいかな？')
        if 'どういう' in content and 'が' in content and 'ですか？' in content:
            await message.channel.send('そうですねぇ...やっぱり僕は王道を征く...ソープ系ですか（王者の風格）')
        if ('丘' in content or '岡' in content) and ('の' in content or 'ノ' in content) and ('下' in content or 'した' in content):
            await message.channel.send('（これ指摘したら淫夢厨ってバレるな...）')
        if 'この' in content and ('辺' in content or 'へん' in content) and 'が' in content and ('セ' in content or 's' in content or 'S' in content):
            await message.channel.send('エロい♪')
        if 'れんなよ' in content:
            await message.channel.send('お前のことがッ！好きだったんだよ！！！')
        if 'これもう' in content and 'な' in content:
            await message.channel.send('この辺がSexy！')
        if 'エロい' in content or 'えろい' in content:
            await message.channel.send('暴れんなよ♪')
        if 'アイスティ' in content:
            await message.channel.send('これもう...わかんねぇな')
        if '多少' in content:
            await message.channel.send('まあ、多少はね？')
        if 'いいじゃん' in content and 'たろ' in content:
            await message.channel.send('すここい歌♪')
        elif 'いいじゃん' in content:
            await message.channel.send('入れたろ♪')
        if 'すここい歌' in content:
            await message.channel.send('YAJU&U！')
        if 'YAJU' in content and ('&' in content or '＆' in content) and 'U' in content or ('24歳' in content or '２４歳' in content) and '学生' in content:
            await message.channel.send('野獣先輩♪')
        if 'one one four five' in content and 'one four' in content:
            await message.channel.send('いいよ♪こいよ♪')
        if ('そうだよ' in content or 'そだよ' in content or 'そうですよ' in content) and '便乗' not in content:
            await message.channel.send('''そうだよ（便乗）
https://tenor.com/XrM8.gif''')
        if '必殺' in content and '発動' in content:
            await message.channel.send('''必殺！野獣の咆哮！
**ヌゥン！ヘッ！ヘッ！**
**ア゛ア゛ア゛ア゛ァ゛ァ゛ァ゛ァ゛**
**ア゛↑ア゛↑ア゛↑ア゛↑ア゛ア゛ア゛ァ゛ァ゛ァ゛ァ゛！！！！**
**ウ゛ア゛ア゛ア゛ア゛ア゛ア゛ァ゛ァ゛ァ゛ァ゛ァ゛ァ゛ァ！！！！！**
**フ ウ゛ウ゛ウ゛ゥ゛ゥ゛ゥ゛ン！！！！**
**フ ウ゛ゥ゛ゥ゛ゥン！！！！(大迫真)**
***（※音量注意）***
https://www.youtube.com/watch?v=A3P4J7TcAk0''')

    
    
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
