list = []

def push(item):
    if len(list) < 5:
       return list.append(item)
    print('Stack overflow')
def pop():
    print(list.pop())

push(5)
push(6)
push(7)
push(8)
push(9)
pop()
push(10)
pop()

