import random
import numpy as np
Mu = 10
# Todo change Mu's coefficient below to attain the best result
Lambda = 1*Mu
crossover_probability = 0.4
mutation_probability = .02

def generate_initial_population():
    # Todo
    list_of_chromosomes = []

    return list_of_chromosomes

def crossover(chromosome, input_dots, sigma, remove_rate):
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
    children = []
    for i in range (len(parent_genes) - 1):
        # mutation with normal distribution
        mutation_a = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000) < mutation_probability else 0
        mutation_b = np.random.normal(0, sigma, 1)[0] if random.randint(0, 1000) < mutation_probability else 0
        children.append([(parent_genes[i][0]*.6 + parent_genes[i + 1][0]*.4) + mutation_a,
                         (parent_genes[i][1]*.6 + parent_genes[i + 1][1]*.4) + mutation_b])
    chromosome.genes.append(children)
    # remove bad genes
    for i in range(remove_rate):
        del chromosome.genes[fitness_gene_sorted[len(fitness_gene_sorted) - i]["index"]]
    return chromosome

def mutation(chromosome):
    """
    Don't forget to use Gaussian Noise here !
    :param chromosome:
    :return: mutated chromosome
    """
    # Todo
    return

def evaluate_new_generation():
    #Todo
    """
    Call evaluate method for each new chromosome
    :return: list of chromosomes with evaluated scores
    """
    return

def choose_new_generation():
    #Todo
    """
    Use one of the discussed methods in class.
    Q-tournament is suggested !
    :return: Mu selected chromosomes for next cycle
    """
    return


if __name__ == '__main__':
    # Todo -- Use Methods In a proper arrangement
