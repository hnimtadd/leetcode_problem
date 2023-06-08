class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1, n2 = len(nums1), len(nums2)
        memo = {}

        def solve(i, j):
            if i <= 0 or j <= 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if nums1[i-1] == nums2[j-1]:
                memo[(i, j)] = 1 + solve(i-1, j-1)
            else:
                memo[(i, j)] = max(solve(i-1, j), solve(i, j-1))
            return memo[(i, j)]
        return solve(n1, n2)


if __name__ == "__main__":
    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    sol = Solution()
    print(sol.maxUncrossedLines(nums1, nums2))
