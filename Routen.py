"""
Class that holds one Tour
"""


class Routen:
    tourid = ""

    startcountry = ""
    startcity = ""

    endcountry = ""
    endcity = ""

    distance = 0
    usesferry = False

    def __init__(self, tourid, startcountry, startcity, endcountry, endcity, distance):
        self.tourid = tourid
        self.startcountry = startcountry
        self.startcity = startcity
        self.endcountry = endcountry
        self.endcity = endcity
        self.distance = distance
