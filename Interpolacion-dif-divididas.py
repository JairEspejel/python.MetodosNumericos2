def readPointValue(index):
    value = input('Digite el valor de x%i,y%i: ' % (index, index))
    return [float(x) for x in value.split(',')]


def readTablePoints(totalPoints):
    points = []
    print('Ingresa los valores de la tabla con el formato: xi,yi')
    for index in range(totalPoints):
        points.append(readPointValue(index))
    return points


def printTable(totalPoints, points):
    for index in range(totalPoints):
        print('x%i ' % (index), end='')
        print(points[index])


def fixPointsValue(points):
    pointsCopy = points.copy()
    pointsIndex = input(
        'Digita los indices separados por comas de los valores a modificar, ej: "0,2,4": ').split(',')
    pointsIndex = [int(x) for x in pointsIndex]
    for pointIndex in pointsIndex:
        pointsCopy[pointIndex] = readPointValue(pointIndex)
    return pointsCopy


def takeXValue(point):
    return point[0]


def sortPoints(points):
    pointsCopy = points.copy()
    pointsCopy.sort(key=takeXValue)
    return pointsCopy


def isinterpolatePointValid(orderedPoints, point):
    if point < orderedPoints[0][0] or point > orderedPoints[len(orderedPoints)-1][0]:
        print('El punto x=%f es inválido.' % point)
        return False
    return True


def getDifferenceTable(points, degree):
    differenceTable = points.copy()
    for i in range(degree):
        for j in range(degree - i):
            differenceTable[j].append(
                (
                    differenceTable[j+1][i+1] -
                    differenceTable[j][i+1]
                )/(
                    differenceTable[j+i+1][0] -
                    differenceTable[j][0]
                )
            )
    return differenceTable


def getpolynomial(differencesTable, degree, interpolateValue):
    print('P%i(x) = ' % degree, end='')
    fx = 0
    for index in range(degree + 1):
        productValue = differencesTable[0][index+1]
        if differencesTable[0][index+1] >= 0 and index > 0:
            print('+', end='')
        print('%0.4f' % differencesTable[0][index+1], end='')
        for polynomialDegree in range(index):
            auxValue = differencesTable[polynomialDegree][0]
            differenceStr = '(x-%0.4f)' % auxValue
            if auxValue < 0:
                differenceStr = '(x+%0.4f)' % abs(auxValue)
            print(differenceStr, end=' ' if polynomialDegree == index-1 else '')
            productValue *= interpolateValue - auxValue
        fx += productValue
    return fx


def main():
    points = []
    differencesTable = []
    totalPoints = 0
    degree = 0

    totalPoints = int(input('Escribe la cantidad de puntos a ingresar: '))
    points = readTablePoints(totalPoints)
    printTable(totalPoints, points)
    if input('Los valores son correctos? s = si, n = no: ') == 'n':
        print('Actualizando datos de la tabla.')
        points = fixPointsValue(points)
        printTable(totalPoints, points)
    points = sortPoints(points)
    print('')
    print('Puntos ordenados:')
    printTable(totalPoints, points)
    isPointValid = False
    while not isPointValid:
        interpolatePoint = float(input('Ingrese el punto a interpolar x = '))
        isPointValid = isinterpolatePointValid(points, interpolatePoint)
    isDegreeValid = False
    while not isDegreeValid:
        degree = int(input('Ingrese el grado de la ecuación: '))
        isDegreeValid = True
        if degree + 1 > len(points):
            isDegreeValid = False
            print('El grado (%d) ingresado es incorrecto' % degree)
    differencesTable = getDifferenceTable(points, degree)
    print('')
    print('Tabla de Diferencias divididas')
    printTable(totalPoints, differencesTable)
    result = getpolynomial(differencesTable, degree, interpolatePoint)
    print('')
    print('Para el punto x = %0.4f, f(x) = %0.4f' % (interpolatePoint, result))


main()