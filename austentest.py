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

        def line(a,b,R,G,B,duration):
            # Draw a line between two points, a and b.
            
            x_distance = b[0]-a[0]
            y_distance = b[1]-a[1]
            
            # Basic Trig
            distance = int(math.sqrt( (x_distance)**2 + (y_distance)**2 ))
            
            for i in range(2,distance):
                Px = a[0] + (x_distance)*(i/distance)
                Py = a[1] + (y_distance)*(i/distance)

                self.matrix.SetPixel(Px, Py, R, G, B)
                time.sleep(duration/(1/distance))
            
            

        while True:
            
            points = [(0,0), (0,0)]
                        
            for i in range(0,2):

                x = random.randrange(0,width-1)
                y = random.randrange(0,height-1)

                self.matrix.SetPixel(x, y, 255, 255, 255)
                
                points[i]=((x,y))
            
            line(points[0], points[1], 0, 0, 255, 2)
            
            self.matrix.Fill(0,0,0)            
            
            
            
            
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
