"""
The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values  in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y = t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.

Download the following text file: Median.txt

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting  denote the th number of the file, the th median  is defined as the median of the numbers . (So, if  is odd, then  is th smallest number among ; if  is even, then  is the th smallest number among .)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute .

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
"""

from statistics import median
import heapq
from IPython import embed
import numpy as np
import time
from tqdm import tqdm

FILE_PATH_2_SUM = "../data/algo1-programming_prob-2sum.txt"
FILE_PATH_MEDIAN = "../data/Median.txt"


class MedianMaintenence:
    def __init__(self, nums):
        self.nums = nums
        self.med_sum = 0
        self.low_list = ['placeholder']
        self.high_list = ['placeholder']

    def solve(self):
        for i, x in enumerate(self.nums):
            if i == 0:
                self.med_sum += x
            elif i == 1:
                self.med_sum += min(self.nums[0], self.nums[1])
                self.low_list[0] = min(self.nums[0], self.nums[1]) * -1
                self.high_list[0] = max(self.nums[0], self.nums[1])
            else:
                highest_low = heapq.heappop(self.low_list) * -1
                lowest_high = heapq.heappop(self.high_list)
                sorted_cands = sorted([highest_low, lowest_high, x])
                self.med_sum += sorted_cands[1]
                heapq.heappush(self.low_list, sorted_cands[0] * -1)
                heapq.heappush(self.high_list, sorted_cands[2])
                if i % 2 == 1:
                    heapq.heappush(self.low_list, sorted_cands[1] * -1)
                else:
                    heapq.heappush(self.high_list, sorted_cands[1])

        return self.med_sum


def parse_file(file_path):
    return [int(num) for num in open(file_path, "r").read().splitlines()]


class TwoSum:
    def __init__(self, nums, min_val, max_val):
        self.nums = nums
        self.min_val = min_val
        self.max_val = max_val
        self.match_count = 0
        self.hash = {}

    def count_matches(self):
        for n in tqdm(self.nums):
            for target in range(self.min_val, self.max_val):
                if self.hash.get(target - n):
                    self.match_count += 1
            self.hash[n] = 1
        return self.match_count


def main():
    two_sum_inputs = set(parse_file(FILE_PATH_2_SUM))
    ts = TwoSum(two_sum_inputs, -10, 10)
    ts_total = ts.count_matches()

    print(f"2-sum total {ts_total}")
    #assert ts_total == 427

    median_inputs = parse_file(FILE_PATH_MEDIAN)

    med_maintainer = MedianMaintenence(median_inputs)

    med_answer = med_maintainer.solve()

    print(f"mm total {med_answer}")
    print(f"mm answer {med_answer % 10000}")
    assert med_answer % 10000 == 427


if __name__ == "__main__":
    main()
