from collections import Counter

def calculate_node_weight(node, dict_weights, dict_children):
    own_weight = dict_weights[node]
    child_nodes = []
    try:
        child_nodes = dict_children[node]
        child_weights = []
        for child_node in child_nodes:
            child_weights.append(calculate_node_weight(child_node, dict_weights, dict_children))

        counts = Counter(child_weights)
        for element, count in counts.items():
            if count == 1:
                print(element)
                wrong_child = child_nodes[child_weights.index(element)]
                print(wrong_child)
                own_weight = dict_weights[element]
        return own_weight + sum(child_weights)
    except KeyError:
        return own_weight



with open("testinput.txt", "r") as f:
    lines = f.read().splitlines()

# From pat 1
#first_program = "ahnofa"
first_program = "tknk"

weights = {}
children = {}

for line in lines:
    if " -> " in line:
        segments = line.split(" -> ")
        childs = segments[1].split(", ")
        parent, weight = segments[0].split(" ", 1)
        weights[parent] = int(weight.replace("(", "").replace(")", ""))
        children[parent] = childs
    else:
        parent, weight = line.split(" ", 1)
        weights[parent] = int(weight.replace("(", "").replace(")", ""))

#print(weights)
#print(children)
calculate_node_weight(first_program, weights, children)

#print(children[first_program])

