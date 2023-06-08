import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid):

        length = len(grid)

        if grid[0][0] == 1 or grid[length - 1][length - 1] == 1:
            return -1

        visited = set((0, 0))

        directions = [[-1, 0], [1, 0], [0, -1],
                      [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

        queue = collections.deque([(1, 0, 0)])

        while queue:

            current_distance, current_position_x, current_position_y = queue.popleft()

            if current_position_x == length - 1 and current_position_y == length - 1:
                return current_distance

            for direction in directions:

                x, y = direction

                next_position_x, next_position_y = current_position_x + x, current_position_y + y

                if 0 <= current_position_x < length and 0 <= current_position_y < length and grid[current_position_x][current_position_y] == 0 and (next_position_x, next_position_y) not in visited:

                    queue.append(
                        (current_distance + 1, next_position_x, next_position_y))
                    visited.add((next_position_x, next_position_y))

        return -1


if __name__ == "__main__":
    grid = [[0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0]]
    sol = Solution()
    print(sol.shortestPathBinaryMatrix(grid))
