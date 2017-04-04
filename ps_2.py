import random
from math import floor
from statistics import median

#Count var only used to answer assignment questions. Not needed for other sorting tasks.

def quick_sort(A, l, r, pivot_rule):
    #base case
    if r-l < 2:
        return A
    else:
        #Choose pivot (several different rules) and set lower numbers below and higher above.
        A, p = pivot_rule(A, l, r)
        #Recursively sort both subarrays
        A = quick_sort(A, l, p, pivot_rule)
        A = quick_sort(A, p+1, r, pivot_rule)
        return A

def pivot_first(A, l, r):
    global COUNT_VAR
    COUNT_VAR += r - l -1
    #pivot is first value in array
    piv_val = A[l]
    #track frontier = leftmost value larger than pivot
    i = l+1
    for j in range(l+1, r):
        #loop through remaining subarray
        #if val less than pivot
        if A[j] < piv_val:
            #swap with frontier and expand frontier.
            A[i], A[j] = A[j], A[i]
            i += 1
    #swap pivot with value next to frontier.
    A[l], A[i-1] = A[i-1], A[l]
    return A, i-1

def pivot_last(A, l, r):
    global COUNT_VAR
    COUNT_VAR += r - l - 1
    #same logic as above. Pivot is last value and swapped to front.
    piv_val = A[r-1]
    A[r-1], A[l] = A[l], A[r-1]
    i = l+1
    for j in range(l+1, r):
        if A[j] < piv_val:
            A[i], A[j]=A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return A, i-1

def pivot_mid_3(A, l, r):
    global COUNT_VAR
    COUNT_VAR += r - l - 1
    #compare first, last and 'middle' values
    last = A[r-1]
    first = A[l]
    middle_index = int(l+floor((r-l-1)/2))
    middle = A[middle_index]
    if middle == median([first, last, middle]):
        #If 'middle' is median of these values, use as pivot and switch with 1st
        piv_val = middle
        A[middle_index], A[l] = A[l], A[middle_index]
    elif first == median([first, last, middle]):
        #If 'first' is median of these values, use as pivot.
        piv_val = first
    else:
        #Otherwise last must be median. Use as pivot.
        piv_val = last
        A[r-1], A[l] = A[l], A[r-1]
    #As first case
    i = l+1
    for j in range(l+1, r):
        if A[j] < piv_val:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return A, i-1

#Testing sorting algo on randomly generated lists vs python's inbuilt algorithm.
def test_sorting_algo_correctness(sorting_algo, num_tests, len_tests, pivot_rule):
    for x in range(num_tests):
        correct = True
        test = random.sample(range(0, len_tests), len_tests)
        if sorting_algo(test, 0, len_tests, pivot_rule) != sorted(test):
            print(test)
            correct = False
    if correct:
        print("Passed Test")

#Load data
TXT_FILE = open("QuickSort.txt", "r")
INPUT_STRING = TXT_FILE.read()
NUMS = INPUT_STRING.splitlines()
NUMS = [int(x) for x in NUMS]
COUNT_VAR = 0
MAX_NUM = len(NUMS)
quick_sort(NUMS, 0, MAX_NUM, pivot_mid_3)

#Commented out testing
#test_sorting_algo_correctness(quick_sort,2,20,pivot_mid_3)
print(COUNT_VAR)
