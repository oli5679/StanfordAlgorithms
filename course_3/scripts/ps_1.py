from IPython import embed
import pandas as pd

JOBS_PATH = "../data/jobs.txt"

EDGES_PATH = "../data/edges.txt"


def calulate_cost(df, sort_col):
    sorted_df = df.copy().sort_values(by=[sort_col, "value"], ascending=[False, False])
    sorted_df["cum_time"] = sorted_df.time.cumsum()
    return (sorted_df.cum_time * sorted_df.value).sum()


def job_min():
    jobs = pd.read_csv(JOBS_PATH, sep=" ").rename(columns={"A": "value", "B": "time"})
    jobs["difference"] = jobs["value"] - jobs["time"]
    jobs["ratio"] = jobs["value"] / jobs["time"]

    val_diff_heuristic = calulate_cost(jobs, "difference")
    val_rat_heuristic = calulate_cost(jobs, "ratio")
    print(
        f"""Difference {val_diff_heuristic}
            Ratio {val_rat_heuristic}"""
    )


class Prim:
    def __init__(self, edges, start_vertex=1):
        flipped_edges = edges.rename(columns={"start": "end", "end": "start"})
        self.edges = edges.append(flipped_edges, sort=True)
        self.nodes = edges["start"].append(edges["end"]).unique()
        self.visited = [start_vertex]
        self.tot_cost = 0
        self.mst_edges = []

    def greedy_add(self):
        cand_edges = self.edges.loc[
            (self.edges["start"].isin(self.visited))
            & (~self.edges["end"].isin(self.visited))
        ]
        min_cost = cand_edges.cost.min()
        new_node = cand_edges.loc[cand_edges.cost == min_cost].head(1)
        new_edge = new_node["end"].item()
        self.visited.append(new_edge)
        self.tot_cost += min_cost
        self.mst_edges.append(new_edge)

    def find_mst(self):
        while len(self.visited) < len(self.nodes):
            self.greedy_add()


def find_mst_cost():
    edges = pd.read_csv(EDGES_PATH, sep=" ")
    p = Prim(edges)
    p.find_mst()
    print(f"tot cost {p.tot_cost}")


if __name__ == "__main__":
    job_min()

    find_mst_cost()
