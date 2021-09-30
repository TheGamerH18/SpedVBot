import json
import os
import typing
import time
import multiprocessing

from datetime import datetime
import discord
from dotenv import load_dotenv
from Routen import Routen
from CSVHandler import CSVHandler
from Api import Api
from threading import Thread

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} connection succesfull")


class Main:

    jobs = []
    csvfilehandler = CSVHandler("routen.csv")

    load_dotenv()

    maps = [5, 6, 7, 8, 14, 18, 21, 27, 11]

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
            # data = api.fetchdata("v1/kontor/0/jobs/available")
            data = json.load(open("09290912.json"))
            print("fetched")
            jobs: typing.List[Routen] = self.formatdata(data)
            filteredjobs: typing.List[Routen] = []

            print("Apply New Distances")
            pool = multiprocessing.Pool()

            pool.map(self.newdistances, range(len(self.jobs)))

            print("Start filtering")
            for route in jobs:
                priceperkm: int = route.priceperkm()
                if priceperkm >= 150:
                    filteredjobs.append(route)
                    # role = discord.utils.get(self.client.get_guild(int(self.GUILDID)), name=str(self.ROLENAME))
                    # self.client.get_channel(int(self.CHANNELID)).send("{} {}".format(role.mention, route.tourid))
            print("Found " + str(len(filteredjobs)))
            time.sleep(60 * 60)

    def newdistances(self, index):
        self.jobs[index].newdistance(self.csvfilehandler)

    def formatdata(self, dataarray) -> typing.List[Routen]:
        converteddata: typing.List[Routen] = []
        for data in dataarray:
            if data["source"]["map"]["id"] in self.maps and data["destination"]["map"]["id"] in self.maps:
                converteddata.append(
                    Routen(
                        data["value"],
                        data["id"],
                        data["source"]["city"]["country"]["shortName"],
                        data["source"]["city"]["inGameNameDictionary"][list(data["source"]["city"]["inGameNameDictionary"])[0]],
                        data["destination"]["city"]["country"]["shortName"],
                        data["destination"]["city"]["inGameNameDictionary"][list(data["destination"]["city"]["inGameNameDictionary"])[0]],
                        data["distance"],
                        data["weight"]
                    )
                )
        return converteddata


if __name__ == '__main__':
    Main()
