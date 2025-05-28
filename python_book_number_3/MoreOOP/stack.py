def create_stack(size_stack):
    list = [-1] * size_stack
    top = -1
    def push(item):
        nonlocal top
        if top >= len(list) - 1:
            print("stack overfollow")
            return
        top += 1
        list[top] = item 

    def pop():
        nonlocal top
        if top < 0:
            print("stack empty")
            return
        item = list[top]
        top -= 1
        return item
    
    def show_stack():
        return list[:top + 1]

    return {'push': push, 'pop': pop, 'get': show_stack}    

stack1 = create_stack(5)
stack2 = create_stack(10)
stack1['push'](0)
stack1['push'](1)
stack1['push'](2)
stack1['push'](3)
stack1['push'](4)
print(stack1['get']())

stack2['push'](3)
stack2['push'](4)
stack2['push'](5)
print(f"stack2 {stack2['get']()}")

