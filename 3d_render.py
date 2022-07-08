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

        def new_pixel(x, y, R, G, B):
            if y>31:
                self.matrix.SetPixel(x+192, y-32, R, G, B)
            else:
                self.matrix.SetPixel(x, y, R, G, B)

        def draw_line(a,b,R,G,B,duration):
            '''Draw a line between two points 'a' and 'b'
            with colour values 'R'ed 'G'reen 'B'lue
            that takes 'duration' to complete.'''
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-a[1]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 ))
            
            for i in range(1,distance):
                Px = int(a[0] + (x_distance)*(i/distance))
                Py = int(a[1] + (y_distance)*(i/distance))

                print("Drawing a pixel at ", Px, Py)
                new_pixel(Px, Py, R, G, B)
                time.sleep(duration/distance)
                
        def draw_line_3d(a, b, R, G, B, duration):
            '''Draw a line between two points 'a' and 'b' in 3d space
            with colour values 'R'ed 'G'reen 'B'lue
            that takes 'duration' to complete'''
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-b[1]
            z_distance = b[2]-b[2]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 +(z_distance)**2 ))

            for i in range(1,distance):
                Px = int(a[0] + (x_distance)*(i/distance))
                Py = int(a[1] + (y_distance)*(i/distance))
                Pz = int(a[2] + (z_distance)*(i/distance))
                
                # Generating brightness from z coordinate
                
                Rz = R-Pz
                Gz = G-Pz
                Bz = G-Pz 
                
                print(f"Drawing a pixel at ({Px}, {Py}) with RGB {Rz}, {Gz}, {Bz}")
                new_pixel(Px, Py, Rz, Gz, Bz)
            
            

        while True:
            for i in range(0, 381):
                draw_line((192, 0), (i, 63), 255, 255, 255, .5) 
            # Do something in here!

            
# Main function
if __name__ == "__main__":
    test_bench = TestBench()
    if (not test_bench.process()):
        test_bench.print_help()