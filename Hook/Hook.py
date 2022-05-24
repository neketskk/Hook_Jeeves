import random
class Vector:
    x: float = 0
    y: float = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({round(self.x, 4)}, {round(self.y, 4)})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)
    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)
    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)
def func_r(v: Vector) -> float:
    return  100 * (v.x**2 - v.y) ** 2 + (1 - v.x) ** 2
def func_r1(v: Vector) -> float:
    return  100 * (v.y - v.x**3) ** 2 + (1 - v.x) ** 2
def explor(p0: Vector,
              h1: float,
              h2: float,
              func: None) -> Vector:
    if func(p0 + Vector(h1, 0)) < func(p0):
        p1 = p0 + Vector(h1, 0)
    elif func(p0 - Vector(h1, 0)) < func(p0):
        p1 = p0 - Vector(h1, 0)
    else:
        p1 = p0
    if func(p1 + Vector(0, h2)) < func(p1):
        p2 = p1 + Vector(0, h2)
    elif func(p1 - Vector(0, h2)) < func(p1):
        p2 = p1 - Vector(0, h2)
    else:
        p2 = p1
    return p2
def sample(x1: Vector,
           x2: Vector,
           gamma: float = 2) -> Vector:
    return x1 + gamma * (x2 - x1)
def hook(func,
                p_0: Vector,
                h1: float = 1.0,
                h2: float = 1.0,
                h_min: float = 1e-10,
                alpha: float = 0.5,
                gamma: float = 2.0,
                iters: int = 10000,
                ) -> (Vector, int):

    global i
    p_explor = p_0
    for i in range(iters):
        p_1 = explor(p_explor, h1, h2, func)
        print("№",i+1,p_1)
        if func(p_1) < func(p_0):
            p_explor = sample(p_0, p_1, gamma)
            p_0 = p_1
        else:
            if h1 < h_min and h2 < h_min:
                break
            else:
                if h1 > h_min:
                    h1 = h1 * alpha
                if h2 > h_min:
                    h2 = h2 * alpha
                p_explor = p_0
    return p_0, i
YorN = input('Enter data yourself? Y or N?\n')
if YorN == "Y":
    a, b = map(float, input('\nEnter the coordinates of the starting point: ').split())
    p = Vector(a, b)
elif YorN == "N":
    p = Vector(random.randint(-10, 10), random.randint(-10, 10))
else:
    print("\nIncorrect data entered \n EROR 404")
    exit(0)
test=input('Select a test. 1 or 2?\n')
if test=="1":
    min_p, iteration = hook(func=func_r,p_0=p)
    print('Algorithm completed:', iteration+1)
    print('Minimum function at a point (x, y) = ', min_p)
    print('Function value F(x, y) = ', round(func_r1(min_p), 6))
elif test=="2":
    min_p, iteration = hook(func=func_r1,p_0=p)
    print('Algorithm completed:', iteration+1)
    print('Minimum function at a point (x, y) = ', min_p)
    print('Function value F(x, y) = ', round(func_r(min_p), 6))
else:
    print("\nIncorrect data entered \n EROR 404")
    exit(0)

