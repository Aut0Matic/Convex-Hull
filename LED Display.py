# A visual representation of the convex hull problem displayed on LED matricies

# Driver file
from samplebase import SampleBase

# Imports
import random
import math
import time

# Defining points:

class LEDdisplay(SampleBase):
    def __init__(self, *args, **kwargs):
        super(LEDdisplay, self).__init__(*args, **kwargs)

    def run(self):
        width = self.matrix.width
        height = self.matrix.height
       
        #! Function definitions for drawing
        
        #? 12 screen pixel correction.
        
        def new_pixel(x, y, R, G, B):
            if y>31:
                self.matrix.SetPixel(x+192, y-32, R, G, B)
            else:
                self.matrix.SetPixel(x, y, R, G, B)
        
        #? Line Function
        def line(a,b,R,G,B,duration):
            # Draw a line between two points, a and b.
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-a[1]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 ))
            
            for i in range(0,distance*2):
                Px = a[0] + (x_distance/2)*(i/distance)
                Py = a[1] + (y_distance/2)*(i/distance)

                print(Py)
                
                new_pixel(Px, Py, R, G, B)
                time.sleep(duration/distance)
        
        #? Point Array Function
        def draw_list(array, R, G, B, duration):
            # Set an array of pixels to a specified colour over a time interval.
            for i in array:
                new_pixel(i[0], i[1], R, G, B)
                time.sleep(duration/len(array))
                
        #! Function definitions for convex hull
        
        #? Lowest Point Function
        def bottom(points):
            minimum = (0, 64)
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
       
       
       #! Main Loop
       
        while True:
            # Clearing the matrix
            self.matrix.Fill(0,0,0)
            
            # Generating Points
            points = []
            no_of_points = random.randrange(5, 200)

            tm = 1/no_of_points
            
            for i in range(no_of_points):
                Px = random.randrange(0,width/2)
                Py = random.randrange(0,height*2)
                
                # Note: this is appending a tuple.
                points.append((Px,Py))

            # Colouring Points dim White
            draw_list(points, 10, 10, 10, 1)
            
            # Determining the bottom point and colouring it green
            bottom_point = bottom(points)
            new_pixel(bottom_point[0], bottom_point[1], 38, 255, 0)

            # Drawing lines from the bottom point to each point in the random order.
            for i in points:
                line(bottom_point, i, 0, 0, 150, tm)
            
            # Re clearing and colouring points dim white
            self.matrix.Fill(0,0,0)
            draw_list(points, 10, 10, 10, 0.00001)
            
            # Sorting all points by anticlockwise angle relative to the bottom point
            points = sorted(points, key=lambda p: (math.atan2(p[1]-bottom_point[1], p[0]-bottom_point[0])))
            
            draw_list(points, 255, 255, 255, 1)
            new_pixel(bottom_point[0], bottom_point[1], 38, 255, 0) 
            
            # Defining the stack
            stack = []
            not_in_hull = []
            
            # Iterating through all points, add the next one
            for i in points:
                stack.append(i)
                draw_list(stack, 38, 255, 0, 0.001)
               
                if len(stack)>1:
                    line(stack[-2], stack[-1], 38, 255, 0, tm)
                
                draw_list(stack, 38, 255, 0, 0.001)
                   
                if len(stack)>2:
                   
                    # While the final 3 line segment turns right, remove the middle segment.
                    try: 
                        while len(stack)>2 and turn(stack[-3], stack[-2], stack[-1])>=0:
                            
                            # This is used to paint red
                            not_in_hull.append(stack[-2])
                            
                            line(stack[-3], stack[-2], 255, 0, 0, tm/2)
                            line(stack[-2], stack[-1], 255, 0, 0, tm/2)
                            
                            temp = stack[-1] # Grabbing the end
                            
                            stack.pop() # Popping end
                            stack.pop() # Popping middle
                            
                            stack.append(temp) # Replacing End
                            
                            # Painting Black.
                            line(stack[-2], not_in_hull[-1], 0, 0, 0, 0.001)
                            line(not_in_hull[-1], stack[-1], 0, 0, 0, 0.001)
                            
                            # Rejoining line segment.
                            draw_list(not_in_hull, 255, 0, 0, 0.001)
                            line(stack[-2], stack[-1], 38, 255, 0, tm)

                            for i in range(len(stack)-1):
                                line(stack[i], stack[i+1], 38, 255, 0, 0.00001)
                    except Exception:
                        pass

            line(points[-1], points[0], 38, 255, 0, tm)
                
            time.sleep(1)
            
            # Debugging
            # print(points)

# Main function
if __name__ == "__main__":
    led_display = LEDdisplay()
    if (not led_display.process()):
        led_display.print_help()
