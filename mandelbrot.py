#!/usr/bin/env python
from samplebase import SampleBase
import time
import math
import random
import numpy as np

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
                
        #? Function to determine if a given complex number, z, will escape after a set number of iterations
        def escape(z, max_iterations):
            x = z.real
            y = z.imag
            
            x0 = x
            y0 = y
            
            x2 = 0
            y2 = 0
            w = 0
            
            iterations = 0
            
            while (x2 + y2 <= 4 and iterations <max_iterations):
                x = x2 - y2 + x0
                y = w - x2 - y2 + y0
                x2 = x * x
                y2 = y * y
                w = (x + y) * (x + y)
                iterations = iterations + 1;
                
            return iterations

        base_array = np.empty((192, 64), complex)
            
        for x in range(0,192):
            for y in range(0, 64):
                base_array[x][y] = np.complex( (300.01/(x-96.01)) , (100.01/(y-64.01)) )
                    
        print("SETUP COMPLETE!")

        #! Main Loop
        while True:
            
            for var in range(1,10):  
                print("var = ", var);
                time.sleep(0.00001)
                
                for i in range(0,192):
                    print("i = ", i)
                    time.sleep(0.00001)
                    
                    for y in range(0, 64):
                        print("y = ", y)
                        time.sleep(0.00001)
                        
                        z = base_array[i][y]

                        result = escape(z, var)
                        
                        sc = int((1/var) * 255)
                        
                        if result == var:
                            new_pixel(i, y, 10, 10, sc)

                        
                    
                
                    
            # Do something in here!

            
# Main function
if __name__ == "__main__":
    test_bench = TestBench()
    if (not test_bench.process()):
        test_bench.print_help()
