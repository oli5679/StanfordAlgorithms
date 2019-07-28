from IPython import embed
import numpy as np
import time
from tqdm import *

TXT_FILE = open("algo1-programming_prob-2sum.txt", "r")
INPUT_STRING = TXT_FILE.read()
NUMS = set([int(num) for num in INPUT_STRING.splitlines()])
COUNT = 0
for num in tqdm(range(-10000, 10001)):
    for cand in NUMS:
        rem = num - cand
        if rem in NUMS and rem != cand:
            COUNT += 1
            break
print(COUNT)
embed()
