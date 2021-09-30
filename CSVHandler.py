import csv
import typing

class CSVHandler:
    def __init__(self, path: str):
        self.data = []
        data = csv.reader(open(path))
        for row in data:
            self.data.append(row)

    def searchroute(self, startcity: str, endcity: str) -> typing.List:
        for entry in self.data:
            if entry[1] == startcity.lower() and entry[2] == endcity.lower() :
                return entry
            elif entry[1] == endcity.lower() and entry[2] == startcity.lower() :
                return entry
        return []