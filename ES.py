import random
import numpy as np
Mu = 40
# Todo change Mu's coefficient below to attain the best result
Lambda = 1*Mu
crossover_probability = 0.4
mutation_probability = .1
def get_best_gene(chromosome, input_dots):
    fitness_vector = chromosome.evaluate(input_dots)
    # first we combine fitness and gene vector (a,b)
    fitness_gene = []
    for i in range(len(chromosome.genes)):
        fitness_gene.append({"fitness": fitness_vector[0], "gene": chromosome.genes[i], "index": i})
    fitness_gene_sorted = sorted(fitness_gene, key=lambda i: i['fitness'], reverse=True)
    return fitness_gene_sorted[0]["gene"][0],fitness_gene_sorted[0]["gene"][1]

def process_genes(chromosome, input_dots, sigma, remove_rate):
    fitness_vector = chromosome.evaluate(input_dots)
    # first we combine fitness and gene vector (a,b)
    fitness_gene = []
    for i in range(len(chromosome.genes)) :
        fitness_gene.append({"fitness": fitness_vector[i], "gene": chromosome.genes[i], "index": i})
    fitness_gene_sorted = sorted(fitness_gene, key= lambda i: i['fitness'], reverse=True)
    parent_genes = []
    if fitness_gene_sorted[0]["fitness"] > chromosome.BEST_FITNESS:
        chromosome.BEST_FITNESS = fitness_gene_sorted[0]["fitness"]
        print(chromosome.BEST_FITNESS)
    # we choose parents by a chance
    parents_counter = 0
    i = 0
    # while parents_counter < Lambda:
    #     if i < len(fitness_gene_sorted) - 1:
    #         i += 1
    #     else:
    #         i = 0
    #     if random.randint(0,100) < 100 * crossover_probability :
    #         parents_counter += 1
    for i in range(Lambda):
        parent_genes.append(fitness_gene_sorted[i]["gene"])
    # crossover
    for i in range (len(parent_genes) - 1):
        # mutation with normal distribution
        mutation_a = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000)/1000 < mutation_probability else 0
        mutation_b = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000)/1000 < mutation_probability else 0
        gene_probability = np.random.rand(1)[0]
        new_gene = [float(format((parent_genes[i][0]*gene_probability + parent_genes[i + 1][0]*(1 - gene_probability)) + mutation_a, "0.3f")),
                         float(format((parent_genes[i][1]*gene_probability + parent_genes[i + 1][1]*(1 - gene_probability)) + mutation_b, "0.3f"))]
        chromosome.genes.append(new_gene)
    # remove bad genes
    for i in range(1,remove_rate + 1):
        del chromosome.genes[fitness_gene_sorted[len(fitness_gene_sorted) - i]["index"]]
    return chromosome
