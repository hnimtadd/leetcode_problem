class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[r] < nums[l]:
                if nums[l] > target > nums[r]:
                    return -1
                if nums[m] <= nums[r]:
                    if nums[m] <= target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                elif nums[l] <= nums[m]:
                    if nums[l] <= target <= nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 6, 7, 8, 1, 2]
    print(sol.search(nums, 7))
    for i in nums:
        print(sol.search(nums, i))
