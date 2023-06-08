class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        a_length = len(mat)
        res = 0

        for i in range(a_length):
            res += mat[i][i]
            res += mat[a_length - i - 1][i]

        if a_length % 2 == 1:
            res -= mat[a_length//2][a_length//2]

        return res

        return 1


if __name__ == "__main__":
    mat = [[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]]
    sol = Solution()
    print(sol.diagonalSum(mat))
