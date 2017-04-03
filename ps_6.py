from IPython import embed
import numpy as np
import time
from tqdm import *

txt_file = open("algo1-programming_prob-2sum.txt", "r")
input_string = txt_file.read()
nums = [int(num) for num in input_string.splitlines()]
sorted_nums = set(nums)
count = 0
for num in tqdm(range(-10000,10001)):
    two_sum = False
    print(num)
    for cand in sorted_nums:
        rem = num - cand
        if rem in sorted_nums and rem != cand:
            two_sum = True
    if(two_sum):
        count += 1
embed()
