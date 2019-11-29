import random
import numpy as np
class Chromosome:
    GENESNUMBER = 100
    MIN = 0
    MAX = 10
    def __init__(self, chromosome_length, min, max):
        self.GENESNUMBER = chromosome_length
        self.MIN = min
        self.MAX = max
        # gene[0] = a and gene[1] = b
        self.genes = [[random.randint(self.MIN,self.MAX), random.randint(self.MIN,self.MAX)] for i in range(self.GENESNUMBER)]
        self.score = [0 for i in range(self.GENESNUMBER)]

    def evaluate(self, input_dots):
        fitness_vector = []
        for gene in self.genes:
            gene_output = []
            for input_dot in input_dots:
                gene_output.append(input_dot[0]*gene[0] + input_dot[1]*gene[1])
            # use standard deviation as fitness
            fitness_vector.append(np.std(gene_output))
        return fitness_vector
