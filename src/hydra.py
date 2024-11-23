import copy
import random


class Head:
    def __init__(self):
        self.children = []
        self.parent = None


    def add_head(self, head: 'Head'):
        head.parent = self
        self.children.append(head)


class Hydra:
    def __init__(self):
        self.children = []
        self.parent = None

    def add_head(self, head: 'Head'):
        self.children.append(head)


def count_heads(root: Hydra):
    node = len(root.children)
    for child in root.children:
        node += count_heads(child)
    return node


def _cut_head(root: Hydra, head: Head):
    children = []
    for child in root.children:
        if child != head:
            children.append(child)
            _cut_head(child, head)
        elif child.parent is not None:
            pass

    root.children = children


def _add_branch(root: Hydra, branch: Head):
    if branch:
        root.add_head(branch)
        root.add_head(copy.deepcopy(branch))


def cut_head(root: Hydra, head: Head):
    parent = head.parent
    _cut_head(root, head)
    branch = copy.deepcopy(parent) if head.parent else None
    _add_branch(parent, branch)


def get_heads(root: Hydra):
    if len(root.children) == 0:
        return 0
    node = len(root.children)
    for child in root.children:
        node += get_heads(child)
    return node


class Randomizer:
    def __init__(self, root: Hydra):
        self.heads = []
        self._prepare(root)

    def _prepare(self, root: Hydra):
        for child in root.children:
            self.heads.append(child)
            self._prepare(child)

    def random(self):
        return random.choice(self.heads)


def get_random_head(root: Hydra):
    return Randomizer(root).random()


def count_branch(root: Hydra):
    return len(root.children)
