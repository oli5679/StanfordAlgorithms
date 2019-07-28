import heapq
from statistics import median
from IPython import embed

TXT_FILE = open("Median.txt", "r")
INPUT_STRING = TXT_FILE.read()
NUMS = [int(num) for num in INPUT_STRING.splitlines()]
MED_SUM = 0
LOW_LIST = ["help"]
HIGH_LIST = ["help"]

for i, x in enumerate(NUMS):
    if i == 0:
        MED_SUM += x
    elif i == 1:
        MED_SUM += min(NUMS[0], NUMS[1])
        LOW_LIST[0] = min(NUMS[0], NUMS[1]) * -1
        HIGH_LIST[0] = max(NUMS[0], NUMS[1])
    else:
        highest_low = heapq.heappop(LOW_LIST) * -1
        lowest_high = heapq.heappop(HIGH_LIST)
        sorted_cands = sorted([highest_low, lowest_high, x])
        MED_SUM += sorted_cands[1]
        heapq.heappush(LOW_LIST, sorted_cands[0] * -1)
        heapq.heappush(HIGH_LIST, sorted_cands[2])
        if i % 2 == 1:
            heapq.heappush(LOW_LIST, sorted_cands[1] * -1)
        else:
            heapq.heappush(HIGH_LIST, sorted_cands[1])

print(MED_SUM % 10000)
print(MED_SUM)
