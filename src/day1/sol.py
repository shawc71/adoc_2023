# https://adventofcode.com/2021/day/1
import sys
from ..common import *


def part1(data):
    sum = 0
    for line in data:
        first = ""
        last = ""
        for char in line:
            if not char.isdigit():
                continue
            if first == "":
                first = char
            last = char

        value = int(first + last)
        sum += value

    return sum


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
