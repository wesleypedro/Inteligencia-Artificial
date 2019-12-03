# -*- coding: utf-8 -*-
# Used to generate the random individual with 0's and 1's
from random import randrange, choices


# Will return a state with modified to the neighbors generator
def neighbors_generator(state: str, nurses_number=10) -> str:
    """ Neighbors Generator

    This function is used to generate another state based on the past state and the bit to be modified, there is,  it
    will generate a neighbor state for the problem.
    :param state: The past state to be used to generate the neighbor state
    :param nurses_number: The number of nurses to know how big the state is
    :return: A new state
    """

    genes = 21 * nurses_number

    # Random index to change and generated the neighbor
    index = randrange(0, genes)

    # Here we're taking the first part of the state before the bit that will be modified
    new_state = state[0:index]

    # Here is modified the bit
    if state[index] == '0':
        new_state += '1'
    else:
        new_state += '0'

    # Here we're taking the last part of the state passed
    new_state += state[index+1:]

    # Here is returned the new state and the next bit to be modified
    return new_state


# 1. Initial Population
def random_generator(nurses_number: int = 10):
    """ Random Generator

    Used to generate a random state with the number of nurses received
    :param nurses_number: Number of nurses
    :return: A new random state to be used
    """

    # For each possible shift of all the nurses, is generated randomly a value to define as allocated or not
    state = ''

    # The range goes from 0 to 21*nurses_number. This happens because we every time have 21 shifts to n nurses
    for i in range(0, 21 * nurses_number):
        state = state + str(randrange(0, 2))

    # Return the new state generated
    return state


# 2. Fitness Function
def fitness_function(individual: str, nurses_number: int = 10):
    """ Check Objective

    This function will verify if the individual that is received is a objective individual, through the individual
    and the number of nurses to knows where the algorithm has to stop
    :param individual: Individual to be verified
    :param nurses_number: Number of nurses
    :return: number of violations
    """

    genes = 21 * nurses_number
    violations_count = 0
    location_count = 0
    before = 0

    # Evaluate the second and third restrictions
    # If the value of location_count is other than 5, we have a restriction violation in the first rule
    # Here, for each 21 shifts we have a nurse. So we evaluate for each nurse if there is any restriction violation
    for i in range(0, genes, 21):
        for j in range(i, (i + 21)):
            if individual[j] == '1':
                location_count += 1

                # Here and in the following 'if' we are evaluating the third restriction, counting the number of
                # allocations and verifying if we have three consecutive allocations using the 'before' variable
                if before > 3:
                    violations_count += 1

                if before <= 3:
                    before += 1

            # When we are in a individual where the nurse isn't allocated, we set the value of before to zero
            else:
                before = 0

        # If location_count different of 5, we have a violation restriction
        if location_count != 5:
            violations_count += 1
        location_count = 0

    # Evaluate if the first restriction was affected
    shift_count = 0
    # For each shift is evaluated how many nurses are allocated in this period
    for i in range(0, 21):
        for j in range(i, 21 * nurses_number, 21):
            if individual[j] == '1':
                shift_count += 1

        # If the number of nurses allocated is out of this interval, we have a violation
        if (shift_count < 1) or (shift_count > 3):
            violations_count += 1
        shift_count = 0

    # Here we are evaluating the fourth restriction for each nurse
    # When an allocation is found it is checked if the following allocations are on the same shift
    line_count = 0
    for i in range(0, 21 * nurses_number, 21):
        j = i
        # First, we look for an allocation
        while j < 210 and individual[j] != '1' and (j <= (i + 21)):
            j += 1

        # When we meet, we check if the next ones are on the same shift
        for k in range(j, i + 21, 3):
            if individual[k] == '1':
                line_count += 1

        # If the number of allocations in the same shift is different of five, we have a violation
        if line_count != 5:
            violations_count += 1

        line_count = 0

    # After each verification, it is returned the number of restrictions violated
    return violations_count


# 3. Selection
def selection(population: list, weights: list):
    """ Select two individuals to breed

    Selection will be given according to the calculation of cumulative selection aptitude for each individual
    in a population. In this way, a random number will be generated proportional to their fitness values and
    thus the two individuals will be chosen to breed

    Suitability function to determine selection probability
    p_i = f_i / sum (f_i, with i from 1 to N), where i represents each individual in the population

    :param population:
    :param weights:
    :return:
    """

    new_population = list()

    for individual in population:
        new_population.append(individual[1])

    individuals = choices(new_population, weights=weights, k=2)

    return individuals[0], individuals[1]


# 4. Crossover
# def crossover(first_chromosome: str, second_chromosome: str, nurses_number: int = 10) -> (str, str):
#     """ Performs crossover between chromosomes
#
#     This function is responsible for, given two chromosomes, crossover between them
#     :param first_chromosome: chromosome of a first individual
#     :param second_chromosome: chromosome of a second individual
#     :param nurses_number: number of nurses
#     :return: chromosomes of two new individuals generated
#     """
#
#     # calculate the number of genes
#     genes = 21 * nurses_number
#     # generated a position to crossover
#     position = randrange(0, genes)
#
#     # Calculate two new chromosomes
#     new_first_chromosome = first_chromosome[:position] + second_chromosome[position:]
#     new_second_chromosome = second_chromosome[:position] + first_chromosome[position:]'
#
#     # calculates the fitness of the new chromosomes generated
#     new_first_chromosome_fitness = fitness_function(individual=new_first_chromosome, nurses_number=nurses_number)
#     new_second_chromosome_fitness = fitness_function(individual=new_second_chromosome, nurses_number=nurses_number)
#
#     # The parents are compared with it's breed and the best between them is returned
#     if first_chromosome_fitness > new_first_chromosome_fitness:
#         return_first_chromosome = new_first_chromosome
#     else:
#         return_first_chromosome = first_chromosome
#
#     if second_chromosome_fitness > new_second_chromosome_fitness:
#         return_second_chromosome = new_second_chromosome
#     else:
#         return_second_chromosome = second_chromosome
#
#     return return_first_chromosome, return_second_chromosome

