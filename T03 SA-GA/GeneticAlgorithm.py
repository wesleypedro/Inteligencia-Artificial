from random import randrange
import Auxiliary as Au


def generic_algorithm_solution(nurses_number: int = 10, population: list = list(), population_size: int = 40,
                               amount_of_generations: int = 1000, mutation_probability: float = .05,
                               elitism_percentage: float = .01):
    """ Genetic Algorithm Solution

    Solve the problem to n nurses using generic algorithm
    :param nurses_number:
    :param population:
    :param population_size:
    :param amount_of_generations:
    :param mutation_probability:
    :param elitism_percentage:
    :return:
    """

    # Initialize population if it isn't initialized
    if len(population) == 0:
        for _ in range(population_size):
            population.append(Au.random_generator(nurses_number=nurses_number))

    new_population = list()

    # Calculate fitness to each individual and creating a new population with it's fitness
    for individual in population:
        new_population.append((Au.fitness_function(individual=individual, nurses_number=nurses_number), individual))

    # Sort new population and assign population list
    new_population.sort()
    population = new_population.copy()
    new_population.clear()

    best_population_fitness = int(population[0][0])
    best_individual = population[0][1]

    # Calculating the number of individuals to the elitism
    # If the calculation of elitism gives a real number, we take only the whole part
    elitism = int(elitism_percentage*population_size)

    # While population gets an individual with maximum fitness
    while amount_of_generations > 0:

        amount_of_generations -= 1

        new_population = list()

        # Calculates the weights of each item
        weight_list = Au.calculate_weights(population=population)

        # Procreation to generate new population
        population_generated = list()

        # The following implementation didn't get a good result for the new generation generated,
        #   so we changed some things so we could get a better job.
        # for _ in range(int(population_size/2)):
        #
        #     # Do selection
        #     first_individual, second_individual = Au.selection(population=population, weights=weight_list)
        #
        #     # Do crossover
        #     first_son, second_son = Au.crossover(first_chromosome=first_individual,
        #                                          second_chromosome=second_individual,
        #                                          nurses_number=nurses_number)
        #
        #     # Do mutation under a random probability
        #     if randrange(0, 1) < mutation_probability:
        #         first_son = Au.chromosome_mutation(chromosome=first_son, nurses_number=nurses_number)
        #
        #     if randrange(0, 1) < mutation_probability:
        #         second_son = Au.chromosome_mutation(chromosome=second_son, nurses_number=nurses_number)
        #
        #     first_son_fitness = Au.fitness_function(individual=first_son, nurses_number=nurses_number)
        #     second_son_fitness = Au.fitness_function(individual=second_son, nurses_number=nurses_number)
        #
        #     population_generated.append((first_son_fitness, first_son))
        #     # Au.print_output_genetic_algorithm(individual=first_son, violations=first_son_fitness)
        #     population_generated.append((second_son_fitness, second_son))

        for _ in range(int(population_size)):

            # Do selection
            first_individual, second_individual = Au.selection(population=population, weights=weight_list)

            # Shawn the parents
            print('\nParents to next generation:')
            Au.print_output_genetic_algorithm(individual=first_individual, violations=Au.fitness_function(
                individual=first_individual, nurses_number=nurses_number), title='Parent 1')
            Au.print_output_genetic_algorithm(individual=second_individual, violations=Au.fitness_function(
                individual=second_individual, nurses_number=nurses_number), title='Parent 2')

            # Do crossover
            first_son = Au.crossover(first_chromosome=first_individual,
                                     second_chromosome=second_individual,
                                     nurses_number=nurses_number)

            # Do mutation under a random probability
            if randrange(0, 1) < mutation_probability:
                first_son = Au.chromosome_mutation(chromosome=first_son, nurses_number=nurses_number)

            # if randrange(0, 1) < mutation_probability:
            #     second_son = Au.chromosome_mutation(chromosome=second_son, nurses_number=nurses_number)

            first_son_fitness = Au.fitness_function(individual=first_son, nurses_number=nurses_number)
            # second_son_fitness = Au.fitness_function(individual=second_son, nurses_number=nurses_number)

            population_generated.append((first_son_fitness, first_son))
            # population_generated.append((second_son_fitness, second_son))

        population_generated.sort()

        # Apply elitism to new population
        for i in range(elitism):
            new_population.append(population[i])

        # Add the fittest children of the new generation to the population after performing elitism and continuing
        # with the fittest of the previous generation
        for i in range(elitism, population_size):
            new_population.append(population_generated[i])

        # Orders new population for fitness
        new_population.sort()

        current_best_fitness = int(new_population[0][0])
        if current_best_fitness < best_population_fitness:
            best_individual = new_population[0][1]
            best_population_fitness = new_population[0][0]

        population = new_population.copy()
        weight_list.clear()

        # Showing population
        print('Population')
        for individual in population:
            Au.print_output_genetic_algorithm(individual=individual[1], violations=individual[0])

    Au.print_output_genetic_algorithm(individual=best_individual, violations=best_population_fitness,
                                      title='Best individual found')
