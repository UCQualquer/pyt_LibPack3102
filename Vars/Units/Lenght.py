# https://wps.prenhall.com/wps/media/objects/165/169061/blb9ch0104.html
# https://www.cuemath.com/measurement/length-conversion/

class Femtometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -15
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Picometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -12
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Nanometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -9
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Micrometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -6
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Millimeter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -3
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Centimeter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -2
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Decimeter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** -1
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Meter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 1
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Decameter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 1
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Hectometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 2
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Kilometer(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 3
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Megameter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 6
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor

class Gigameter(object):
    def __init__(self, quantity: float):
        self.quantity = quantity
        self.factor = 10 ** 9
    def __repr__(self) -> str:
        return '{:.15g}'.format(self.Meters)
    @property
    def Meters(self) -> float:
        return self.quantity * self.factor