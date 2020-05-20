import discord
import random
import time

with open("tokens/happi_token.txt") as tkn:
    TOKEN = tkn.read()

    client = discord.Client()

    @client.event
    async def on_ready():
        print("ハッピッピくんログイン中…"

    @client.event
    async def on_message(message):
        cnt = 0
        if message.content == "!bye":
            print("送信停止中...")
            time.sleep(60)
            await message.channel.send("お騒がせしました。")
            print("送信停止解除")
            break
        elif message.content == "/happy":
            if (random.randrange(0,40,4) % 3 == 0) or (random.randrange(0,40,4) % 3 == 1):
                while cnt <= 10:
                    await message.channel.send("/happy")
                    cnt += 1
                break

            else:
                await message.channel.send("!5cho")
                await message.channel.send("!spc")
                while cnt <= 5:
                    await message.channel.send("/happy")
                    cnt += 1
                break

        elif message.content == ("/stop"):
            if random.randrange(100) == 28:
                print("送信停止中...")
                time.sleep(60)
                await message.channel.send("お騒がせしました。")
                print("送信停止解除")
                break
            else:
                while cnt <= 10:
                    await message.channel.send("/happy")
                break
        
    client.run(TOKEN)