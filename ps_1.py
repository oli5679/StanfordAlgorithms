from math import floor
import time
from tqdm import *

def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        split = int(floor(len(array)/2))
        first = merge_sort(array[0:split])
        second = merge_sort(array[split:len(array)])
        merged = []
        i = 0
        j = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1
        merged = merged + first[i:len(first)] + second[j:len(second)]
        return merged

def merge_count_inv(array):
    if len(array) < 2:
        return [0, array]
    else:
        split = int(floor(len(array)/2))
        first_count, first = merge_count_inv(array[0:split])
        second_count, second = merge_count_inv(array[split:len(array)])
        merged = []
        i = 0
        j = 0
        split_count = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1
                split_count += (len(first) - i)
        merged = merged + first[i:len(first)] + second[j:len(second)]
        merged_count = first_count+second_count + split_count
        return [merged_count, merged]

def naive_count_inv(input):
    count = 0
    for x in tqdm(range(len(input))):
        for y in range(x+1, len(input)):
            if input[x] > input[y]:
                count += 1
    return count

#pre-processing
TXT_FILE = open("IngegerArray.txt", "r")
INPUT_STRING = TXT_FILE.read()
NUMS = [int(x) for x in INPUT_STRING.splitlines()]

#efficient inversion count
ANS_2 = merge_count_inv(NUMS)
print(ANS_2[0])

#naive (takes ages)
ANS = naive_count_inv(NUMS)
print(ANS)
