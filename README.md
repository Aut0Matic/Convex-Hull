# Convex Hull
 A solution and visual for the Convex Hull problem

# Outline:
Given a set of points in space, the Convex Hull problem aims to find the smallest subset of points which geometrically encloses the entire set.

In this solution, I have used the Graham Scan algorithm (https://en.wikipedia.org/wiki/Graham_scan) which starts from an extrema point in any direction and works around the set, determining if the proposed hull turns in a concave direction.

[GrahamScanDemo](https://user-images.githubusercontent.com/82569441/149131849-736cd10f-92bb-4c76-9edf-1bbaa312e596.gif)

# Files
## convex hull.py
will generate and solve hulls, outputting a format of:
```
All points
Hull points
```
These can conveniently be copy/pasted directly into a desmos window: https://www.desmos.com/calculator

## samplebase.py
is a required file for the Adafruit Raspberry Pi Bonnet, allowing it to be driven by python code.

## LED Display.py
continuously generates and solves the complex hull problem step by step, displaying it on LED matrices.

## testbench.py
can be used as a basis to start writing code to be executed on the LEDs
