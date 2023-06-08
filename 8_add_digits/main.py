class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        pass

    # def addDigits(self, num):
    #     """
    #     :type num: int
    #     :rtype: int
    #     """
    #     res = 0
    #     while num != 0:
    #         num, digit = divmod(num, 10)
    #         res += digit
    #     return res if 0 <= res <= 9 else self.addDigits(res)
    # def addDigits(self, num):
    #     """
    #     :type num: int
    #     :rtype: int
    #     """
    #     sNum = str(num)
    #     while len(sNum) != 1:
    #         sNum = str(sum([int(num) for num in sNum]))
    #     return int(sNum)


if __name__ == "__main__":
    sol = Solution()
    num = 387
    print(sol.addDigits(num))
