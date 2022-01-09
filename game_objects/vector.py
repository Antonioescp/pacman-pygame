# For position and physics
class Vector2:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    
    def __repr__(self) -> str:
        return '<Vector x: %.2f, y: %.2f>' % (self.x, self.y)

    
    def to_tuple(self):
        # for ease of use in pygame methods
        return (self.x, self.y)
