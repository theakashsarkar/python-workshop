# list = []

# def push(item):
#     if len(list) < 5:
#        return list.append(item)
#     print('Stack overflow')
# def pop():
#     print(list.pop())

# push(5)
# push(6)
# push(7)
# push(8)
# push(9)

# print(len(list))

list = []

def push(item):
    if len(list) < 5:
        list.append(item)

def pop():
    return list.pop(0)

push(1)
push(2)
push(3)
push(4)

print(pop())
print(pop())
print(pop())