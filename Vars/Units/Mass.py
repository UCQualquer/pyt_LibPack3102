# https://en.wikipedia.org/wiki/Tonne
# https://www.greenfacts.org/glossary/mno/mass-units.htm

class Picogram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -12
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Nanogram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -9
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Microgram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -6
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Milligram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -3
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Gram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 1
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Kilogram(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 3
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Tonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 6
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor


class Kilotonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 9
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Megatonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 12
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Gigatonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 15
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Teratonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -18
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Petatonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 21
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor

class Exatonne(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 24
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Grams) # https://stackoverflow.com/a/69529125/10996607
    @property
    def Grams(self) -> float:
        return self.quantity * self.factor
