from randgrid import Grid


class Solution:
    def __init__(self):
        g = Grid()
        self.target = g.target()
        self.matrix = g.generate()

    def dfs(self):
        pass

    def bfs(self):
        pass


if __name__ == '__main__':
    sol = Solution()
