
class Interval:

    def __init__(self, min: float, max: float):
        self.__min = min
        self.__max = max
    
    @property
    def min(self):
        return self.__min
    
    @property
    def max(self):
        return self.__max

    def __contains__(self, value: float):
        return self.min <= value <= self.max
    
    def surrounds(self, value: float):
        return self.min <= value <= self.max