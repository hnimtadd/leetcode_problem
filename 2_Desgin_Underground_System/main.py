class UndergroundSystem(object):

    def __init__(self):
        self.logs = {}
        self.travel_time = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        # print('checkIn: {} {} {}'.format(id, stationName, t))
        self.logs[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, checkInTime = self.logs[id]

        key = (startStation, stationName)
        total_time, count = self.travel_time[key] if key in self.travel_time.keys() else (0,0)
        self.travel_time[key] = (total_time + t - checkInTime, count + 1)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        startStation = str(startStation)
        endStation = str(endStation)
        # print("getAverageTime: {} to {}".format(
        #     startStation, endStation
        # ))
        key = (startStation, endStation)
        if key in self.travel_time.keys():
            travel_time, count = self.travel_time[key]
            return float(travel_time) / float(count)


if __name__ == "__main__":
    cmds = [
        "checkIn",
        "checkOut",
        "getAverageTime",
        "checkIn",
        "checkOut",
        "getAverageTime",
        "checkIn",
        "checkOut",
        "getAverageTime"
    ]
    args = [
        [10, "Leyton", 3],
        [10, "Paradise", 8],
        ["Leyton", "Paradise"],
        [5, "Leyton", 10],
        [5, "Paradise", 16],
        ["Leyton", "Paradise"],
        [2, "Leyton", 21],
        [2, "Paradise", 30],
        ["Leyton", "Paradise"]
    ]
    obj = UndergroundSystem()
    for cmd, arg in zip(cmds, args):
        func_call = 'obj.'+cmd + \
            '(' + ','.join('\'' + str(a) + '\'' for a in arg) + ')'
        print(eval(func_call))
