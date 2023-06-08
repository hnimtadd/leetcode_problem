class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(nums1), len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2, m, n = nums2, nums1, n, m
        l, r, h_len = 0, m, (m + n + 1)//2
        while (l <= r):
            i = (l + r) // 2
            j = h_len - i
            if i < m and nums2[j-1] > nums1[i]:
                l = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                r = i - 1
            else:
                if i == 0:
                    lnum = nums2[j-1]
                elif j == 0:
                    lnum = nums1[i-1]
                else:
                    lnum = max(nums2[j-1], nums1[i-1])
                if (m + n) % 2 == 1:
                    return lnum
                if i == m:
                    rnum = nums2[j]
                elif j == n:
                    rnum = nums1[i]
                else:
                    rnum = min(nums2[j], nums1[i])
                return (lnum+rnum) / 2.0
            # def findMedianSortedArrays(self, nums1, nums2):
            #     """
            #     :type nums1: List[int]
            #     :type nums2: List[int]
            #     :rtype: float
            #     """
            #     m, n = len(nums1), len(nums2)
            #     if m == 0 or n == 0:
            #         nums = nums1 if m != 0 else nums2
            #         if len(nums) % 2 == 0:
            #             return float(nums[int((len(nums) - 1)/2)] + nums[int((len(nums)-1)/2)+1])/2
            #         else:
            #             return nums[int(len(nums)/2)]
            #     if m > n:
            #         nums1, nums2, m, n = nums2, nums1, n, m
            #     lsize = int((m + n + 1)/2)
            #     ptr = int((m + 1) / 2)
            #     while True:
            #         if len(nums1[:ptr]) and len(nums2[lsize-ptr:]) and nums1[:ptr][-1] > nums2[lsize-ptr:][0]:
            #             ptr -= 1
            #         elif len(nums2[:lsize-ptr]) and len(nums1[ptr:]) and nums2[:lsize-ptr][-1] > nums1[ptr:][0]:
            #             ptr += 1
            #         else:
            #             if (m + n) % 2 == 0:
            #                 if len(nums2[:lsize-ptr]) and len(nums1[:ptr]):
            #                     l = max(nums2[:lsize-ptr][-1], nums1[:ptr][-1])
            #                 else:
            #                     l = nums2[:lsize -
            #                               ptr][-1] if len(nums2[:lsize-ptr]) else nums1[:ptr][-1]
            #                 if len(nums1[ptr:]) and len(nums2[lsize-ptr:]):
            #                     r = min(nums1[ptr:][0], nums2[lsize-ptr:][0])
            #                 else:
            #                     r = nums1[ptr:][0] if len(
            #                         nums1[ptr:]) else nums2[lsize-ptr:][0]
            #                 return float(l + r)/2
            #             else:
            #                 if len(nums1[:ptr]) and len(nums2[:lsize-ptr]):
            #                     l = max(nums2[:lsize-ptr][-1], nums1[:ptr][-1])
            #                 else:
            #                     l = nums2[:lsize -
            #                               ptr][-1] if len(nums2[:lsize-ptr]) else nums1[:ptr][-1]
            #                 return l


if __name__ == "__main__":
    nums1 = [2, 3]
    nums2 = [1, 4, 5]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
