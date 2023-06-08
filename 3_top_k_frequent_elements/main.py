from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        num_dict, l = {}, []
        for num in nums:
            c = num_dict[num] if num in num_dict else 0
            num_dict[num] = c+1
        idx = sorted(num_dict.values(), reverse=True)[k-1]
        print(idx)
        for i in num_dict:
            if num_dict[i] < idx:
                continue
            else:
                l.append(i)
        return l


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    obj = Solution()
    print(obj.topKFrequent(nums, k))
