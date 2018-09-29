from math import floor
import time
from tqdm import *

#same as above, also counting inversions
def merge_sort(array, count_inversions = False):
    '''
    Recursively sorts array by:
        (a) sorting left and right halves of subarray, then 
        (b) merging these arrays.
    
    Also added optional 'inversion counter', needed to answer question
    '''
    if len(array) < 2:
        #return 2 element array - inversions, sorted array
        return [0, array]
    else:
        split_index = int(floor(len(array)/2))
        
        if count_inversions:
            first_count, first = merge_sort(array=array[0:split_index],
                                        count_inversions=True)
            second_count, second = merge_sort(array=array[split_index:len(array)], 
                                            count_inversions=True)
        else:
            first = merge_sort(array[0:split_index])
            second = merge_sort(array[split_index:len(array)])

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
                
                if count_inversions:
                    split_count += (len(first) - i)
        
        #add unscanned elements from other array
        merged = merged + first[i:len(first)] + second[j:len(second)]
        
        
        #add inversions counted from lower recursive calls
        if count_inversions:
            merged_count = first_count + second_count + split_count
            return (merged_count, merged)

        else:
            return merged

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
ANS_2 = merge_sort(array = NUMS, count_inversions=True)
print(ANS_2[0])

##naive (takes ages)
#ANS = naive_count_inv(NUMS)
#print(ANS)
