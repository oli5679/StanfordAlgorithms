from IPython import embed
import heapq
from statistics import median

txt_file = open("Median.txt", "r")
input_string = txt_file.read()
nums = [int(num) for num in input_string.splitlines()]
#nums = nums[0:10]
med_sum = 0
low_list = ['help']
high_list = ['help']

for i, x in enumerate(nums):
    if(i == 0):
        med_sum +=x 
    elif(i == 1):
        med_sum += min(nums[0],nums[1])
        low_list[0] = min(nums[0],nums[1])*-1
        high_list[0] = max(nums[0],nums[1])
        
    else:
        highest_low = heapq.heappop(low_list)*-1
        lowest_high = heapq.heappop(high_list)
        sorted_cands = sorted([highest_low,lowest_high,x])
        med_sum += sorted_cands[1]
        heapq.heappush(low_list,sorted_cands[0]*-1)
        heapq.heappush(high_list,sorted_cands[2])
        if i % 2 == 1:
            heapq.heappush(low_list,sorted_cands[1]*-1)
        else:
            heapq.heappush(high_list,sorted_cands[1])

print(med_sum % 10000)
print(med_sum)