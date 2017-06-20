from math import floor
import time
from tqdm import *

#recursively sorts array by (a) left and right halves of subarray, then (b) merging these arrays.
def merge_sort(array):
    #base case
    if len(array) < 2:
        return array
    #other cases
    else:
        #(a)
        #split into first and second half 
        split_index = int(floor(len(array)/2))
        first = merge_sort(array[0:split_index])
        second = merge_sort(array[split_index:len(array)])
        #(b)
        merged = []
        i = 0
        j = 0
        #continue until one subarray is completely scanned
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1
        #add unscanned elements from other array
        merged = merged + first[i:len(first)] + second[j:len(second)]
        return merged

#same as above, also counting inversions
def merge_sort_count_inv(array):
    if len(array) < 2:
        #return 2 element array - inversions, sorted array
        return [0, array]
    else:
        split_index = int(floor(len(array)/2))
        first_count, first = merge_sort_count_inv(array[0:split_index])
        second_count, second = merge_sort_count_inv(array[split_index:len(array)])
        merged = []
        i = 0
        j = 0
        #split inversions only occur when element in j < i
        split_count = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1
                #addition to merging sub-routine. Each time j < i, each element in i will be inversion.
                split_count += (len(first) - i)
        #add unscanned elements from other array
        merged = merged + first[i:len(first)] + second[j:len(second)]
        #add inversions counted from lower recursive calls
        merged_count = first_count+second_count + split_count
        return [merged_count, merged]

def naive_count_inv(input):
    #Naive inversion count (super-slow)
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
ANS_2 = merge_sort_count_inv(NUMS)
print(ANS_2[0])

##naive (takes ages)
#ANS = naive_count_inv(NUMS)
#print(ANS)
