def evalRPN(tokens) :
    stack = []
    if len(tokens) == 1:
        return int(tokens[0])
    for ele in tokens:
        if ele == "+" and len(tokens) >= 2:
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(first+second)
        elif ele == "*" and len(tokens) >= 2:
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(first * second)
        elif ele == "/" and len(tokens) >= 2:
            first = int(stack.pop())
            second = int(stack.pop())
            if second // first <=0:
                stack.append(int(second/first))
            else:
                stack.append(second // first)
        elif ele == "-" and len(tokens) >= 2:
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(second - first)
        else:
            stack.append(ele)
    return stack[-1]

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))