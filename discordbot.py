import os

import discord
import random
from dotenv.main import load_dotenv

load_dotenv()

def main():

    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'Logged on as {self.user}!')

        async def on_message(self, message):
            print(f'Message from {message.author}: {message.content}')

    token = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    lista = ["cuvant 1","cuvant 2","cuvant 3"]
    lista2 = ["cuvant 4","cuvant 5","cuvant 6"]
    lista3 = ["cuvant 7","cuvant 8","cuvant 9"]
    #damiane

    @client.event
    async def on_message(message):
        a = random.randint(0, 8)
        b = random.randint(0,14)
        if not message.author.bot and message.content in lista:
            mesaj=lista2[a]
            await message.channel.send(mesaj)
        if message.content.startswith("<"):
            taggedUser = message.content
            mesajul = lista3[b] + f'{taggedUser}'
            await message.channel.send(mesajul)



    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()