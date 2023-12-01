# https://adventofcode.com/2021/day/1
import sys
from ..common import *

number_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


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


def get_numeric(number):
    if number.isdigit():
        return number
    return number_mapping[number]


def part2(data):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(1, 10):
        nums.append(str(i))

    sum = 0
    for line in data:
        first = None
        last = None
        for num in nums:
            idx = line.find(num)
            if idx != -1 and (first is None or first['idx'] > idx):
                first = {'idx': idx, 'val': get_numeric(num)}
            idx = line.rfind(num)
            if idx != -1 and (last is None or last['idx'] < idx):
                last = {'idx': idx, 'val': get_numeric(num)}

        value = int(first['val'] + last['val'])
        sum += value
    return sum


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
