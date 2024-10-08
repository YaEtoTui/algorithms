class DataObject:
    def __init__(self, c, a, b, A, j, Y):
        self.c = c
        self.a = a
        self.b = b
        self.A = A
        self.j = j
        self.x = None
        self.Y = Y

    def set_x(self, value):
        self.x = value