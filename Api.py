import requests


class Api:
    SERVER = ""
    APITOKEN = ""

    data = {}

    def __init__(self, apitoken, server):
        self.APITOKEN = apitoken
        self.SERVER = server

    def fetchdata(self, link):
        header = {
            "X-Api-Key": self.APITOKEN
        }
        return requests.get(self.SERVER + link, headers=header).json()
