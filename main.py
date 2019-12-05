from Chromosome import Chromosome
from ES import process_genes, get_best_gene
from plot import plot_result
from file_handler import read_from_file
input_dots = read_from_file("./Dataset/Dataset2.csv")
chromosome = Chromosome(500,-.1,.1)
#.903 .51
while sorted(chromosome.evaluate(input_dots), reverse=True)[0] < 100:
    chromosome = process_genes(chromosome, input_dots, 10**-2, 39)
print(sorted(chromosome.evaluate(input_dots), reverse=True)[0] )
a,b = get_best_gene(chromosome, input_dots)
print(a, "  ", b)
plot_result(input_dots,a,b)