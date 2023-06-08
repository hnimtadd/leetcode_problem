class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = {1: "1"}
        for i in range(2, n + 1):
            prev = res[i-1]
            char = prev[0]
            charCount = 1
            curr = ""
            for cChar in prev[1:]:
                if cChar == char:
                    charCount += 1
                else:
                    curr += "{}{}".format(charCount, char)
                    char = cChar
                    charCount = 1
            curr += "{}{}".format(charCount, char)
            res[i] = curr

        return res[n]


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.countAndSay(n))
