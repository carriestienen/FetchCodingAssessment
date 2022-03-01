def createMatrix(xVals,yVals):
    matrix = []

    for y in yVals:
        curr_row = []
        for x in xVals:
            curr_row.append([x,y])
        matrix.insert(0,curr_row)

    return matrix

def getAllPts(len,min,max):
    interval = (max-min)/(len-1)

    vals = []

    n = min

    while n < max:
        vals.append(n)
        n += interval

    vals.append(max)

    return vals

def organizeCPs(pts):
    '''takes four points and returns them in a 2 dimensional array
    such that [0,0] is the top left corner, [0,1] is the top right
    [1,0] is the bottom left and [1,1] is the bottom right

    Ex. [(3,1),(1,1),(1,3),(3,3)] -> [[(1,3),(3,3)],[(1,1),(3,1)]]'''

    small_X = pts[0][0]
    small_Y = pts[0][1]

    big_X = pts[0][0]
    big_Y = pts[0][1]    

    for pt in pts:
        if pt[0] > big_X:
            big_X = pt[0]
        elif pt[0] < small_X:
            small_X = pt[0]

        if pt[1] > big_Y:
            big_Y = pt[1]
        elif pt[1] < small_Y:
            small_Y = pt[1]

    return [
        [[small_X,big_Y],[big_X,big_Y]],
        [[small_X,small_Y],[big_X,small_Y]]
    ]

def main(imageDimensions, cornerPoints):
    rowLen = imageDimensions[0]
    columnLen = imageDimensions[1]

    cornerPoints = organizeCPs(cornerPoints)

    small_X = float(cornerPoints[0][0][0])
    big_X = float(cornerPoints[0][1][0])

    small_Y = float(cornerPoints[1][0][1])
    big_Y = float(cornerPoints[0][1][1])

    xVals = getAllPts(rowLen,small_X,big_X)
    yVals = getAllPts(columnLen,small_Y,big_Y)

    matrix = createMatrix(xVals,yVals)

    return matrix