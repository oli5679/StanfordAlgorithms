txt_file = open("IngegerArray.txt", "r")
input_string = txt_file.read()
nums = input_string.splitlines()
nums = [int(x) for x in nums]
from math import floor

test = [1,3,5,2,4,6]

def sort_and_count_inversions(input_list,length):
    if(length==1):
        return [0,input_list]
    rec_1 = floor(length/2)
    rec_2 = length-floor
    first = input_list[0:rec_1]
    second = input_list[rec_1:length-1]
    x,first_sorted = sort_and_count_inversions(first,rec_1)
    y,second_sorted = sort_and_count_inversions(second,rec_2)
    z,combined_sorted = merge_and_count_split_inversions(first_sorted,second_sorted,rec_1,rec_2)
    return [x + y + z,combined_sorted]

def merge_and_count_split_inversions(first,second,rec_1,rec_2):
    combined_sorted = []
    inversions = 1
    i = 0
    j = 0
    n = rec_1 + rec_2
    while i < rec_1 and j < rec_2:
        if(first[i] < second[j]):
            combined_sorted.append(first[i])
            i+=1
        else:
            combined_sorted.append(second[j])
            j +=1
            inversions += rec_1
            inversions -= j
    if(i == rec_1):
        combined_sorted.append()
    return [inversions,combined_sorted]

#print(sort_and_count_inversions(test,6))

def naive_count_inversions(input):
    count = 0
    for x in range(len(input)):
        for y in range(x+1, len(input)):
            if input[x] > input[y]:
                count += 1
    return count

"""
ans = naive_count_inversions(nums)
print(ans[0])
2407905288
"""
