import pandas as pd
from IPython import embed
import numpy as np
from tqdm import tqdm

INPUT_SMALL = "../data/knapsack_1.txt"

INPUT_BIG = "../data/knapsack_big.txt"


class Knapsack:
    def __init__(self, knapsack_size, items):
        self.knapsack_size = knapsack_size
        self.items = items
        self.num_items = items.shape[0]
        self.m = np.zeros((self.num_items, knapsack_size))
        self.cache = {}

    def solve(self):
        for i in tqdm(range(1, self.num_items)):
            for j in range(self.knapsack_size):
                w_i = self.items.iloc[i].weight
                v_i = self.items.iloc[i].value
                if w_i > j:
                    self.m[i, j] = self.m[i - 1, j]
                else:
                    self.m[i, j] = max(self.m[i - 1, j], self.m[i - 1, j - w_i] + v_i)

    def solve_recursive(self, i, j):
        if self.cache.get((i, j)):
            return self.cache.get((i, j))
        else:
            if i == 0 or j == 0:
                return_val = 0
            else:
                w_i = self.items.iloc[i].weight
                v_i = self.items.iloc[i].value
                if w_i > j:
                    return_val = self.solve_recursive(i - 1, j)
                else:
                    return_val = max(
                        self.solve_recursive(i - 1, j),
                        self.solve_recursive(i - 1, j - w_i) + v_i,
                    )
            self.cache[(i, j)] = return_val
            return return_val


def parse_file(file_path):
    cand_items = pd.read_csv(file_path, sep=" ")
    knapsack_size = int(cand_items.columns[0])
    cand_items.columns = ["value", "weight"]
    return knapsack_size, cand_items


def main():
    size_small, items_small = parse_file(INPUT_SMALL)
    knap = Knapsack(knapsack_size=size_small, items=items_small)
    # knap.solve()
    # print(f"small {knap.m[-1, -1]}")

    ans_small = knap.solve_recursive(i=len(items_small) - 1, j=size_small)
    print(f"small {ans_small}")

    size_large, items_large = parse_file(INPUT_BIG)
    knap_large = Knapsack(knapsack_size=size_large, items=items_large)

    # knap_large.solve()
    # print(f"large {knap_large.m[-1, -1]}")
    size_large, items_large = parse_file(INPUT_BIG)
    knap_large = Knapsack(knapsack_size=size_large, items=items_large)

    ans_large = knap_large.solve_recursive(i=len(items_large) - 1, j=size_large)
    print(f"large {ans_large}")


if __name__ == "__main__":
    main()
