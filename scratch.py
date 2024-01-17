# %%
from typing_extensions import SupportsIndex

import math

class Vector(tuple):
    def __mul__(self, __value: SupportsIndex) -> tuple:
        return Vector([x * __value for x in self])
    
    def __rmul__(self, __value: SupportsIndex) -> tuple:
        return self.__mul__(__value)
    
    def __truediv__(self, other) -> tuple:
        return Vector([x/other for x in self])
    
    @property
    def length(self):
        return math.sqrt(sum([x*x for x in self]))
    
    @property
    def average(self):
        return sum(self) / len(self)
    
    @property
    def manhattan(self):
        return sum(self)
