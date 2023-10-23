def max_stack_height(boxes, bottom_index=-1, memo={}):
    if bottom_index in memo:
        return memo[bottom_index]
    max_height = 0
    for i in range(len(boxes)):
        if bottom_index == -1 or boxes[i][0] < boxes[bottom_index][0] and boxes[i][1] < boxes[bottom_index][1]:
            height = max_stack_height(boxes, i, memo)
            max_height = max(max_height, height)
    max_height += boxes[bottom_index][2] if bottom_index != -1 else 0
    memo[bottom_index] = max_height
    return max_height

# Generar todas las rotaciones de las cajas
boxes = [(1, 16, 14), (13,4,8),(9,14,6), (3,8,12), (13, 13, 19), (13,15,11)]
rotations = []
for box in boxes:
    rotations.append([max(box[0], box[1]), min(box[0], box[1]), box[2]])
    rotations.append([max(box[0], box[2]), min(box[0], box[2]), box[1]])
    rotations.append([max(box[1], box[2]), min(box[1], box[2]), box[0]])

# Prueba del algoritmo
print(max_stack_height(rotations))
