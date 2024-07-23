class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(self.name, self.number_of_floors)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("такого этажа не сушествует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
            if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def add(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
            return House(self.value + value)

    def __iadd__(self, value):
            self.number_of_floors += value
            return self


h1 = House("ЖК Эльбрус", 30 )

h2 = House("April", 9)

h1.go_to(5)
h2.go_to(9)
print(len(h1))
print(str(h1))
print(h1 == h2)  # False
print(h1 < h2)   # True
print(h1 <= h2)  # True
print(h1 > h2)   # False
print(h1 >= h2)  # False
print(h1 != h2)

h1.add(2)
print(h1)

h2 += 1
print(h2)