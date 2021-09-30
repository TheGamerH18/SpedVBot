"""
Class that holds one Tour
"""
import math
import CSVHandler


class Routen:
    specialcircle = [
        "FI",
        "RU",
        "EST"
    ]

    tourid: str

    startcountry: str
    startcity: str

    endcountry: str
    endcity: str

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

    def newdistance(self, csvfilehandler: CSVHandler.CSVHandler):
        entry = csvfilehandler.searchroute(self.startcity, self.endcity)
        if not entry == []:
            distance = entry[3]
            if not distance == 0:
               self.distance = distance
            else:
                print("start: " + self.startcity + "\nende:" + self.endcity)

    """
    Calculates the value per Kilometer using data from csv file
    """
    def priceperkm(self) -> int:
        if self.weight >= 42000:
            return self.money / ((self.distance + 1) * self.amounttodrive())
        return self.money / (self.distance + 1)

    def amounttodrive(self):
        return int(math.ceil(self.weight / 42000))
