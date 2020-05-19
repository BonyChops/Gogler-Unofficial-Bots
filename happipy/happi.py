import discord
import random
import time

with open("happipy/happi_token.txt") as tkn:
    TOKEN = tkn.read()

    client = discord.Client()

    @client.event
    async def on_ready():
        print("ハッピッピくんログイン")

    @client.event
    async def on_message(message):
        l,m,n = 0,0,0
        if message.content == "!bye":
            print("!byeコマンド受信")
            time.sleep(60)
            await message.channel.send("お騒がせしました。")
            return
        elif message.content == "/happy":
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                for l in range(10):
                    while l <= 10:
                        await message.channel.send("/happy")
                return
            else:
                await message.channel.send("!5cho")
                await message.channel.send("!spc")
                for m in range(10):
                    while m <= 10:
                        await message.channel.send("/happy")
                return
        elif message.content == ("/stop"):
            if random.randrange(100) == 28:
                await message.channel.send("お騒がせしました。")
                return
            else:
                for n in range(10):
                    while n <= 0:
                        await message.channel.send("/happy")
                return
        
    client.run(TOKEN)