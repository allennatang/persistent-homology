'''
Exercise: Write a script (say in Python, or some other language) 
that selects 400 points uniformly at random (or approximately uniformly at random) 
from the annulus {(x,y)|0.952≤x^2+y^2≤1.052} in R2. 
Compute its persistent homology barcodes using Ripser.
'''
import random
import math

# Return the next random floating-point number in the range 0.0 <= X < 1.0
def get_annulus_points():
    random.seed(10)
    r = random.uniform(math.sqrt(0.952), math.sqrt(1.052))
    theta = random.uniform(0,360)

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return (x,y)

def test(points):
    result = points[0]**2+points[1]**2
    return ((0.952 <= result) & (result <= 1.052))

def main():
    points = get_annulus_points()
    print(points)
    print(test(points))

if __name__ == "__main__":
    main()