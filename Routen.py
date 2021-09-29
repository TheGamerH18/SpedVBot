"""
Class that holds one Tour
"""
import math


class Routen:
    specialcircle = [
        "FI",
        "RU",
        "EST"
    ]

    tourid = ""

    startcountry = ""
    startcity = ""

    endcountry = ""
    endcity = ""

    weight = 0
    money = 0
    distance = 0
    usesferry = False

    def __init__(self, money, tourid, startcountry, startcity, endcountry, endcity, distance, weight):
        self.money = money
        self.tourid = tourid
        self.startcountry = startcountry
        self.startcity = startcity
        self.endcountry = endcountry
        self.endcity = endcity
        self.distance = distance
        self.weight = weight

    def priceperkm(self):
        if self.distance > 1500:
            if self.startcountry in self.specialcircle and self.endcountry not in self.specialcircle:
                self.distance -= 1500
            elif self.endcountry in self.specialcircle and self.startcountry not in self.specialcircle:
                self.distance -= 1500

        if self.weight >= 42000:
            return self.money / ((self.distance + 1) * self.amounttodrive())
        return self.money / (self.distance + 1)

    def amounttodrive(self):
        return int(math.ceil(self.weight / 42000))
