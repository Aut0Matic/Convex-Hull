# A solution to the Convex Hull problem

import random
import math

# Defining points:

points = []

for i in range(1,50):
    Px = random.randrange(-25,25)
    Py = random.randrange(-25,25)
    
    points.append((Px, Py))
    
# Function to solve the lowest y-value point

def bottom(points):
    minimum = (11, 11)
    for i in points:
        if i[1]<minimum[1]:
            minimum = i
    return minimum

# Function to solve which direction the line connected by p1-p2-p3

def turn(p1, p2, p3):
    # = 0: collinear
    # >0: left turn
    # <0: right turn
    value = (p1[0]-p2[0])*(p3[1]-p2[1])-(p1[1]-p2[1])*(p3[0]-p2[0])
    return value

# Determining the bottom point

bottom_point = bottom(points)

# Sorting all points by anticlockwise angle relative to the bottom point

points =sorted(points, key=lambda p: (math.atan2(p[1]-bottom_point[1], p[0]-bottom_point[0])))

# Defining the stack

stack = []

# Iterate through all points, add the next one
for i in points:
    stack.append(i)
    if len(stack)>2:
        
        # While the final 3 line segment turns right, remove the middle segment.
        
        while turn(stack[-3], stack[-2], stack[-1])>=0:
            
            temp = stack[-1] # Grabbing the end
            
            stack.pop() # Popping end
            stack.pop() # Popping middle
            
            stack.append(temp) # Replacing End
                        
print("All points: ", points)

print("Hull points: ", stack)
