from aoc_io import fetch, run, stopwatch


class Solution:
    def __init__(self):
        self.data = [list(map(int, i.split())) for i in fetch("09").splitlines()]

    @stopwatch
    def calculate_p1(self) -> int:
        p1 = 0
        for d in self.data:
            while not all([i == 0 for i in d]):
                p1 += d[-1]
                d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        return p1

    @stopwatch
    def calculate_p2(self) -> int:
        p2 = 0
        for d in self.data:
            add = True
            while not all([i == 0 for i in d]):
                p2 += d[0] if add else -d[0]
                add = not add
                d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        return p2


if __name__ == "__main__":
    run(Solution)
