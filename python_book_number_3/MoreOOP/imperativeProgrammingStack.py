stackDict = {
    "stack1" : [-1] * 5,
    "stack2" : [-1] * 5
}

TopOfTheStack ={
    "stack1" : -1,
    "stack2" : -1
}

def push(stackName, item, max_size = 5):
    if TopOfTheStack[stackName] >= max_size - 1:
        print("stack overfollow")
        return False
    TopOfTheStack[stackName] += 1
    stackDict[stackName][TopOfTheStack[stackName]] = item
    return item 

def pop(stackName):
    if TopOfTheStack[stackName] < 0:
        print("stack empty")
        return None
    item = stackDict[stackName][TopOfTheStack[stackName]]
    TopOfTheStack[stackName] -= 1
    return item

def show_stack(stack_name):
    return stackDict[stack_name][:TopOfTheStack[stack_name] + 1]


push("stack1", 1)
push("stack1", 2)
push("stack1", 3)
print(f"Stack1: {show_stack('stack1')}")

push("stack2", 10)
push("stack2", 20)
print(f"Stack2: {show_stack('stack2')}")
print(f"Popped stack1: {pop('stack1')}")
print(f"Stack1: {show_stack('stack1')}")
print(f"Popped stack2: {pop('stack2')}")
print(f"Stack2: {show_stack('stack2')}")


# # List of 2 stacks
# stackList = [[], []]  # 0 -> stack1, 1 -> stack2

# def push(stack_index, item, max_size=5):
#     if len(stackList[stack_index]) >= max_size:
#         print("Stack overflow")
#         return False
#     stackList[stack_index].append(item)
#     return item

# def pop(stack_index):
#     if not stackList[stack_index]:
#         print("Stack empty")
#         return None
#     return stackList[stack_index].pop()

# def show_stack(stack_index):
#     return stackList[stack_index]

# # Test
# push(0, 1)
# push(0, 2)
# push(0, 3)
# print(f"Stack1: {show_stack(0)}")

# push(1, 10)
# push(1, 20)
# print(f"Stack2: {show_stack(1)}")
# print(f"Popped from stack1: {pop(0)}")
