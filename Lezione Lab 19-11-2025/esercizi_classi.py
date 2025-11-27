class Punto:
    def __init__(self, x_cord: int, y_cord: int):
        self.x_cord = x_cord
        self.y_cord = y_cord
    def distanza_origine(self):
        return pow(pow(self.x_cord,2)+pow(self.y_cord,2), 1/2)
    
x = Punto(x_cord = 5,
          y_cord = 10)
    
print(x.distanza_origine())
