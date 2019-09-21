import pandas as pd
import math
from tqdm import tqdm
import numpy as np

INPUT_PATH = "../data/tsp.txt"

import logging

logging.basicConfig(level=logging.INFO)



def main():
    city_coords = pd.read_csv(INPUT_PATH, sep=" ")
    #city_coords = city_coords.head(21)
    tsp = TSP(city_coords)
    dist, path = tsp.solve()
    print(f"min tsp distance {dist} using path {path}")


class TSP:
    def __init__(self, city_coords, start_node = 0):
        self.city_coords = city_coords
        self.city_num = city_coords.shape[0]
        self.distance_matrix = np.zeros((self.city_num, self.city_num))
        for i, start in city_coords.iterrows():
            x_start = start["x"]
            y_start = start["y"]
            for j, end in city_coords.iterrows():
                x_end = end["x"]
                y_end = end["y"]
                self.distance_matrix[i, j] = self.city_distance(
                    x_start, y_start, x_end, y_end
                )
        self.start_node = start_node
        self.tour_cache = {}

    def city_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def shortest_tour(self, tour, end):

        tour_key = (tour, end)
        if self.tour_cache.get(tour_key):
            return self.tour_cache.get(tour_key)
        else:
            if len(tour) == 1:
                    tour_len, tour_path = (self.distance_matrix[self.start_node, end], tour)
            else:
                tour_len, tour_path = 1e20, None
                before = tuple([x for x in tour if x != end])

                for node in before:
                    subtour_dist, subtour_path = self.shortest_tour(before, node)
                    cand = subtour_dist + self.distance_matrix[node, end]
                    if cand < tour_len:
                        tour_len = cand
                        tour_path = subtour_path + (end,)

            self.tour_cache[tour_key] = (tour_len, tour_path)
            return (tour_len, tour_path)

    def solve(self):
        min_tour, min_path = 1e20, None
        for tour_end in tqdm(range(0, self.city_num)):
            if tour_end != self.start_node:
                cand, cand_path = self.shortest_tour(
                    tuple([x for x in range(0, self.city_num) if x != tour_end and x != self.start_node]), tour_end
                )
                if cand < min_tour:
                    min_tour = cand
                    min_path = cand_path
        return min_tour, min_path


if __name__ == "__main__":
    main()
