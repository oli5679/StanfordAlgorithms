from IPython import embed

HUFF_PATH = "../data/huffman.txt"

MWIS_PATH = "../data/mwis.txt"


def main():
    huff_weights = [int(x) for x in open(HUFF_PATH, "r").read().splitlines()]
    h = Huffman(huff_weights)
    encodings = h.encode_all()
    encode_lens = [len(x) for x in encodings.values()]
    print(
        f"""min val {min(encode_lens)} 
        max val {max(encode_lens)}"""
    )

    mwis_vals = [int(x) for x in open(MWIS_PATH, "r").read().splitlines()]
    mw = Mwis(mwis_vals)
    solved_vals, _ = mw.solve()
    cands = [cand - 1 for cand in [1, 2, 3, 4, 17, 117, 517, 997]]
    print(
        f"""mwis includes {''.join([str(int((cand) in solved_vals)) for cand in cands])}"""
    )


class Mwis:
    def __init__(self, nodes):
        self.nodes = nodes
        self.mwis = [0 for x in nodes]
        self.mwis[0] = ([0], self.nodes[0])
        if self.nodes[1] > self.nodes[0]:
            self.mwis[1] = ([1], self.nodes[1])
        else:
            self.mwis[1] = ([0], self.nodes[0])

    def solve(self):
        for i in range(2, len(self.nodes)):
            cand_val = self.mwis[i - 2][1] + self.nodes[i]
            if self.mwis[i - 1][1] > cand_val:
                self.mwis[i] = self.mwis[i - 1]
            else:
                self.mwis[i] = (self.mwis[i - 2][0] + [i], cand_val)

        return self.mwis[-1]


class Huffman:
    def __init__(self, weights):
        self.nodes = sorted(zip(weights, range(len(weights))), key=lambda x: x[0])
        self.encodings = {}

    def _encode_one(self):
        first_w, first_val = self.nodes.pop(0)
        second_w, second_val = self.nodes.pop(0)
        combined = (first_w + second_w, [first_val, second_val])
        self.nodes = sorted(self.nodes + [combined])

    def traverse(self, tree, current_string):
        if type(tree) == int:
            self.encodings[tree] = current_string
        else:
            self.traverse(tree[0], current_string + "0")
            self.traverse(tree[1], current_string + "1")

    def encode_all(self):
        while len(self.nodes) > 1:
            self._encode_one()
        self.traverse(self.nodes[0][1], "")
        return self.encodings


if __name__ == "__main__":
    main()
