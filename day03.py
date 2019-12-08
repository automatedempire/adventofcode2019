#!/usr/bin/env python3

from adventhelper import download_input

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.segments = {
            'x': [x1, x2],
            'y': [y1, y2]
        }

        self.changed, self.unchanged = ['x','y'] if x1 != x2 else ['y','x']

        self.staticval = self.segments[self.unchanged][0]
        self.minChanged = min(self.segments[self.changed])
        self.maxChanged = max(self.segments[self.changed])

    def __repr__(self):
        x=self.segments["x"]
        y=self.segments["y"]
        return f'{self.unchanged}:({x[0]},{y[0]}):({x[1]},{y[1]})'

def intersection(line1, line2):
    xChanged, yChanged = [line1, line2] if line1.changed == 'x' else [line2, line1]

    #This logic works because we are guaranteed segments that only change in one dimension.
    #This means that they will intersect at the static values of both points if they cross.

    #See if the X and Y values might touch.
    xTouch = xChanged.minChanged <= yChanged.staticval <= xChanged.maxChanged
    yTouch = yChanged.minChanged <= xChanged.staticval <= yChanged.maxChanged

    if xTouch and yTouch:
        return (yChanged.staticval, xChanged.staticval)
    else:
        return False

def parsePath(path):
    pathSegments = []
    x,y = 0,0
    for dirvec in path:
        direction = dirvec[0]
        mag = int(dirvec[1:])

        if direction == 'U':
            newX = x + mag
            newY = y
        elif direction == 'D':
            newX = x - mag
            newY = y
        elif direction == 'L':
            newY = y - mag
            newX = x
        elif direction == 'R':
            newY = y + mag
            newX = x

        pathSegments.append(Line(x,y,newX,newY))
        x, y = newX, newY
    return pathSegments

dayinput = download_input(day=3)

with open(dayinput) as d_in:
    path1 = d_in.readline().split(',')
    path2 = d_in.readline().split(',')

firstpath = parsePath(path1)
secondpath = parsePath(path2)
intersections = []
for seg1 in firstpath:
    for seg2 in secondpath:
        point = intersection(seg1, seg2)
        if point:
            intersections.append(point)

#Ignore touching at 0,0
intersections.remove((0,0))

print(f"Wires cross at {len(intersections)} points")

closest = min(map(lambda p: abs(p[0]) + abs(p[1]), intersections))
print(f"Manhattan distance to closest crossed wire: {closest}")
