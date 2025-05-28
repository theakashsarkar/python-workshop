def create_queue(size_queue: int):
    lst = [-1] * size_queue
    top = -1

    def push(item):
        nonlocal top
        if top >= len(lst) - 1:
            print("Queue full")
            return
        top += 1
        lst[top] = item
    
    def pop():
        nonlocal top, lst
        if top < 0:
            print("queue empty")
            return 
        item = lst[0]
        lst = lst[1:]
        top -= 1
        return item 
    
    def show_queue():
        return lst[:top+1]
    
    return {'push': push, 'pop': pop, 'get': show_queue}

queue = create_queue(5)
queue['push'](4)
queue['push'](6)
queue['push'](6)
print(queue['pop']())
print(queue['pop']())

print(queue['get']())


