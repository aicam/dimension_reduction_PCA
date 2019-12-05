from Chromosome import Chromosome
from ES import process_genes, get_best_gene
from plot import plot_result
from file_handler import read_from_file
input_dots = read_from_file("./Dataset/Dataset1.csv")
chromosome = Chromosome(100,-10,10)
while sorted(chromosome.evaluate(input_dots), reverse=True)[0] < 10:
    process_genes(chromosome, input_dots, 10**-2, 5)
a,b = get_best_gene(chromosome, input_dots)
plot_result(input_dots,a,b)