class Solution(object):
    def solve(self, nums, k):
        '''
        [summary]: Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
        ::type
        nums: list(int)
        k: int
        ::rtype: bool
        '''
        nums = sorted(nums)
        max = sum(nums)
        for i in range(max):
            x = self.find_subset_with_sum(nums, i, [])
            print(x)
            if len(x) >= k:
                for lst in x:
                    for index in lst:
                        print(nums[index], end=" ")
                    print()
                return True
        return False

    def find_subset_with_sum(self, lst, sum, curr):
        res = []
        if sum == 0 or len(lst) == 0:
            # print(curr)
            curr = sorted(curr)
            return [curr]

        for index, val in enumerate(lst):
            if index in curr:
                continue
            if val <= sum:
                # print(val)
                res += self.find_subset_with_sum(lst[:index] + lst[index + 1:],
                                                 sum - val, curr + [index])
        return [list(x) for x in list(tuple(res))] # if len(lst) == 0 else []


if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    #
    k = 4
    # nums = sorted(nums)
    solution = Solution()
    print(solution.solve(nums, k))
    # print(nums)
    # print(solution.find_subset_with_sum(nums, 4, []))
