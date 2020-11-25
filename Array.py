import random
import timeit

"""
    Custom array
"""
class Array:

    MAX_NUMBER = 999999
    MIN_NUMBER = -999999
    SPACE = 25000

    """
        Constructor
    """
    def __init__(self, size):
        self.size = size
        self.sort_time = 0
        self.elements = []
        self.generate_descending()

    """
        Sort an array in ascending order
    """
    def insertion_sort(self):

        start = timeit.default_timer() 

        for i in range(1, self.size):
            temp = self.elements[i]
            j = i
            while j > 0 and self.elements[j - 1] > temp: 
                self.elements[j] = self.elements[j - 1]
                j -= 1
            self.elements[j] = temp

        self.sort_time = timeit.default_timer() - start

    """
        Generate in descending order
    """
    def generate_descending(self):
        maxi = random.randint(0, self.MAX_NUMBER)
        for _ in range(self.size):
            self.elements.append(maxi)
            maxi -= random.randint(0, self.SPACE)

    """
        Shuffle elements in data
    """
    def custom_shuffle(self):
        random.shuffle(self.elements)

    """
        Return sorting time
    """
    def get_time(self):
        return self.sort_time

    """
        Return array size
    """
    def get_size(self):
        return self.size