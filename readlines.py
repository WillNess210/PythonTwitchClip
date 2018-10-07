def getAllLinesIn(filename):
    items = []
    with open(filename, 'r') as f:
        items = [line.strip() for line in f]
    return items
