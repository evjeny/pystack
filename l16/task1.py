class Касса:
    def __init__(self, cash = 0):
        self.cash = cash

    def top_up(self, X):
        self.cash += X
    
    def count_1000(self):
        print(self.cash // 1000)
    
    def take_away(self, X):
        if self.cash >= X:
            self.cash -= X
        else:
            raise ValueError("Недостаточно средств")

