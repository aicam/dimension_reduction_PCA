Mu = 10
# Todo change Mu's coefficient below to attain the best result
Lambda = 1*Mu
crossover_probability = 0.4


def generate_initial_population():
    # Todo
    list_of_chromosomes = []

    return list_of_chromosomes

def generate_new_seed():
    """
    :return: return lambda selected parents
    """
    #Todo
    return

def crossover(chromosome1, chromosome2):
    # Todo
    return

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
