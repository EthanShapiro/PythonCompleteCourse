from collections import Counter


class PriorityQueue(object):
    nodes = []

    def two_lowest_priority(self):
        nodes = self.nodes[:2]
        self.nodes = self.nodes[2:]
        return nodes

    def add_node(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_frequency() > node.get_frequency():
                self.nodes.insert(i, node)
                return
        self.nodes.append(node)

    def add_initial_nodes(self, nodes):
        self.nodes = sorted(nodes, key=LeafNode.get_frequency)

    def get_length(self):
        return len(self.nodes)

    def get_first_node(self):
        return self.nodes[0]


class LeafNode(object):

    tag = "leaf"

    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def get_symbol(self):
        return self.symbol

    def get_tag(self):
        return self.tag

class InternalNode(object):

    tag = "internal"

    def __init__(self, frequency, r_child, l_child):
        self.frequency = frequency
        self.r_child = r_child
        self.l_child = l_child

    def get_frequency(self):
        return self.frequency

    def get_l_child(self):
        return self.l_child

    def get_r_child(self):
        return self.r_child

    def get_tag(self):
        return self.tag


def huffman_coding(string):
    # Count each symbol and frequency
    letter_count = dict(Counter(string))

    # Create Priority Queue
    priority_queue = PriorityQueue()

    # Create temporary array for nodes
    temp_arr = []

    # Create leaf nodes for each symbol and add to priority queue
    for k, v in letter_count.items():
        temp_arr.append(LeafNode(k, v))

    # Add all initial leaf nodes to Priority Queue
    priority_queue.add_initial_nodes(temp_arr)

    # Combine nodes until only 1 node is left
    while priority_queue.get_length() > 1:
        n_1, n_2 = priority_queue.two_lowest_priority()
        total_frequency = n_1.get_frequency() + n_2.get_frequency()
        new_node = InternalNode(total_frequency, n_1, n_2)
        priority_queue.add_node(new_node)

    # Create new dictionary
    symbols_paths = {}

    # Traverse the new tree and add symbols and paths to dictionary
    to_leaf_child(priority_queue.get_first_node(), '', symbols_paths)

    print(symbols_paths)

    # Translate tree to string
    tree_list = []
    convert_tree(priority_queue.get_first_node().get_l_child(), tree_list)
    convert_tree(priority_queue.get_first_node().get_r_child(), tree_list)

    new_string = ''.join(tree_list) + ' '

    # Convert string
    for c in string:
        new_string += symbols_paths[c]
    return new_string


def convert_tree(node, tree_string):
    # Look at tree and translate
    # 0 means internal node
    # 1 means leaf node and get character after
    if node.get_tag() == 'internal':
        tree_string += '0'
        # Check left child
        if node.get_l_child().get_tag() == 'leaf':
            tree_string += '1'
            tree_string += node.get_l_child().get_symbol()
        elif node.get_l_child().get_tag() == 'internal':
            convert_tree(node.get_l_child(), tree_string)

        # Check right child
        if node.get_r_child().get_tag() == 'leaf':
            tree_string += '1'
            tree_string += node.get_r_child().get_symbol()
        elif node.get_r_child().get_tag() == 'internal':
            convert_tree(node.get_r_child(), tree_string)



def to_leaf_child(node, path, symbols_paths):
    if node.get_tag() != "leaf":
        to_leaf_child(node.get_l_child(), path+'0', symbols_paths)
        to_leaf_child(node.get_r_child(), path+'1', symbols_paths)
    else:
        symbols_paths[node.get_symbol()] = path

test_string = 'y'*20 + 'a'*50 + 'c'*60 + 'b'*100 + 'f'*140 + 'e'*200
#test_string = 'AAAAAABCCCCCCDDEEEEE'

new_string = huffman_coding(test_string)

test_string = ''.join(format(ord(x), 'b') for x in test_string)

with open('thuffmanstring.txt', 'w') as f:
    f.write(test_string)

with open('testfile.txt', 'w') as f:
    f.write(new_string)

