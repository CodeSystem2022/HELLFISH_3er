from math import sqrt


class funCuad:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def vertice(self):
        vx = (-self.b)/(2*self.a)
        vx2 = vx**2
        vy = self.a * vx2 + self.b*vx + self.c
        msg = f"Vertice en: ({vy}, {vx})"
        return msg

    def raices(self):
        dis = self.b ** 2 - 4 * self.a * self.c
        if dis == 0.0:
            x = -self.b/(2 * self.a)
            msg = f"Raiz única en x = {x}"
        elif dis > 0.0:
            x1 = (-self.b + sqrt(dis)) / 2 * self.a
            x2 = (+self.b + sqrt(dis)) / 2 * self.a
            msg = f"Raices en x = {x1}, y en x = {x2}"
        else:
            msg = "Raices imaginarias"
        return msg

    def ordenada(self):
        msg = f"La ordenada al orignen es {self.c}"
        return msg

    def forma(self):
        if self.a > 0:
            msg = "La parabola abre hacia: Arriba"
        else:
            msg = "La parabola abre hacia: Abajo"
        return msg
