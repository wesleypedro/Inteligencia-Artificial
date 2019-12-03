# -*- coding: utf-8 -*-
import SimulatedAnnealing as Sa
import GeneticAlgorithm as Ga
import Auxiliary as Au


def main():
    """
    This function is responsible for start the menu of the program to execute options that the user will
    choose to solve the problem of nurses allocation
    :return: void
    """

    option = 1

    while option != 0:
        print('Choose one option')
        print('1 - Simulated Annealing')
        print('2 - Genetic Algorithm')
        print('3 - Documentation')
        print('4 - About')
        print('5 - Exit')
        option = int(input())

        if option == 1:
            temperature = 350
            nurses_number = 10
            initial_state = None

            option_temperature_value = int(input('Do you want to define a value to temperature? (Default: 350)\n'
                                                 '1 - Yes\t\t2 - No\n'))
            if option_temperature_value == 1:
                temperature = int(input('Enter with the value of the temperature:\n'))

            option_nurses_number = int(input('Do you want to define a number of nurses? (Default: 10)\n'
                                             '1 - Yes\t\t2 - No\n'))
            if option_nurses_number == 1:
                nurses_number = int(input('Enter number of nurses:\n'))

            option_state = int(input('Do you want define the initial state?\n'
                                     '1 - Yes\t\t2 - No\n'))
            if option_state == 1:
                iterator = 0
                print('Alert: An state consists of a string of bits (0 or 1).\n'
                      'Insert the bits of each position all together, without spaces \n'
                      'or any other character.The individual contains ', 21 * nurses_number, ' bits.\n')
                initial_state = input('Enter with the initial state :\n')
                while not Au.check_chromosome_composition(chromosome=initial_state, nurses_number=nurses_number):
                    print('Invalid Input')
                    initial_state = input('Enter with the individual number ' + str(iterator + 1) + ':\n')

            Sa.simulated_annealing_solution(current_state=initial_state,
                                            nurses_number=nurses_number,
                                            temperature=temperature)

        elif option == 2:
            population_size = 40
            amount_of_generations = 1000
            mutation_probability = .05
            elitism_percentage = .01
            nurses_number = 10
            population = list()

            option_population_size = int(input('Do you want define population size? (Default: 40)\n'
                                               '1 - Yes\t\t2 - No\n'))
            if option_population_size == 1:
                population_size = int(input('Enter population size:\n'))

            option_amount_of_generations = int(input('Do you want to define a amount of generations? (Default: 1000)\n'
                                                     '1 - Yes\t\t2 - No\n'))
            if option_amount_of_generations == 1:
                amount_of_generations = int(input('Enter amount of generations:\n'))

            option_mutation_probability = int(input('Do you want to define a mutation probability? (Default: 5%)\n'
                                                    '1 - Yes\t\t2 - No\n'))
            if option_mutation_probability == 1:
                mutation_probability = float(input('Enter mutation probability (Ex: 0.05 to 5%):\n'))

            option_elitism_percentage = int(input('Do you want to define a elitism percentage? (Default: 1%)\n'
                                                  '1 - Yes\t\t2 - No\n'))
            if option_elitism_percentage == 1:
                elitism_percentage = float(input('Enter elitism percentage (Ex: 0.25 to 25%):\n'))

            option_nurses_number = int(input('Do you want to define a number of nurses? (Default: 10)\n'
                                             '1 - Yes\t\t2 - No\n'))
            if option_nurses_number == 1:
                nurses_number = int(input('Enter number of nurses:\n'))

            option_population = int(input('Do you want define each individual?\n'
                                          '1 - Yes\t\t2 - No\n'))
            if option_population == 1:
                iterator = 0
                print('Alert: Each individual consists of a string of bits (0 or 1).\n'
                      'Insert the bits of each chromosome all together, without spaces \n'
                      'or any other character.The individual contains ', 21*nurses_number, ' bits.\n')
                while iterator < population_size:
                    individual = input('Enter with the individual number ' + str(iterator+1) + ':\n')
                    if Au.check_chromosome_composition(chromosome=individual, nurses_number=nurses_number):
                        population.append(individual)
                        iterator += 1
                    else:
                        print('Invalid Input')

            Ga.generic_algorithm_solution(nurses_number=nurses_number,
                                          population=population,
                                          population_size=population_size,
                                          amount_of_generations=amount_of_generations,
                                          mutation_probability=mutation_probability,
                                          elitism_percentage=elitism_percentage)

        elif option == 3:
            print('Main Documentation')
            help(main)
            print('-------------------------------------------------------')
            print('Simulated Annealing Documentation')
            help(Sa.simulated_annealing_solution)
            print('-------------------------------------------------------')
            print('Genetic Algorithm Documentation')
            help(Ga.generic_algorithm_solution)
            print('-------------------------------------------------------')
            print('Auxiliary Documentation')
            help(Au.neighbors_generator)
            print('-------')
            help(Au.random_generator)
            print('-------')
            help(Au.fitness_function)
            print('-------')
            help(Au.selection)
            print('-------')
            help(Au.crossover)
            print('-------')
            help(Au.chromosome_mutation)
            print('-------')
            help(Au.check_chromosome_composition)
            print('-------')
            help(Au.calculate_weights)
            print('-------')
            help(Au.print_output_simulated_annealing)
            print('-------')
            help(Au.print_output_genetic_algorithm)
            print('-------------------------------------------------------')

        elif option == 4:
            print('\n\nThis program was developed as a work proposal for the \n'
                  'Artificial Intelligence discipline of the Computer Science course \n'
                  'at the Federal University of Ceará, Quixadá campus.\n'
                  'The authors of the program are the following students: \n'
                  'Wallesson Cavalcante and Wesley Pedro. We intend to present \n'
                  'solutions to the problem of nurse allocation in their respective \n'
                  'shifts using the Simulated Annealing and Genetic Algorithm \n'
                  'with some restrictions or extra add-ons.\n\n')

        elif option == 5:
            option = 0

        else:
            print('Invalid option')


# Here is identified the main block of code to be executed fist
if __name__ == '__main__':
    main()

