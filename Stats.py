from Array import *
import random
import matplotlib.pyplot as plt

"""
    Class represent stats
"""
class Stats:

    MAX_SIZE = 1000
    MIN_SIZE = 30

    """
        Constructor
    """
    def __init__(self, nb_tests, arrays_size):
        self.nb_tests = nb_tests
        self.array_size = int(arrays_size)
        self.random_test = []
        self.desc_test = []
        self.desc_size_time = {}
        self.rand_size_time = {}
        self.desc_time = 0
        self.rand_time = 0
        self.total_time = 0

    """
        Initialize array to make stats
    """
    def init_stats(self):
        for _ in range(self.nb_tests):
            if self.array_size < 1:
                arr = Array(random.randint(self.MIN_SIZE, self.MAX_SIZE))
            else:
                arr = Array(self.array_size)
            self.desc_test.append(arr)
            arr.custom_shuffle()
            self.random_test.append(arr)

    """
        Sort arrays and compute total time
    """
    def make_stats(self):
        for arr in self.desc_test:
            arr.insertion_sort()
            self.desc_time += arr.get_time()
            self.desc_size_time[arr.get_time()] = arr.get_size()

        for arr in self.random_test:
            arr.insertion_sort()
            self.rand_time += arr.get_time()
            self.rand_size_time[arr.get_time()] = arr.get_size()

        self.total_time = self.rand_time + self.desc_time

        return self.informations()

    """
        Make charts
    """
    def make_charts(self):
        fig, axs = plt.subplots(2, figsize=(8,8))
        
        for size, time in self.desc_size_time.items():
            axs[0].scatter(time, size)

        for size, time in self.rand_size_time.items():
            axs[1].scatter(time, size)
        
        fig.suptitle('Temps de tri suivant la taille des tableaux')
        axs[0].set_title('Génération descendante')
        axs[0].set_xlabel('Taille des tableaux')
        axs[0].set_ylabel('Temps de tri (secondes)')

        axs[1].set_title('Génération aléatoire')
        axs[1].set_xlabel('Taille des tableaux')
        axs[1].set_ylabel('Temps de tri (secondes)')

        plt.show()

    """
        Return time
    """
    def get_all_time(self):
        return [str(self.array_size), 
                str(self.total_time), 
                str(self.desc_time), 
                str(self.rand_time)]

    """
        Display test informations
    """
    def informations(self):
        return 'Temps total de tri : {} secondes\n'\
            '------------------------------------------------------------------------------------------\n'\
            'Tri total ordre décroissant : {} secondes\n'\
            'Moyenne de tri décroissant : {} secondes\n'\
            '------------------------------------------------------------------------------------------\n'\
            'Tri total aléatoire : {} secondes\n'\
            'Moyenne de tri aléatoire : {} secondes\n'\
            '------------------------------------------------------------------------------------------\n'\
            .format(self.total_time, 
                    self.desc_time, 
                    self.desc_time / self.nb_tests,
                    self.rand_time,
                    self.rand_time / self.nb_tests)