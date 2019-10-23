class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, node):
    if(root is None):
        root = node
    else:
        if(root.val < node.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right, node)
        elif(root.val >= node.val):
            if(root.left is None):
                root.left = node
            else:
                insert(root.left, node)


def inOrder(root):
    if(root):
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


def preOrder(root):
    if(root):
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if(root):
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)


r = Node(3)
insert(r, Node(2))
insert(r, Node(1))
insert(r, Node(4))
insert(r, Node(5))
insert(r, Node(6))

# inOrder(r)
# preOrder(r)
postOrder(r)
