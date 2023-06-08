import bisect


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.top_k = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.top_k) == 0:
            self.top_k.append(val)
        elif len(self.top_k) == self.k and val > self.top_k[0]:
            i = bisect.bisect_right(self.top_k, val)
            self.top_k = self.top_k[1:i] + [val] + self.top_k[i:]
        elif len(self.top_k) < self.k:
            i = bisect.bisect_right(self.top_k, val)
            self.top_k = self.top_k[:i] + [val] + self.top_k[i:]
        return self.top_k[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == "__main__":
    k = 2
    nums = [0]
    args = [-1, 1, -2, -4, 3]
    '''
    [4,5,8,2].add(3)->(2,3,4,5,8)
    [2,3,4,5,8].add(5)->(2,3,4,5,5,8)
    [2,3,4,5,5,8].add(10)->(2,3,4,5,5,8,10)
    [2,3,4,5,5,8,10].add(9)->(2,3,4,5,5,8,9,10)
    [2,3,4,5,5,8,9,10].add(4)->(2,3,4,4,5,5,8,9,10)
    '''
    obj = KthLargest(k, nums)
    [print(obj.add(i)) for i in args]
