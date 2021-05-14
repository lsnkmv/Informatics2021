class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

def tail_print(node, res):
    if node:
        tail_print(node.left, res)
        tail_print(node.right, res)  
        res.append(str(node.data))

def is_op(element):
    operators = ['+', '-', '/', '*']
    return element in operators

operators = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '-': lambda a, b: a - b,
    '^': lambda a, b: a ** b,
}

def evaluater(expr):
    number_stack = []

    for e in expr:
        if e in operators:
            op = operators[e]
            a = int(number_stack.pop())
            b = int(number_stack.pop())
            res = op(b, a)
            number_stack.append(res)
        else:
            number_stack.append(e)

    return number_stack[0]

root = TreeNode('/')
root.left = TreeNode('*')
root.right = TreeNode('3')
root.left.left = TreeNode('+')
root.left.right = TreeNode('-')
root.left.left.left = TreeNode('2')
root.left.left.right = TreeNode('3')
root.left.right.left = TreeNode('7')
root.left.right.right = TreeNode('4')

print ("\n Решение выражения с помощью обхода дерева в концевом порядке:")
result = []
tail_print(root, result)

print(evaluater(result))
