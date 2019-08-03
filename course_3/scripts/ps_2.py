import pandas as pd
from IPython import embed

CLUSTERS_PATH = "../data/clustering1.txt"


class Kruskal:
    def __init__(self, edges, num_clusters):
        self.edges = edges.sort_values(by="distance")
        self.nodes = edges["from"].append(edges["to"]).unique()
        self.num_clusters = num_clusters

    def find_clusters(self):
        for i, row in self.edges.iterrows():
            if len(self.nodes) <= self.num_clusters:
                break

            from_val = row["from"]
            to_val = row["to"]
            if from_val != to_val:
                self.nodes = [node for node in self.nodes if node != from_val]

            self.edges.loc[self.edges["from"] == from_val, "from"] = to_val
            self.edges.loc[self.edges["to"] == from_val, "to"] = to_val
        return (
            self.edges.loc[self.edges["from"] != self.edges["to"]]
            .groupby(["from", "to"])["distance"]
            .min()
        )


def main():
    edges = pd.read_csv(CLUSTERS_PATH, sep=" ")
    k = Kruskal(edges, 4)
    clusters = k.find_clusters()
    print(f"clusters {clusters}")


if __name__ == "__main__":
    main()