def crossover(first_chromosome: str, second_chromosome: str, nurses_number: int = 10) -> (str, str):
    """ Performs crossover between chromosomes

    This function is responsible for, given two chromosomes, crossover between them
    :param first_chromosome: genes of the first chromosome
    :param second_chromosome: genes of the second chromosome
    :param nurses_number: number of nurses
    :return: new chromosome of a individual generated
    """

    # calculate the number of genes
    genes = 21 * nurses_number
    # generated a position to crossover
    position = randrange(0, genes)

    # Calculate two new chromosomes
    new_first_chromosome = first_chromosome[:position] + second_chromosome[position:]
    new_second_chromosome = second_chromosome[:position] + first_chromosome[position:]

    # calculates the fitness of the new chromosomes generated
    new_first_chromosome_fitness = fitness_function(individual=new_first_chromosome, nurses_number=nurses_number)
    new_second_chromosome_fitness = fitness_function(individual=new_second_chromosome, nurses_number=nurses_number)

    # return the best chromosome generated
    if new_first_chromosome_fitness < new_second_chromosome_fitness:
        return new_first_chromosome

    return new_second_chromosome


# 5. Mutation
def chromosome_mutation(chromosome: str, nurses_number: int = 10):
    """ Performs a mutation on a given chromosome

    This function is responsible for update a chromosome value after a mutation and return it
    :param chromosome: Chromosome of an individual
    :param nurses_number: number of nurses
    :return: new chromosome mutated
    """

    # The number of genes in the chromosome is generated
    genes = 21 * nurses_number

    # Random index to mutate
    index = randrange(0, genes)

    # New Chromosome to be returned
    new_chromosome = chromosome[:index]

    # Condition to mutate
    if chromosome[index] == '0':
        new_chromosome += '1'
    else:
        new_chromosome += '0'

    new_chromosome += chromosome[index + 1:]

    # Returning the new chromosome
    return new_chromosome


# Other functions
def check_chromosome_composition(chromosome: str, nurses_number: int) -> bool:
    """ Check the chromosome composition

    This function will return False case the chromosome isn't composed by 0 and 1 and its size does not match
    the amount of shifts for the problem. If it is correct, True will be returned
    :param chromosome:  The chromosomes of the individual
    :param nurses_number: The number of nurses
    :return: True or False when assessing individual composition
    """

    # The number of genes in the chromosome is generated
    genes = 21 * nurses_number

    # Here is removed white spaces
    chromosome = chromosome.replace(' ', '')

    # If the number of genes on the chromosome is different from the expected
    # number of genes, the function returns False
    if len(chromosome) != genes:
        return False

    # For each gene is verified if it is composed by zero or one. Otherwise, the function returns False
    for i in range(len(chromosome)):
        if chromosome[i] != '0' and chromosome[i] != '1':
            return False

    # If all the restrictions was satisfied, the function returns True
    return True


def calculate_weights(population: list()) -> list:
    """ Calculates the weights of each item.

    Receives a population and returns the selection weights, equivalent to probability for the later implemented
    selection function, of each individual in a population.
    :param population: population
    :return: Weights for each individual in the population
    """

    fitness_list = list()
    minimum_fitness = population[0][0]
    maximum_fitness = population[-1][0]
    weight_list = list()

    # Responsible for normalizing fitness values
    for individual in population:
        # fitness_list.append(int(individual[0])
        fitness_list.append((int(individual[0])-minimum_fitness)/(maximum_fitness-minimum_fitness))

    for fitness in fitness_list:
        weight_list.append(100-(fitness*100))

    return weight_list


# Used to print each state from Simulated Annealing
def print_output_simulated_annealing(temperature: int, state: str, violations: int, title: str = None,
                                     nurses_number: int = 10, chose: bool = True):
    """ Print Output of a state, with its violations, and other information

    This function is used to show to the user a state.
    It is used to reduce lines of code in other parts of the program.
    Here you get the status, title, number of violations, the number
    of nurses for our individual size and if it was a state chosen
    for next season and the temperature in the current state.
    :param title: The title of individual to be shown
    :param state: The state to be shown
    :param violations: The number of violations to be shown
    :param nurses_number: The number of nurses to know the size of the individual
    :param chose: If the state was selected or not to the next epoch
    :param temperature: The temperature in the current state
    """

    # Here is shown the title
    if title is not None:
        print(title)
    print('Temperature: ', temperature)
    # For each nurse their allocations are checked and shown
    for i in range(0, 21*nurses_number, 21):
        output_line = ''
        line = state[i:(i+21)]
        for j in range(0, 21):
            output_line += '|' + str(line[j])
        output_line += '|'
        print(output_line)

    # Here is shown the number of restrictions of the current individual
    print('Number of violated restrictions: ', violations)

    # Here is informed if the state was used to the next epoch or not
    print('Was used to the next epoch' if chose else 'Was not used to the next generation')
    print()


# Used to print a individual, to reduce code in others functions
def print_output_genetic_algorithm(individual: str, violations: int, title: str = None):
    """ Print Output

    This function is used to show to the user a individual.
    It is used to reduce lines of code in other parts of the program.
    Here is received the individual, the title and the number of violation.
    :param title: The title of individual to be shown
    :param individual: The individual to be shown
    :param violations: The number of violations to be shown (or value of fitness)
    """

    # Here is shown the title
    if title is not None:
        print(title)
    try:
        print(violations, '\t', hex(int(individual, 2)))
    except:
        print(violations, '\t', individual)

