txt_file = open("QuickSort.txt", "r")
input_string = txt_file.read()
nums = input_string.splitlines()
nums = [int(x) for x in nums]
import random
from math import floor
from statistics import median

test = [3,8,2,5,1,4,7,6]
count_var = 0


def quick_sort(A,l,r,pivot_rule):
    if(r-l<2):
        return A
    A,p = pivot_rule(A,l,r)
    A = quick_sort(A,l,p,pivot_rule)
    A = quick_sort(A,p+1,r,pivot_rule)
    return A

def pivot_first(A,l,r):
    global count_var
    count_var +=  r - l -1
    piv_val = A[l]
    i = l+1
    for j in range(l+1,r):
        if A[j]<piv_val:
            A[i],A[j]=A[j],A[i]
            i+=1
    A[l],A[i-1]=A[i-1],A[l]
    return A,i-1

def pivot_last(A,l,r):
    global count_var
    count_var +=  r - l -1
    piv_val = A[r-1]
    A[r-1],A[l]=A[l],A[r-1]
    i = l+1
    for j in range(l+1,r):
        if A[j]<piv_val:
            A[i],A[j]=A[j],A[i]
            i+=1
    A[l],A[i-1]=A[i-1],A[l]
    return A,i-1

def pivot_mid_3(A,l,r):
    global count_var
    count_var +=  r - l -1
    last = A[r-1]
    first = A[l]
    middle_index = int(l+floor((r-l-1)/2))
    middle = A[middle_index]
    if(middle == median([first,last,middle])):
        piv_val = middle
        A[middle_index],A[l]=A[l],A[middle_index]
    elif(first == median([first,last,middle])):
        piv_val = first
    else:
        piv_val = last
        A[r-1],A[l]=A[l],A[r-1]
    i = l+1
    for j in range(l+1,r):
        if A[j]<piv_val:
            A[i],A[j]=A[j],A[i]
            i+=1
    A[l],A[i-1]=A[i-1],A[l]
    return A,i-1

def test_sorting_algo_correctness(sorting_algo,num_tests,len_tests,pivot_rule):
    for x in range(num_tests):
        correct = True
        test = random.sample(range(0,len_tests),len_tests)
        if(sorting_algo(test,0,len_tests,pivot_rule) != sorted(test)):
            print(test)
            correct = False
    if(correct):
        print("Passed Test")

max_num = len(nums)
quick_sort(nums,0,max_num,pivot_mid_3)

#test_sorting_algo_correctness(quick_sort,2,20,pivot_mid_3)
#quick_sort_p1(test,0,8)
print(count_var)
