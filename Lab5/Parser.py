from LinkedStack import LinkedStack, StackNode

def is_op(element):
    operators = ['+', '-', '/', '*']
    return element in operators

def parser(data):
    calculator = LinkedStack()
    j = 0
    result = []
    for el in data:
        if el.isdigit():
            result.insert(j, el)
            j += 1
        elif is_op(el):
            if calculator.is_empty() or prior(calculator.get_top()) < prior(el):
                calculator.push(el)
            else:
                while not calculator.is_empty() and prior(calculator.get_top()) >= prior(el):
                    result.insert(j, calculator.get_top())
                    calculator.pop()
                    j+=1
                calculator.push(el)
        elif el == '(':
            calculator.push(el)
        elif el == ')':
            if calculator.is_empty() or calculator.get_top() == '(':
                print('Input Error')
                return
            else:
                while calculator.get_top() != '(' and not calculator.is_empty():
                    result.insert(j, calculator.get_top())
                    calculator.pop()
                    j += 1
            calculator.pop()
    while not calculator.is_empty():
        if calculator.get_top() == '(':
            print('Input error')
            return
        else:
            result.insert(j, calculator.get_top())
            calculator.pop()
            j += 1
    return result


def prior(element):
    if element == '(':
        return 1
    if element == '+':
        return 2
    if element == '*':
        return 3
    if element == '/':
        return 3
    if element == '-':
        return 2


def evaluater(data):
    S = LinkedStack()
    postfix_form = parser(list(data.strip()))
    for ch in postfix_form:
        if ch.isdigit():
            S.push(ch)
        elif is_op(ch):
            r1 = int(S.get_top())
            S.pop()
            r2 = int(S.get_top())
            S.pop()
            if ch == '+':
                S.push(r2+r1)
            if ch == '-':
                S.push(r2-r1)
            if ch == '*':
                S.push(r2*r1)
            if ch == '/':
                S.push(r2/r1)
    return S.get_top()

print(evaluater('2*(2+3)*((5*2-8)+6-2*2)'))