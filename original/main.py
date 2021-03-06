import discord
import random
import requests
import json

with open ("tokens/main_token.txt") as tkn:
    TOKEN = tkn.read() #トークンを文字列として読み込み

    #接続に必要なオブジェクト生成
    client = discord.Client()

    @client.event
    async def on_ready():
        print("TESTログイン")

    @client.event
    async def on_message(message):
        cnt = 0
        if message.content == "/happy":
            await message.channel.send(",(便乗)")

        if message.content == "/cat":
            await message.channel.send(f"{message.author.mention}" + ",にゃおん(迫真)")

        if (message.content == "/uuum") or (message.content == "thinking"):
            await message.channel.send(":thinking:")

        if message.content.find("NG") != -1:
            if (message.content.find("ING") != -1) or (message.content.find("NGO") != -1):
                return
            else:
                await message.channel.send(":ng:")

        if message.content.find("うぉい！！") != -1:
            while cnt <= 2:
                if random.randrange(30) == 3:
                    await message.channel.send(":pleading_face:")
                else:
                    await message.channel.send(":thinking:")
                cnt += 1

        if message.content == "/get point":
            #Gogler_Pointのエンドポイント(ラッパーみたい)
            endp = requests.get("https://bonychops.com/experiment/discord-police/api/getGoglerPoint.php")
            data = json.loads(endp.text) #data関数にjson内の情報をブチコ
            for member in data["data"].values():
                await message.channel.send(f'{member["name"]}は現在{member["point"]}ptです。')
    
    client.run(TOKEN)