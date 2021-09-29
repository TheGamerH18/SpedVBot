import os

from datetime import datetime
import discord
from dotenv import load_dotenv
from Routen import Routen
from threading import Thread


class Main:
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = discord.Client()

    def __init__(self, name):
        self.client.run(TOKEN)
        ct = Thread(target=data)
        ct.start()
        self.name = name

    @client.event(self.name)
    async def on_ready(self):
        print(f"{client.user} connection succesfull")

    def data(self):
        print("Initial at " + datetime.now().strftime("%d|%m|%y %H:%M"))
        while True:
            
            time.sleep(60 * 60)


if __name__ == '__main__':
    Main(__name__)
