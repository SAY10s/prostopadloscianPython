class Sixwaller:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def count(self):
        self.pole = 2 * self.a * self.b + 2 * self.a * self.c + 2 * self.b * self.c
        self.V = self.a * self.b * self.c
        self.krawedzie = 4 * self.a + 4 * self.b + 4 * self.c

    def info(self):
        print(f"Pole: {self.pole}\nObjętość: {self.V}\nDługość wszystkich krawędzi: {self.krawedzie}")

a = input("Podaj A: ")
b = input("Podaj B: ")
c = input("Podaj C: ")

prostopadloscian = Sixwaller(a, b, c)
prostopadloscian.count()
prostopadloscian.info()

