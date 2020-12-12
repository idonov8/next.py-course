from functools import reduce
class Pixel():
    def __init__(self, x=0, y=0, r=0, g=0, b=0):
        self._x     = x
        self._y     = y
        self._red   = r
        self._green = g
        self._blue  = b
    
    def set_coords(self, x, y):
        self._x = x
        self._y = y
    
    def set_grayscale(self):
        avg = (self._red+self._green+self._blue)/3
        self._red, self._green, self._blue = avg, avg, avg

    def print_pixel_info(self):
        rgb = {"Red": self._red, "Green": self._green, "Blue": self._blue}
        color = list(filter(lambda a: rgb[a] != 0 or rgb[a]>50, rgb))
        color = color[0] if len(color)==1 else ""
        print('X: %i, Y: %i, Color: (%i, %i, %i) %s'%(self._x, self._y, self._red, self._green, self._blue, color))

def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

main()

