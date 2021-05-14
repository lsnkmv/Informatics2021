class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    
def straight_print(node):
    if node:
        print(node.data, end='-')
        straight_print(node.left)
        straight_print(node.right)

def reverse_print(node):
    if node:
        reverse_print(node.left)
        print(node.data, end='-')
        reverse_print(node.right)   

def tail_print(node):
    if node:
        tail_print(node.left)
        tail_print(node.right)  
        print(node.data, end='-')

 
root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')
root.right.right = TreeNode('f')
print ("Обход дерева в прямом порядке:")
straight_print(root)
 
print ("\nОбход дерева в обратном порядке:")
reverse_print(root)
 
print ("\nОбход дерева в концевом порядке:")
tail_print(root)