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
        m,n = 0,0
        if message.content == "!bye":
            print("!byeコマンド受信")
            time.sleep(60)
            await message.channel.send("お騒がせしました.")
        elif message.content == "/happy":
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                await message.channel.send("/happy")
            else :
                await message.channel.send("!5cho")
                await message.channel.send("!spc")
                for m in range(10):
                    while m <= 10:
                        await message.channel.send("/happy")
        elif message.content == ("/stop"):
            if random.randrange(100) == 28:
                pass
            else:
                for n in range(10):
                    while n <= 0:
                        await message.channel.send("/happy")
        
    client.run(TOKEN)