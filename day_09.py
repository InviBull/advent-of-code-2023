from aoc_io import fetch, run, stopwatch
import math, re


class Solution:
    def __init__(self):
        self.data = self._parse_data()
        self.length = len(self.data)

    def _parse_data(self):
        data = fetch("09", "2023").splitlines()
        return data

    @stopwatch
    def calculate_p1(self) -> int:
        p1 = 0
        return p1

    @stopwatch
    def calculate_p2(self) -> int:
        p2 = 0
        return p2


if __name__ == "__main__":
    run(Solution)
