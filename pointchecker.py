#!/usr/bin/env python
from samplebase import SampleBase
import time
import math
import random

class TestBench(SampleBase):
    def __init__(self, *args, **kwargs):
        super(TestBench, self).__init__(*args, **kwargs)

    def run(self):
        width = self.matrix.width
        height = self.matrix.height

        #? Function to draw a pixel mapped for -c=12
        def new_pixel(x, y, R, G, B):
            if y>31:
                self.matrix.SetPixel(x+192, y-32, R, G, B)
            else:
                self.matrix.SetPixel(x, y, R, G, B)

        #? Function to draw a line
        def draw_line(a,b,R,G,B,duration):
            # Draw a line between two points, a and b.
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-a[1]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 ))
            
            for i in range(1,distance):
                Px = int(a[0] + (x_distance)*(i/distance))
                Py = int(a[1] + (y_distance)*(i/distance))

                new_pixel(Px, Py, R, G, B)
                time.sleep(duration/distance)
        
        #? Function to draw a polygon from its points
        def draw_polygon(polygon, R, G, B, duration):
            size = len(polygon)
            for i in range(0, size-1):
                draw_line(polygon[i], polygon[i+1], R, G, B, duration/size)
            draw_line(polygon[-1], polygon[0], R, G, B, duration/size)
        
        #! Polygons
        
        #? Square!
        def quad():
            
            left = random.randrange(10, width/4 - 10)
            right = random.randrange(width/4 + 10, width/2 - 10)
            top = random.randrange(5, height-5)
            bottom = random.randrange(height+5, height*2 - 5)

            return [(left, top), (right, top), (right, bottom), (left, bottom)]
       
        def vectorSort(a, b):
            # returns the bottom vector, then the top vector
            if a[1]<=b[1]:
                return a, b
            else:
                return b, a
            
        #? Turn Direction Function
        def turn(p1, p2, p3):
            # = 0: collinear
            # >0: left turn
            # <0: right turn
            value = (p1[0]-p2[0])*(p3[1]-p2[1])-(p1[1]-p2[1])*(p3[0]-p2[0])
            return value
            
        def lineCross(a, b, p):
            if a[0]<=p[0] and p[0]<=b[0]:
                if turn(a, b, p)>=0:
                    return True
            
            if b[0]<=p[0] and p[0]<=a[0]:
                if turn(a, b, p)<=0:
                    return True
                
            return False;
                
            return True
        
        def isinppoly(point, polygon):
            count = 0
            for i in range(0, len(polygon)-1):
                bottom, top = vectorSort(polygon[i], polygon[i+1])
                if lineCross(bottom, top, point):
                    count = count + 1
            
            bottom, top = vectorSort(polygon[i], polygon[i+1])
            
            if count%2==0:
                return False
            return True
                
            
                
            
        #! Main Loop
        while True:
            self.matrix.Fill(0,0,0)
            
            new_quad = quad()
            
            draw_polygon(new_quad, 0, 0, 255, 1)

            #? Generating Points.
            
            points = []
            
            no_of_points = random.randrange(1,200)
            
            for i in range(1,no_of_points):
                Px = random.randrange(0, width/2)
                Py = random.randrange(0, height*2)
                
                points.append((Px, Py))
                
                new_pixel(Px, Py, 255, 255, 255)
                
            for i in points:
                if isinppoly(i, new_quad):
                    new_pixel(i[0], i[1], 0, 255, 0)
                else:
                    new_pixel(i[0], i[1], 255, 0, 0)
                time.sleep(0.01)
            
            
            time.sleep(1)
                
                

                    
            # Do something in here!

            
# Main function
if __name__ == "__main__":
    test_bench = TestBench()
    if (not test_bench.process()):
        test_bench.print_help()
