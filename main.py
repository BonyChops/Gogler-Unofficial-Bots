import discord
import requests
import json

with open ("tokens/main_token.txt") as tkn:
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
        #if message.author.bot:
        #    return 

        if message.content == "/happy":
            await message.channel.send(",(便乗)")

        if message.content == "/cat":
            await message.channel.send(f"{message.author.mention}" + ",にゃおん(迫真)")

        if (message.content == "/uuum") or (message.content == "thinking"):
            await message.channel.send(":thinking:")
    
        if message.content == "おい":
            await message.channel.send(":anger:")

        if message.content == "/get point":
            #Gogler_Pointのエンドポイント(ラッパーみたい)
            endp = requests.get("https://bonychops.com/experiment/discord-police/api/getGoglerPoint.php")
            data = json.loads(endp.text) #data関数にjson内の情報をブチコ
            for member in data["data"].values():
                await message.channel.send(f'{member["name"]}は現在{member["point"]}ptです。')
    
    client.run(TOKEN)