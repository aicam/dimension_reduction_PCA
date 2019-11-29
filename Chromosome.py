import random
class Chromosome:
    GENESNUMBER = 100
    MIN = 0
    MAX = 10
    def __init__(self, chromosome_length, min, max):
        self.GENESNUMBER = chromosome_length
        self.MIN = min
        self.MAX = max
        # Todo create a random list for genes between min and max below
        self.genes = [[random.randint(self.MIN,self.MAX), random.randint(self.MIN,self.MAX)] for i in range(self.GENESNUMBER)]
        self.score = [0 for i in range(self.GENESNUMBER)]

    def evaluate(self):
        """
        Update Score Field Here
        """
        #Todo
