import random
import numpy as np
Mu = 10
# Todo change Mu's coefficient below to attain the best result
Lambda = 1*Mu
crossover_probability = 0.4
mutation_probability = .02

def get_best_gene(chromosome, input_dots):
    fitness_vector = chromosome.evaluate(input_dots)
    # first we combine fitness and gene vector (a,b)
    fitness_gene = []
    for i in range(len(chromosome.genes)):
        fitness_gene.append({"fitness": fitness_vector[0], "gene": chromosome.genes[i], "index": i})
    fitness_gene_sorted = sorted(fitness_gene, key=lambda i: i['fitness'], reverse=True)
    return fitness_gene_sorted[0]["gene"][0],fitness_gene_sorted[0]["gene"][1]

def process_genes(chromosome, input_dots, sigma, remove_rate):
    fitness_vector = chromosome.evaluate(chromosome, input_dots)
    # first we combine fitness and gene vector (a,b)
    fitness_gene = []
    for i in range(len(chromosome.genes)) :
        fitness_gene.append({"fitness": fitness_vector[0], "gene": chromosome.genes[i], "index": i})
    fitness_gene_sorted = sorted(fitness_gene, key= lambda i: i['fitness'], reverse=True)
    parent_genes = []
    # we choose parents by a chance
    for i in range(Lambda):
        if random.randint(0,100) < 100 * crossover_probability :
            parent_genes.append(fitness_gene_sorted[i]["gene"])
    # crossover
    for i in range (len(parent_genes) - 1):
        # mutation with normal distribution
        mutation_a = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000) < mutation_probability else 0
        mutation_b = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000) < mutation_probability else 0
        new_gene = [(parent_genes[i][0]*.6 + parent_genes[i + 1][0]*.4) + mutation_a,
                         (parent_genes[i][1]*.6 + parent_genes[i + 1][1]*.4) + mutation_b]
        chromosome.genes.append(new_gene)
    # remove bad genes
    for i in range(remove_rate):
        del chromosome.genes[fitness_gene_sorted[len(fitness_gene_sorted) - i]["index"]]
    return chromosome
