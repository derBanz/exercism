"""
Set task: Refactor a tree building algorithm.
Method: Reconstruct the original algorithm and optimize it.
Example: None
"""


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    if records:
        if records[0].record_id != 0:
            raise ValueError('Tree must start with id 0')
        elif records[-1].record_id != len(records) - 1:
            raise ValueError('Tree must be continuous')
    trees = []
    for j in records:
        if j.record_id == 0 and j.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
        elif j.record_id < j.parent_id:
            raise ValueError('Parent id must be lower than child id')
        elif j.record_id == j.parent_id != 0:
            raise ValueError('Tree is a cycle')
        trees.append(Node(j.record_id))
    for i in range(len(records)):
        for j in trees[1:]:
            if i == records[j.node_id].parent_id:
                trees[i].children.append(j)
    if len(trees) > 0:
        root = trees[0]
    return root
