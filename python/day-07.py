# Day 7 - Handy Haversacks
# Part One and Two

# Note: I'm adapting a solution using networkx from this post: https://nopaste.ml/?l=py#XQAAAQB9BAAAAAAAAAA0m0pnuFI8c+p2+Rz3XuIPf73C+fYxki2ikt/yQjfa7TF3Zexo+Yr41QhE1nsMeP+K4A9ZosurnrDxbYkWsymSklsHCJ0D1jsxi0WVCwv7n/jZcxuR2Bh/91mKylSdjf64bqPH1QpdNPptljb/U9enWdBgILy8J4ScwuIaHEAPPHQwN9F1XFaQBNuCpxhBLwOKzZwJvc8HhbxsbOcZk2XgFI3YxgbL7Q/mImbPdSANg1+atwpgVGFkJLb6HcQl4Q4k2KcugEA0jXBjU78zp97GcUF05NftR2y27uLfKJ2G0zxOwvjwETD7m3vv3kp61jyTzNmWbfjOXYnHsdjhvRC7JmDhUzJwsSZnr99e15zYSNG2Vlkog8ZyzXLCPMe3o+zG/8+nzzCMVCSktedHDh48dZRozm6/ux+CkwN/ZMjmfATrFhFNRIzBBCU/gHcp7Q6IHipNhh8tchOXD/P91iAMkiv9/549YsyOM6vgRSZBYS/GBxrvTmruf1353DqVcxxwzbMdtpY0/e2g9RRZe9co6ORIoy1PQMr7LAQvhb0MdRjlpLzkbREaRaGSyxN8RvWsYf82XboZbHr8BliSsJ3tmzWjOD8ARBIeZhV4BiDPHZ7A0OV4O7/vHydP45WifdyMJrw2sC9vOfEgH/6ZVgs=

import re
import networkx as nx
import networkx.algorithms as nxa

def load_data(f = 'full'):
    if f == 'full':
        with open("../data/day-7.txt", "r") as fp:
            lines=fp.readlines()
    elif f == 'test':
        with open("../data/day-7-test.txt", "r") as fp:
            lines=fp.readlines()
    else:
        lines = []
    return lines

def get_graph(data):
    # Initialise the network/graph
    G = nx.DiGraph()

    # Regex
    NODE_REGEX = r'(^\w+ \w+)'
    VERTEX_REGEX = r'(\d+) (\w+ \w+)'

    # Go through the input line by line
    for line in data:
        # Find nodes (n) and vertex/edges (v)
        n = re.search(NODE_REGEX, line)
        v = re.findall(VERTEX_REGEX, line)

        # if the node doesn't exist in the graph yet, add it
        if n[0] not in G.nodes:
            G.add_node(n[0])

        # if the bag can contain other bags, then add each one as an edge
        # add the number of bags as a weight to the graph
        if len(v) > 0:
            for each in v:
                inner_bag = each[1]
                w = int(each[0]) # weights should be an integer
                if inner_bag not in G.nodes:
                    # add the node if it doesn't exist
                    G.add_node(inner_bag)

                # add the edge to the graph (syntax: edge, node, weight)
                G.add_edge(inner_bag, n[0], weight=w)
    return G

def get_sum(H, node):
    # Recursive function to get the product of all weights (for the bags going inside one another)
    return sum(H[node][n]['weight'] * get_sum(H, n) for n in H.neighbors(node)) + 1


def part_one(data):
    G = get_graph(data)
    bags = len(nxa.dfs_tree(G, "shiny gold").nodes) - 1
    print('Bags containing shiny gold:', bags)

def part_two(data):
    H = get_graph(data).reverse()
    bags = get_sum(H, 'shiny gold') - 1 # -1 is to not include the shiny gold itself
    print('Total bags inside a shiny gold:', bags)


def main():
    data = load_data('full')
    part_one(data)
    part_two(data)

if __name__ == '__main__':
    main()