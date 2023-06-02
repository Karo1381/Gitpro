def remove_min(queue):
    stack1 = []
    stack2 = []

    from queue to stack1 while not queue.empty():
        stack1.append(queue.get())

        stack1 min_element = float('inf')
        while stack1:
            element =
            stack1.pop()
            if element <
                min_element:
                main_element = elemnt
                stack2.append(element)

                while stack2:
                    element =
                    stack2.pop()
                    if element !=
                        min_element:
                        stack1.append(element)
                        queue.put(stack1.pop())
                        return min_element