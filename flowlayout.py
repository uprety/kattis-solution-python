def getWidthHeight(width, rectangles):
    rows_width = [rectangles[0][0]] # List of width of each row 
    rows_height = [rectangles[0][1]] # List of highest height of each row 
    current_row_index = 0
    for rec in rectangles[1:]:
        x, y = rec[0], rec[1]
        if x + rows_width[current_row_index] <= width:
            rows_height[current_row_index] = max(rows_height[current_row_index], y)
            rows_width[current_row_index] += x
        else:
            current_row_index += 1
            rows_width.append(x)
            rows_height.append(y)

    print(max(rows_width), 'x', sum(rows_height))


while True:
    given_width = int(input())
    if not given_width:
        break
    rectangles = []
    rectangle = list(map(int, input().split()))
    while rectangle != [-1, -1]:
        rectangles.append(rectangle)
        rectangle = list(map(int, input().split()))
    getWidthHeight(given_width, rectangles)
