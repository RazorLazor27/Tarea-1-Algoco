import TESTFUNCTION as test

def initial_input(boxes):
    rotations = []
    for box in boxes:
        rotations.append([max(box[0], box[1]), min(box[0], box[1]), box[2]])
        rotations.append([max(box[0], box[2]), min(box[0], box[2]), box[1]])
        rotations.append([max(box[1], box[2]), min(box[1], box[2]), box[0]])

    return rotations

def Pregunta_1(boxes, bottom_index=-1):
    max_height = 0
    for i in range(len(boxes)):
        if bottom_index == -1 or boxes[i][0] < boxes[bottom_index][0] and boxes[i][1] < boxes[bottom_index][1]:
            height = Pregunta_1(boxes, i)
            max_height = max(max_height, height)
    max_height += boxes[bottom_index][2] if bottom_index != -1 else 0
    return max_height

def Pregunta_2(boxes, bottom_index=-1, memo={}):
    if bottom_index in memo:
        return memo[bottom_index]
    max_height = 0
    for i in range(len(boxes)):
        if bottom_index == -1 or boxes[i][0] < boxes[bottom_index][0] and boxes[i][1] < boxes[bottom_index][1]:
            height = Pregunta_2(boxes, i, memo)
            max_height = max(max_height, height)
    max_height += boxes[bottom_index][2] if bottom_index != -1 else 0
    memo[bottom_index] = max_height
    return max_height


boxes = test.data_input()
resultado = test.data_output()
for i in range(len(resultado)):

    entrada = Pregunta_1(initial_input(boxes[i]))
    if (entrada == resultado[i]):
        print("PASSED")
    else:
        print("FAILDED")