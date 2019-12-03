from math import e
import math
from random import uniform, randint
import Auxiliary as Au


def simulated_annealing_solution(current_state: str = None, nurses_number: int = 10, temperature: int = 350):
    """ Function used to solve the problem of nurse shifts using Simulated Annealing

    :param current_state: Initial state to use in the problem
    :param nurses_number: Number of nurses
    :param temperature: Initial temperature to solve the problem
    :return: void
    """
    # Initializing current state if it wasn't defined by the user
    if current_state is None:
        current_state = Au.random_generator(nurses_number=nurses_number)

    # Repeat until temperature is set to zero
    while temperature > 0:
        # Used to determinate if the state was chose to the next epoch
        chose = False

        # Violation count to the current state
        violation_count_current_state = Au.fitness_function(individual=current_state, nurses_number=nurses_number)

        # Verify if the objective state was found
        if violation_count_current_state == 0:
            Au.print_output_simulated_annealing(state=current_state, violations=0,
                                                title='Best state found', nurses_number=nurses_number,
                                                chose=chose, temperature=temperature)
            return

        # Get the next neighbor state randomly
        next_state = Au.neighbors_generator(state=current_state, nurses_number=nurses_number)

        # Violation count to the neighbor state
        violation_count_next_state = Au.fitness_function(individual=next_state, nurses_number=nurses_number)

        # Calculate the variation of violation between the current state and the generated state
        violation_count_variation = violation_count_current_state - violation_count_next_state

        # Conditions to choose the next state
        if violation_count_variation > 0:
            current_state = next_state
            violation_count_current_state = violation_count_next_state
            chose = True

        # Using the calculation below, the generated states always had a greater number of constraints violated.
        # elif (e**(violation_count_variation/temperature)) > uniform(0, 1):
        #     current_state = next_state

        else:
            n = randint(0, 100)
            if n < math.exp(violation_count_variation/temperature):
                current_state = next_state
                violation_count_current_state = violation_count_next_state
                chose = True

        Au.print_output_simulated_annealing(state=current_state, violations=violation_count_current_state,
                                            nurses_number=nurses_number, chose=chose, temperature=temperature)

        temperature -= 1

    Au.print_output_simulated_annealing(state=current_state, violations=violation_count_current_state,
                                        title='Last state found', nurses_number=nurses_number,
                                        chose=chose, temperature=temperature)
