"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the  row of the file indicates the  entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any spaces or commas or any other punctuation marks. You can make up to 5 attempts.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
"""

from math import floor
import time

INPUT_PATH = "../data/IntegerArray.txt"


class InversionCounter:
    def __init__(self, unsorted_input):
        self.unsorted_input = unsorted_input
        self.sorted_input, self.inversion_count = self.count_inv(unsorted_input)

    def merge_count(self, list_1, list_2):
        """
        Given 2 sorted lists, count inversions, and return
        single sorted list
        """
        output = []
        # Pointers for c and d, and count of inversions
        i, j, split_inv = 0, 0, 0
        while True:
            # If all of c list added to output, append remainder
            # of d and return (no extra inversions)
            if i >= len(list_1):
                return (output + list_2[j:], split_inv)

            # If all of d list added to output, append remainder
            # of c and return (one extra inversion per
            # remaining element of c * d)
            if j >= len(list_2):
                return (
                    output + list_1[i:],
                    split_inv + (len(list_1) - i) * (len(list_2) - j),
                )

            # Else add smallest element of c and d
            # and increment pointer
            if list_1[i] < list_2[j]:
                output.append(list_1[i])
                i += 1

            # If d is smaller, add inversion for each element
            # of c remaining
            else:
                output.append(list_2[j])
                j += 1
                split_inv += len(list_1) - i

    def count_inv(self, list_to_sort):
        """
        Returns tuple, sorted list and count of inversions

        Based on:
            total inversions = left inversions + right inversions
            + split inversions
        """
        # Base case - single element with no inversions
        if len(list_to_sort) == 1:
            return (list_to_sort, 0)

        # Sort and count inversions of both 1st and 2nd half
        midpoint = len(list_to_sort) // 2
        left, left_inv = self.count_inv(list_to_sort[:midpoint])
        right, right_inv = self.count_inv(list_to_sort[midpoint:])

        # Merge together and count split inversions
        comb, split_inv = self.merge_count(left, right)
        return (comb, left_inv + right_inv + split_inv)


def main():
    # pre-processing
    unsorted_list = [int(x) for x in open(INPUT_PATH, "r").read().splitlines()]

    # efficient inversion count
    ans = InversionCounter(unsorted_list)
    print(f" Inversions: {ans.inversion_count}")

    assert ans.inversion_count == 2407905288


if __name__ == "__main__":
    main()
