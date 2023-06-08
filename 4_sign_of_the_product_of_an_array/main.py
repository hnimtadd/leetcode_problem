from collections import Counter


class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            else:
                sign *= int(num/abs(num))
        return sign


if __name__ == "__main__":
    nums = [-1,1,-1,1,-1]
    obj = Solution()
    print(obj.arraySign(nums))
