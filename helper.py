

def faces():
    yield [[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1]]
    yield [[1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1]]
    yield [[-1, -1, 1], [-1, 1, 1], [-1, 1, -1], [-1, -1, -1]]
    yield [[-1, -1, -1], [1, -1, -1], [1, -1, 1], [-1, -1, 1]]
    for segment in range(4):
        y1 = 1 + segment * 2
        y2 = 3 + segment * 2
        yield [[1, y1, 1], [1, y2, 1], [-1, y2, 1], [-1, y1, 1]]
        yield [[1, y1, -1], [1, y2, -1], [1, y2, 1], [1, y1, 1]]
        yield [[-1, y1, -1], [-1, y2, -1], [1, y2, -1], [1, y1, -1]]
        yield [[-1, y1, 1], [-1, y2, 1], [-1, y2, -1], [-1, y1, -1]]
    yield [[1, y2, 1], [1, y2, -1], [-1, y2, -1], [-1, y2, 1]]
    for segment in range(2):
        x1 = 1 + segment * 2
        x2 = 3 + segment * 2
        yield [[x1, -1, 1], [x2, -1, 1], [x2, 1, 1], [x1, 1, 1]]
        yield [[x1, -1, -1], [x2, -1, -1], [x2, -1, 1], [x1, -1, 1]]
        yield [[x1, 1, -1], [x2, 1, -1], [x2, -1, -1], [x1, -1, -1]]
        yield [[x1, 1, 1], [x2, 1, 1], [x2, 1, -1], [x1, 1, -1]]
    yield [[x2, -1, 1], [x2, -1, -1], [x2, 1, -1], [x2, 1, 1]]
