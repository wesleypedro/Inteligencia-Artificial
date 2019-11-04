# -*- coding: utf-8 -*-
import HillClimbing as Hc
import SteepestAscentHillClimbing as Sa
import BestFirstSearch as Bf
import Auxiliary as Au


def main():
    """
    This is the 'Main' file, that contains the main scope of execution of the code. Here, we will receive from the user
    the parameters to execute the code and which options he/she wants to do.

    Example of output
    -----------------

        print('Choose one option')
        print('1 - Hill Climbing')
        print('2 - Steepest-Ascent Hill Climbing')
        print('3 - Best-First Search')
        print('4 - Execute Steepest-Ascent Hill Climbing n times')
        print('5 - Help')
        print('6 - About')
        print('7 - Exit')
        >>

    When the program is executed, this is the first output that the user will see. It contains the Main Menu that the
    user will interact with the system

    Important observation
    ----------------------
        Pay attention to the input format when solicited.
            Incorrect or other type of input to a option can generate an error during the program execution


    Important variables
    --------------------
        option          :   Will save the option that the user will choose according to the menu options
        nurses_number   :   Will save the number of nurses to be used as instance to the problem
        n_times         :   Will save the number of random states that the Steepest-Ascent Hill Climbing will execute

    """

    print('Hill_Climbing Solution by IA\n')
    option = 1

    # Will execute a loop with the menu option to the user choose what wants to do
    while option != 0:
        nurses_number = 10

        print('Choose one option')
        print('1 - Hill Climbing')
        print('2 - Steepest-Ascent Hill Climbing')
        print('3 - Best-First Search')
        print('4 - Execute Steepest-Ascent Hill Climbing n times')
        print('5 - Documentation')
        print('6 - About')
        print('7 - Exit')
        option = int(input())

        # Will analyze the user choose and execute the respective code

        # Here we will collect informations to execute the Hill Climbing algorithm
        if option == 1:
            print('Hill Climbing')

            # To this algorithm option, we can set the number of nurses than will be used in the problem
            print('Choose a option to number of nurses:\n1. Default value\t2. Enter a value')
            nurses_option = int(input())
            if nurses_option == 1:
                nurses_number = 10
            elif nurses_option == 2:
                print('Enter with the number of nurses')
                nurses_number = int(input())
            else:
                print('Invalid choose!\nDefault value will be used')

            # We can yet choose if we will execute with our value or with a random value
            print('Choose a option to Hill Climbing:\n1. Enter a value\t2. Use random value')
            choose = int(input())
            if choose == 1:
                print('Enter initial state')
                state = input()
                Hc.hill_climbing_solution(state, nurses_number)
            elif choose == 2:
                Hc.hill_climbing_solution(Au.random_generator(nurses_number), nurses_number)
            else:
                print('Invalid choose')

        # Here we will collect informations to execute the Steepest-Ascent Hill Climbing
        elif option == 2:
            print('Steepest-Ascent Hill Climbing')

            # To this algorithm option, we can set the number of nurses than will be used in the problem
            print('Choose a option to number of nurses:\n1. Default value\t2. Enter a value')
            nurses_option = int(input())
            if nurses_option == 1:
                nurses_number = 10
            elif nurses_option == 2:
                print('Enter with the number of nurses')
                nurses_number = int(input())
            else:
                print('Invalid choose!\nDefault value (10 nurses) will be used')

            # We can yet choose if we will execute with our value or with a random value
            print('Choose a option to Steepest-Ascent Hill Climbing:\n1. Enter a value\t2. Use random value')
            choose = int(input())
            if choose == 1:
                print('Enter initial state')
                state = input()
                Sa.steepest_ascent_hill_climbing_solution(state, nurses_number)
            elif choose == 2:
                Sa.steepest_ascent_hill_climbing_solution(Au.random_generator(nurses_number), nurses_number)
            else:
                print('Invalid choose')

        # Here we will collect informations to execute the Best-First Search algorithm
        elif option == 3:
            print('Best-First Search')

            # To this algorithm option, we can set the number of nurses than will be used in the problem
            print('Choose a option to number of nurses:\n1. Default value\t2. Enter a value')
            nurses_option = int(input())
            if nurses_option == 1:
                nurses_number = 10
            elif nurses_option == 2:
                print('Enter with the number of nurses')
                nurses_number = int(input())
            else:
                print('Invalid choose!\nDefault value (10 nurses) will be used')

            # We can yet choose if we will execute with our value or with a random value
            print('Choose a option to Best-First Search:\n1. Enter a value\t2. Use random value')
            choose = int(input())
            if choose == 1:
                print('Enter initial state')
                state = input()
                Bf.best_first_search_solution(state, nurses_number)
            elif choose == 2:
                Bf.best_first_search_solution(Au.random_generator(nurses_number), nurses_number)
            else:
                print('Invalid choose')

        # Here we will collect information to execute the Steepest-Ascent Hill Climbing algorithm for n random states
        elif option == 4:
            print('Steepest-Ascent Hill Climbing n times')

            # To this algorithm option, we can set the number of nurses than will be used in the problem
            print('Choose a option to number of nurses:\n1. Default value\t2. Enter a value')
            nurses_option = int(input())
            if nurses_option == 1:
                nurses_number = 10
            elif nurses_option == 2:
                print('Enter with the number of nurses')
                nurses_number = int(input())
            else:
                print('Invalid choose!\nDefault value (10 nurses) will be used')

            # Here we will receive the value to the n random states that the algorithm will execute
            print('Enter n times the program will run')
            n_times = int(input())
            Sa.steepest_ascent_hill_climbing_n_times(nurses_number, n_times)

        # Here we will show the program documentation by file, and its respectively functions
        elif option == 5:
            documentation = 1
            while documentation != 0:
                print('Choose a option:')
                print('1. Show Main documentation')
                print('2. Show Hill Climbing documentation')
                print('3. Show Steepest-Ascent Hill Climbing documentation')
                print('4. Show Best-Fist Search documentation')
                print('5. Show Auxiliary documentation')
                print('6. Back to the Main menu')
                documentation = int(input())

                # Will show the Main file documentation
                if documentation == 1:
                    print('Main documentation')
                    help(main)

                # Will show the HillClimbing file documentation
                elif documentation == 2:
                    print('Hill Climbing documentation')
                    help(Hc.hill_climbing_solution)

                # Will show Steepest-Ascent the HillClimbing file documentation
                elif documentation == 3:
                    print('Steepest-Ascent Hill Climbing documentation')
                    help(Sa.steepest_ascent_hill_climbing_solution)
                    print('\n')
                    help(Sa.steepest_ascent_hill_climbing_n_times)

                # Will show the HillClimbing file documentation for n random states
                elif documentation == 4:
                    print('HillClimbing for n random states documentation')
                    help(Bf.best_first_search_solution)

                # Will show the Auxiliary file documentation
                elif documentation == 5:
                    print('Auxiliary documentation')
                    help(Au.random_generator)
                    help(Au.check_objective)
                    help(Au.state_generator)
                    help(Au.print_output)

                elif documentation == 6:
                    documentation = 0

                else:
                    print('Invalid choose')

        elif option == 6:
            print('\n\nThis program was developed as a work proposal for the \n'
                  'Artificial Intelligence discipline of the Computer Science course \n'
                  'at the Federal University of Ceará, Quixadá campus.\n'
                  'The authors of the program are the following students: \n'
                  'Wallesson Cavalcante and Wesley Pedro. We intend to present \n'
                  'solutions to the problem of nurse allocation in their respective \n'
                  'shifts using the Hill Cilmbing, Steepest-Ascent Hill Climbing and \n'
                  'Best-First Search algorithms, with some restrictions or extra add-ons.\n\n')

        elif option == 7:
            option = 0

        else:
            print('Invalid option')


# Here is identified the main block of code to be executed fist
if __name__ == '__main__':
    main()

