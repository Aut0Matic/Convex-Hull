#!/usr/bin/env python
from samplebase import SampleBase
import time
import math

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
        def quad(left_x, top_y, right_x, bottom_y):
            return [(left_x, ), (126, 9), (126, 51), (62, 51)]
        
        def isinppoly(point, polygon):
            for p in polygon:
                for k in polygon:
                    print("Placeholder Function")
            
        #! Main Loop
        while True:
            draw_polygon(square, 255, 255, 255, 1)
                    
            # Do something in here!

            
# Main function
if __name__ == "__main__":
    test_bench = TestBench()
    if (not test_bench.process()):
        test_bench.print_help()
