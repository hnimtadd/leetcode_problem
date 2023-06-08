class Solution:
    def dfs(self, graph, colors, curr, color):
        if colors[curr] != 0:
            return colors[curr] == color

        colors[curr] = color

        for neighbor in graph[curr]:
            if not self.dfs(graph, colors, neighbor, -color):
                return False

        return True

    def isBipartite(self, graph):
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] == 0:
                if not self.dfs(graph, colors, i, 1):
                    return False

        return True


if __name__ == "__main__":
    graph = [[3], [2, 4], [1], [0, 4], [1, 3]]
    sol = Solution()
    print(sol.isBipartite(graph))
