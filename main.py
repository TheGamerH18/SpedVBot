import os
import typing
import time

from datetime import datetime
import discord
from dotenv import load_dotenv
from Routen import Routen
from Api import Api
from threading import Thread

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} connection succesfull")


class Main:
    load_dotenv()

    DISCORDTOKEN = os.getenv("DISCORD_TOKEN")
    APITOKEN = os.getenv("API_TOKEN")
    SERVERIP = "https://api.sped-v.de/"

    GUILDID = os.getenv("GUILDID")
    CHANNELID = os.getenv("CHANNELID")
    ROLENAME = os.getenv("ROLENAME")

    client = discord.Client()

    def __init__(self):
        global client
        ct = Thread(target=self.data)
        ct.start()
        client.run(self.DISCORDTOKEN)

    def data(self):
        print("Initial at " + datetime.now().strftime("%d|%m|%y %H:%M"))
        api = Api(self.APITOKEN, self.SERVERIP)
        while True:
            print("start fetch")
            data = api.fetchdata("v1/kontor/0/jobs/available")
            jobs: List[Routen] = self.formatdata(data)

            for route in jobs:
                priceperkm: int = route.priceperkm()
                if priceperkm >= 150:
                    print(route.tourid)
                    print("     €/km: " + route.priceperkm)
                    print("     start: " + route.startcity)
                    print("     end: " + route.endcity)
                    print("     times: " + route.amounttodrive)
                    # role = discord.utils.get(self.client.get_guild(int(self.GUILDID)), name=str(self.ROLENAME))
                    # self.client.get_channel(int(self.CHANNELID)).send("{} {}".format(role.mention, route.tourid))

            time.sleep(60 * 60)

    def formatdata(self, dataarray) -> typing.List:
        converteddata: typing.List[Routen] = []
        for data in dataarray:
            converteddata.append(
                Routen(
                    data["value"],
                    data["id"],
                    data["source"]["city"]["country"]["shortName"],
                    data["source"]["city"]["name"],
                    data["destination"]["city"]["country"]["shortName"],
                    data["destination"]["city"]["name"],
                    data["distance"],
                    data["weight"]
                )
            )
        return converteddata


if __name__ == '__main__':
    Main()
