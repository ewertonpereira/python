class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        

    def __str__(self) -> str:
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None) -> None:
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
    
            
if __name__ == '__main__':
    # tree = BinaryTree(7)
    # tree.root.right = Node(14)
    # tree.root.left = Node(18)
    
    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left)

    tree = BinaryTree()
    n1 = Node('2')
    n2 = Node('5')
    n3 = Node('1')
    n4 = Node('6')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('*')
    n8 = Node('8')
    n9 = Node('17')
    n0 = Node('+')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n9.left = n8
    n9.right = n7
    n8.right = n7
    n7.right = n3

    tree.root = n0
    
    tree.simetric_traversal()