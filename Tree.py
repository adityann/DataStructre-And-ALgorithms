import ipdb
class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newnode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newnode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key


# Inorder traversal of a tree
#Left, Root, Right
def inorder(root):
    if root:
        inorder(root.getLeftChild())
        print(root.key)
        inorder(root.getRightChild())

# Preorder travesal of a tree
#Root, Left , Right


def preorder(root):
    ipdb.set_trace()
    if root:
        print(root.key)
        preorder(root.getLeftChild())
        preorder(root.getRightChild())

# Postorder traversal of a tree
#Left, Right, Root


def postorder(root):
    if root:
        postorder(root.getLeftChild())
        postorder(root.getRightChild())
        print(root.key)
