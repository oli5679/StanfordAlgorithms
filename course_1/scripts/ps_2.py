import random
from math import floor
from statistics import median
import copy

FILE_PATH = "../data/QuickSort.txt"


class QuickSort:
    def __init__(self, unsorted_list, pivot_rule):
        self.list_to_sort = unsorted_list
        self.pivot_rule = pivot_rule
        self.comparisons_count = 0

    def quick_sort(self, l, r):
        """
        # Count var only used to answer assignment questions. Not needed for other sorting tasks.
        """
        # Base case. Return array.
        if r - l >= 2:
            # Choose pivot (several different rules) and set lower numbers below and higher above.
            # Returns 'pivoted' array and index of this pivot.
            pivot = self.pivot(l=l, r=r)

            # Recursively sort both subarrays
            self.quick_sort(l=l, r=pivot)

            self.quick_sort(l=pivot + 1, r=r)

    def pivot(self, l, r):
        self.comparisons_count += r - l - 1
        pivot_index, pivot_val = self.pivot_rule(self, l, r)
        # track frontier = leftmost value larger than pivot
        self.list_to_sort[pivot_index], self.list_to_sort[l] = (
            self.list_to_sort[l],
            self.list_to_sort[pivot_index],
        )
        i = l + 1
        for j in range(l + 1, r):
            # loop through remaining subarray
            # if val less than pivot
            if self.list_to_sort[j] < pivot_val:
                # swap with frontier and expand frontier.
                self.list_to_sort[i], self.list_to_sort[j] = (
                    self.list_to_sort[j],
                    self.list_to_sort[i],
                )
                i += 1
        # swap pivot with value next to frontier.
        self.list_to_sort[l], self.list_to_sort[i - 1] = (
            self.list_to_sort[i - 1],
            self.list_to_sort[l],
        )
        return i - 1


def pivot_first(self, l, r):
    return l, self.list_to_sort[l]


def pivot_last(self, l, r):
    return r - 1, self.list_to_sort[r - 1]


def pivot_mid_3(self, l, r):
    # use median of first, last and 'middle' values
    last = self.list_to_sort[r - 1]
    first = self.list_to_sort[l]
    middle_index = int(l + floor((r - l - 1) / 2))
    middle = self.list_to_sort[middle_index]
    if middle == median([first, last, middle]):
        return middle_index, middle
    elif first == median([first, last, middle]):
        return l, first
    else:
        return r - 1, last


def test_sorting_algo_correctness(num_tests, len_tests, pivot_rule):
    for _ in range(num_tests):
        test = random.sample(range(0, len_tests), len_tests)
        test_sorter = QuickSort(test, pivot_rule)
        test_sorter.quick_sort(0, len_tests)
        assert test_sorter.list_to_sort == sorted(test)


def count_comparisons(nums, pivot_fn, name, target):
    sorter_obj = QuickSort(copy.copy(nums), pivot_fn)
    sorter_obj.quick_sort(0, len(nums))
    print(f" count - {name}  {sorter_obj.comparisons_count}")

    assert sorter_obj.comparisons_count == target


def main():
    test_sorting_algo_correctness(2, 20, pivot_mid_3)
    test_sorting_algo_correctness(2, 20, pivot_last)
    test_sorting_algo_correctness(2, 20, pivot_first)

    nums = [int(x) for x in open(FILE_PATH, "r").read().splitlines()]

    for pivot_fn, name, target in [
        (pivot_first, "sorter first", 162085),
        (pivot_last, "sorter last", 164123),
        (pivot_mid_3, "sorter mid", 138382),
    ]:
        count_comparisons(nums, pivot_fn, name, target)


if __name__ == "__main__":
    main()
