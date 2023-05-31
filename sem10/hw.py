class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    def __lt__(self, other):
        if self.height != other.height:
            return self.height < other.height
        elif self.danger != other.danger:
            return self.danger < other.danger
        else:
            return self.color < other.color

    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other):
        min_color = min(self.color, other.color)
        avg_height = (self.height + other.height) // 2
        max_danger = max(self.danger, other.danger)
        return Dragon(avg_height, max_danger, min_color)

    def __isub__(self, number):
        self.height -= self.height // number
        self.danger += self.danger % number
        return self

    def __call__(self, string):
        return string * self.danger

    def change_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."

    def __repr__(self):
        return f"Dragon({self.height}, {self.danger}, {self.color})"


# Пример использования

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome"))
