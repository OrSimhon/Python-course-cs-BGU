class Tree_node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key) + ': ' + str(self.val)

    def is_leaf(self):
        return (self.left is None) and (self.right is None)


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        """
        Return node with key, uses recursion
        :param key:
        :return:
        """

        def lookup_rec(node, key):
            if node is None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                lookup_rec(node.left, key)
            else:
                lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        """
        Insert node with key, val into tree. Use recursion
        :param key:
        :param val:
        :return:
        """

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val
            elif key<node.key:
                if node.left is None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: # key>node.key:
                if node.right is None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        if self.root is None: # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

