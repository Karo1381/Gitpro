def prefix_to_postfix(expression):
    stack =[]
    for char in
        reversed(expression):
        if char.isdigit():

            stack.append(char)
        else:operand1 =
        stack,pop()
        operand2 =
        stack.pop()
        postfix =
        operand1+operand2+char
        stack.append(postfix)
        return stack.pop()

    def postfix_to_prefix(expression):
        stack = []
        for char in
            reversed(expression):
            if char.isdigit():

                stack.append(char)
            else:
                operand1 =
            stack, pop()
            operand2 =
            stack.pop()
            prefix =
            operand1 + operand2 + char
            stack.append(prefix)
            return stack.pop()