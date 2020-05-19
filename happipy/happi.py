import discord
import random
import time

with open("tokens/happi_token.txt") as tkn:
    TOKEN = tkn.read()

    client = discord.Client()

#ログイン時操作
    @client.event
    async def on_ready():
        print("ハッピッピくんログイン中…")

#メッセージ受信時動作
    @client.event
    async def on_message(message):
        l,m,n = 0,0,0
        if message.content == "!bye":
            print("送信停止中...")
            time.sleep(30)
            await message.channel.send("お騒がせしました。")
            time.sleep(30)
            print("送信停止解除")
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
                print("送信停止中...")
                time.sleep(30)
                await message.channel.send("お騒がせしました。")
                time.sleep(30)
                print("送信停止解除")
                return
            else:
                for n in range(10):
                    while n <= 0:
                        await message.channel.send("/happy")
                return
        
    client.run(TOKEN)