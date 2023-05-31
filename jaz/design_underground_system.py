from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.times    = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_info = self.checkins.pop(id)
        transit_time = t - checkin_info[0]

        self.times[(checkin_info[1], stationName)][1] += 1
        prev_mean = self.times[(checkin_info[1], stationName)][0]
        self.times[(checkin_info[1], stationName)][0] += ((transit_time - prev_mean) /
            self.times[(checkin_info[1], stationName)][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)][0]
