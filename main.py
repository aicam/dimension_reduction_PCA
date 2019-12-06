from Chromosome import Chromosome
from ES import process_genes, get_best_gene
from plot import plot_result
from file_handler import read_from_file
import numpy as np
input_dots = read_from_file("./Dataset/Dataset1.csv")
chromosome = Chromosome(500,-.1,.1)
#.903 .51
fitness_array = []
while sorted(chromosome.evaluate(input_dots), reverse=True)[0] < 10:
    chromosome, fitness_array = process_genes(chromosome, input_dots, 10**-1, 39, fitness_array)
print(sorted(chromosome.evaluate(input_dots), reverse=True)[0] )
a,b = get_best_gene(chromosome, input_dots)
print(a, "  ", b)
plot_result(input_dots,a,b, fitness_array)
def find_loss(a,b,input_dots):
    z_array = []
    loss_count = 0
    for dot in input_dots:
        add_new = True
        zprim = dot[0]*a + dot[1]*b
        for z in z_array:
            if np.abs(zprim - z) < .01:
                add_new = False
                loss_count += 1
                break
        if add_new :
            z_array.append(zprim)
    return loss_count
print(find_loss(a,b,input_dots))
