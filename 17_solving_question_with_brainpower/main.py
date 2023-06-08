class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in reversed(range(0, len(questions)-1)):
            dp[i], skip = questions[i]
            if i + skip + 1 < len(questions):
                dp[i] += dp[i+skip+1]
            dp[i] = max(dp[i], dp[i+1])
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    questions = [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]
    print(sol.mostPoints(questions))
