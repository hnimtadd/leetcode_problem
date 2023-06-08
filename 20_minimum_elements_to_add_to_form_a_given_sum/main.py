class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        sums = sum(nums)
        offset = goal - sums if goal > sums else sums-goal
        return offset // limit + 1 if offset % limit != 0 \
            else offset // limit


if __name__ == "__main__":
    nums = [3, 2, 6, -9, 6, -8, 0, 9, 9]
    limit = 9
    goal = 901891104
    sol = Solution()
    print(sol.minElements(nums, limit, goal))
