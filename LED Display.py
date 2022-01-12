# A visual representation of the convex hull problem displayed on LED matricies

# Driver file
from samplebase import SampleBase

# Imports
import random
import math
import time

# Defining points:

class visualHull(SampleBase):
    def __init__(self, *args, **kwargs):
        super(visualHull, self).__init__(*args, **kwargs)

    def run(self):
        width = self.matrix.width
        height = self.matrix.height
        
        def wait(multiplier):
            time.sleep(0.5/multiplier)
        
        while True:
            # Clearing the matrix
            self.matrix.Fill(0,0,0)
            
            points = []
            
            no_of_points = random.randrange(5, 50)
            
            for i in range(no_of_points):
                Px = random.randrange(1,width)
                Py = random.randrange(1,height)
                
                # Note: this is appending a tuple.
                points.append((Px,Py))
                
                # Set the point pixel to white.
                self.matrix.SetPixel(Px,Py,255,255,255)

                wait(no_of_points)
                
# Main function
if __name__ == "__main__":
    visual_hull = visualHull()
    if (not visual_hull.process()):
        visual_hull.print_help()






""" points = []

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
 """