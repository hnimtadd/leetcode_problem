class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
               "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        # res = 0
        res = []
        sign = None
        lower_bound = -pow(2, 31)
        upper_bound = pow(2, 31) - 1
        s = s.lstrip(' ')
        for char in s:
            # print("read: \'{}\'".format(char))
            if char in str.keys():
                # res = 10 * res + ord(char) - ord('0')
                res.append(char)
            elif len(res) > 0 or sign is not None:
                break
            elif char == "+":
                sign = 1
            elif char == "-":
                sign = -1
            else:
                break
        res = int(''.join(res)) if len(res) else 0
        res = res*sign if sign is not None else res
        if res < lower_bound:
            return lower_bound
        elif res > upper_bound:
            return upper_bound
        else:
            return res


if __name__ == "__main__":
    num = "  +  413"
    sol = Solution()
    print(sol.myAtoi(num))
