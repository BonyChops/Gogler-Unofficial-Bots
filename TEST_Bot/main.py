import discord

with open ("main_token.txt") as tkn:
    
    TOKEN = tkn.read() #トークンを文字列として読み込み

    #接続に必要なオブジェクト生成
    client = discord.Client()

    #起動時動作
    @client.event
    async def on_ready():
        print("TESTログイン")

    #メッセージ受信時動作
    @client.event
    async def on_message(message):
        if message.author.bot:
            return #Bot同士の無限ループ防止

        if message.content == "/happy":
            await message.channel.send(",(便乗)")

        if message.content == "/cat":
            await message.channel.send(f"{message.author.mention}" + ",にゃおん(迫真)")

        if (message.content == "/uuum") or (message.content == "thinking"):
            await message.channel.send(":thinking:")
    
        if message.content == "/smile":
            await message.channel.send(f"{message.author.mention}" + ",( ◠‿◠ )")
    
    client.run(TOKEN)