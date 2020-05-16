import discord
import random

with open("happi_token.txt") as tkn:
    TOKEN = tkn.read()

    client = discord.Client()

    @client.event
    async def on_ready():
        print("ハッピッピくんログイン")

    @client.event
    async def on_message(message):
        if message.content == "!bye":
            print("停止コマンド受信...")
        
        elif message.content == "/happy":
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                await message.channel.send("/happy")
            else :
                await message.channel.send("!5cho")
                await message.channel.send("!spc")
                await message.channel.send("/happy")
                await message.channel.send("/happy")
                await message.channel.send("/happy")
        elif message.content == ("/stop"):
            if random.randrange(100) == 28:
                pass
            else:
                await message.content.send("/happy") 
                await message.channel.send("/happy")
                await message.channel.send("/happy")
                await message.channel.send("/happy")
                await message.channel.send("/happy")
        
    client.run(TOKEN)