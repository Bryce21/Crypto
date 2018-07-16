class p_double():
    def __init__(self, mod, px, py, a):
        """ Create a new point at the origin """
        self.mod = mod
        self.px = px
        self.py = py
        self.a = a
        check = ((3 * self.px ** 2) + self.a) / (2 * self.py)
        if not float(check).is_integer():
            self.den_inv = pow((2 * self.py), self.mod - 2, self.mod)
            self.c = (((3 * px ** 2) + a) * self.den_inv) % self.mod
        else:
            self.c = (((3 * px ** 2) + a) / (2 * py)) % mod
        self.rx = (self.c ** 2 - (2 * px)) % mod
        self.ry = (self.c * (self.px - self.rx) - self.py) % self.mod

    def print_values(self):
        print("C is: {}, Px is {}".format(self.c, self.px))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == "__main__":
    print("Point doubling")
    p = p_double(67, 2, 22, 0)
    print(p.c)
    print(p.rx)
    print(p.ry)