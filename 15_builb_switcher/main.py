class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return math.isqrt(n)

    def find_num_divisors(self, i):
        ptr = 2
        res = 1
        while ptr * ptr <= i:
            cnt = 0
            while i % ptr == 0:
                i = i // ptr
                cnt += 1
            # print(ptr, cnt)
            res *= (cnt+1)

            ptr += 1
        if i > 1:
            res *= 2
        return res


if __name__ == "__main__":
    n = 9
    sol = Solution()
    # print(sol.find_num_divisors(n))
    print(sol.bulbSwitch(n))
