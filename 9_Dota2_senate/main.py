class Solution(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        _dict = {"R": [], "D": []}
        for index, char in enumerate(senate):
            _dict[char].append(index)
        n = len(senate)

        while len(_dict["R"]) != 0 and len(_dict["D"]) != 0:
            if _dict["R"][0] < _dict["D"][0]:
                _dict["R"].append(n)
            elif _dict["R"][0] > _dict["D"][0]:
                _dict["D"].append(n)

            _dict["D"].pop(0), _dict["R"].pop(0)
            n += 1
        return "Radiant" if len(_dict["R"]) > 0 else "Dire"

        # def predictPartyVictory(self, senate):
        #     """
        #     :type senate: str
        #     :rtype: str
        #     """
        #
        #     def _find_next(senate, index, curr):
        #         str_len = len(senate)
        #         for i in range(str_len):
        #             if senate[(i+index) % str_len] != senate[index]:
        #                 return (i+index) % str_len
        #         return -1
        #
        #     def _check_win(senate):
        #         b1 = 'R' in senate
        #         b2 = 'D' in senate
        #         if b1 and b2:
        #             return ''
        #         if b1:
        #             return 'Radiant'
        #         return 'Dire'
        #     i = 0
        #     res = _check_win(senate)
        #
        #     while (res == ""):
        #         ni = _find_next(senate, i, senate[i])
        #         print('baned {}, curr: {}'.format(ni, i))
        #         print(senate)
        #         # exit()
        #         i = (i+1)
        #         senate = senate[:ni] + senate[ni+1:]
        #         if i == len(senate):
        #             i = 0
        #         res = _check_win(senate)
        #     return res


if __name__ == "__main__":
    sol = Solution()
    senate = "RDDDRRRRDRRRRDRRRRDDDRDDRRRRDDRRDDRDDDDRDDDDRDRRRDRDDDRDDRRRRRRRRRRDRDDRRRRDRRDDDRRRRDDRDRDRRRDRDDDRDDDDRRRDRDDDRDDRDRDDRDDRDRRDRDRDDRRRDRRRRRDRDDRDDRRRDRDDRDDRDDRRDDDRRDDDRDRRDRDRDDDDDDDRDDRRDDDRRRDRDRDRRRDDDRDRRDRDDRRRRDDRRRRRDDRRDRRRRDRDDDDDDDRDDRDRRDRDRDDRRRRDRDRRRRDDRDDDRDRDRRDRDRDRDRRDDRRRRRDRDRDDDDDRRRRRRRDDDRDDDDRDDRDRRDRRDRRDRDDRDDRRDRRRDRDDRDDDRDDRRDDRRDRDRDDDDDRDRDRDRRRRRRRDRRDRDDRRRDDDDDRR"
    print(sol.predictPartyVictory(senate))
