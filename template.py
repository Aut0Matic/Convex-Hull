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
            
            
        #! Main Loop
        while True:
            for i in range(0,394):
                for k in range(0, 64):
                    new_pixel(i, k, 255, 255, 255)
                    
            # Do something in here!

            
# Main function
if __name__ == "__main__":
    test_bench = TestBench()
    if (not test_bench.process()):
        test_bench.print_help()