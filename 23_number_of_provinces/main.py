class Solution(object):
    def dfs(self, isConnected, index, colors, color):
        # print('->visit city: {}'.format(index))
        # print('curr colors', colors)
        # print('curr nodes: ', isConnected[index])
        if colors[index] != 0:
            return
        else:
            colors[index] = color
        for i, neighbor in enumerate(isConnected[index]):
            if neighbor == 1 and index != i:
                self.dfs(isConnected, i, colors, color)
        # print('<-leave city: {}'.format(index))
        return

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        colors = [0] * n
        for i in range(n):
            # print(colors)
            if colors[i] == 0:
                self.dfs(isConnected, i, colors, max(colors) + 1)
        # print(colors)
        return max(colors) if len(colors) > 0 else 0


if __name__ == "__main__":
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    sol = Solution()
    print(sol.findCircleNum(isConnected))
