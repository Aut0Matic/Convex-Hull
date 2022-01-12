#!/usr/bin/env python
from samplebase import SampleBase
import time
import random
import math

class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):
        width = self.matrix.width
        height = self.matrix.height

        def line(a,b,colour,time):
            # Draw a line between two points, a and b.
            
            # Basic Trig
            distance = int(math.sqrt( (b[0]-a[0])**2 + (b[1]-a[1])**2 ))
            
            for i in range(1,distance):
                Px = a[0] + (b[0]-a[0])*(i/distance)
                Py = a[1] + 1
            
            

        while True:
            
            self.matrix.SetPixel(1,1,255,255,0)
            self.matrix.SetPixel(width, height, 100,100,100)
            
            
            
            
            """ for i in range(1,2):
                points = []
                
                Px = random.randrange(1,width)
                Py = random.randrange(1,height)

                points.appedn((Px, Py))
                
                self.matrix.setPixel(Px, Py, 255,255,255)
                time.sleep(1)
 """

            
# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()
