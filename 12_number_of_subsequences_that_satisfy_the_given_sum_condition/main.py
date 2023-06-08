from bisect import bisect_right


class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        res = 0
        mod = 10**9 + 7
        while (left <= right):
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right-left, mod)
                left += 1
        return res % mod


if __name__ == "__main__":
    nums = [2, 3, 3, 4, 6, 7]
    target = 12
    sol = Solution()
    print(sol.numSubseq(nums, target))
