from math import ceil

class Чебурашка:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.s = 1
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Невозможно деградировать")

    def count_moves(self, x2, y2):
        """
         возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        """
        return int(ceil(abs(self.x - x2) / self.s)) + int(ceil(abs(self.y - y2) / self.s))
