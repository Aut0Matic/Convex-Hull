import cmath
import random
import numpy as np

def escape(z):
    x = z.real
    y = z.imag
    
    x0 = x
    y0 = y
    
    x2 = 0
    y2 = 0
    w = 0
    
    iterations = 0
    max_iterations = 50;
    
    while (x2 + y2 <= 4 and iterations <max_iterations):
        x = x2 - y2 + x0
        y = w - x2 - y2 + y0
        x2 = x * x
        y2 = y * y
        w = (x + y) * (x + y)
        iterations = iterations + 1;
        
    return iterations


for i in range(1,100):
    xcord = random.uniform(-1.5,1.5)
    ycord = random.uniform(-1.5,1.5)
    
    z=np.complex(xcord + ycord)
    
    result = escape(z)
    
    if result < 50:
        print(z, " escaped after: ", result)
    else:
        print(z, " didnt escape!")
    
    