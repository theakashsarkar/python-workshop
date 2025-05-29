stackDict = {
    "queueName1" : [-1] * 5,
    "queueName2" : [-1] * 5
}

TopOfTheStack ={
    "queueName1" : -1,
    "queueName2" : -1
}

def push(queueName, item, max_size = 5):
    if TopOfTheStack[queueName] >= max_size - 1:
        print("stack overfollow")
        return False
    TopOfTheStack[queueName] += 1
    stackDict[queueName][TopOfTheStack[queueName]] = item
    return item 

def pop(queueName):
    if TopOfTheStack[queueName] < 0:
        print("stack empty")
        return None
    item = stackDict[queueName][0]
    stackDict[queueName] = stackDict[queueName][1:]
    TopOfTheStack[queueName] -= 1
    return item


def show_stack(queueName):
    return stackDict[queueName][:TopOfTheStack[queueName] + 1]


push("queueName1", 1)
push("queueName1", 2)
push("queueName1", 3)
print(f"queueName1: {show_stack('queueName1')}")

push("queueName2", 10)
push("queueName2", 20)
print(f"queueName2: {show_stack('queueName2')}")
print(f"Popped queueName1: {pop('queueName1')}")
print(f"queueName1: {show_stack('queueName1')}")
print(f"Popped queueName2: {pop('queueName2')}")
print(f"queueName2: {show_stack('queueName2')}")

    