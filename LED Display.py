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
       
        #! Function definitions for drawing
        
        #? Line Function
        def line(a,b,R,G,B,duration):
            # Draw a line between two points, a and b.
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-a[1]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 ))
            
            for i in range(1,distance):
                Px = a[0] + (x_distance)*(i/distance)
                Py = a[1] + (y_distance)*(i/distance)

                self.matrix.SetPixel(Px, Py, R, G, B)
                time.sleep(duration/distance)
        
        #? Point Array Function
        def draw_list(array, R, G, B, duration):
            # Set an array of pixels to a specified colour over a time interval.
            for i in array:
                self.matrix.SetPixel(i[0], i[1], R, G, B)
                time.sleep(duration/len(array))
                
        #! Function definitions for convex hull
        
        #? Lowest Point Function
        def bottom(points):
            minimum = (11, 11)
            for i in points:
                if i[1]<minimum[1]:
                    minimum = i
            return minimum

        #? Turn Direction Function
        def turn(p1, p2, p3):
            # = 0: collinear
            # >0: left turn
            # <0: right turn
            value = (p1[0]-p2[0])*(p3[1]-p2[1])-(p1[1]-p2[1])*(p3[0]-p2[0])
            return value
        """
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
        """                 
        while True:
            # Clearing the matrix
            self.matrix.Fill(0,0,0)
            
            # Generating Points
            points = []
            no_of_points = random.randrange(5, 50)
            
            for i in range(no_of_points):
                Px = random.randrange(1,width)
                Py = random.randrange(1,height)
                
                # Note: this is appending a tuple.
                points.append((Px,Py))
            
            # Colouring Points dim White
            draw_list(points, 180, 180, 180, 1)
            
            # Determining the bottom point and colouring it green
            bottom_point = bottom(points)
            self.matrix.SetPixel(bottom_point[0], bottom_point[1], 38, 255, 0)
            
            # Sorting all points by anticlockwise angle relative to the bottom point
            points = sorted(points, key=lambda p: (math.atan2(p[1]-bottom_point[1], p[0]-bottom_point[0])))
            
            draw_list(points, 255, 255, 255, 0.25)
            self.matrix.SetPixel(bottom_point[0], bottom_point[1], 38, 255, 0) 
            
            # Defining the stack
            stack = []
            not_in_hull = []
            
            # Iterating through all points, add the next one
            for i in points:
                stack.append(i)
                draw_list(stack, 38, 255, 0, 0.001)
               
                if len(stack)>1:
                    line(stack[-2], stack[-1], 38, 255, 0, 0.25)
                
                draw_list(stack, 38, 255, 0, 0.001)
                   
                if len(stack)>2:
                   
                   # While the final 3 line segment turns right, remove the middle segment. 
                    while turn(stack[-3], stack[-2], stack[-1])>=0:
                        
                        # This is used to paint red
                        not_in_hull.append(stack[-2])
                        
                        line(stack[-3], stack[-2], 255, 0, 0, 0.001)
                        line(stack[-2], stack[-1], 255, 0, 0, 0.001)
                        
                        time.sleep(0.2) 
                        
                        temp = stack[-1] # Grabbing the end
                        
                        stack.pop() # Popping end
                        stack.pop() # Popping middle
                        
                        stack.append(temp) # Replacing End
                        
                        line(stack[-2], not_in_hull[-1], 0, 0, 0, 0.001)
                        line(not_in_hull[-1], stack[-1], 0, 0, 0, 0.001)
                        
                        draw_list(not_in_hull, 255, 0, 0, 0.001)
                        line(stack[-2], stack[-1], 38, 255, 0, 0.25)
            line(points[-1], points[1], 38, 255, 0, 0.25)
                
            time.sleep(0.25)
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