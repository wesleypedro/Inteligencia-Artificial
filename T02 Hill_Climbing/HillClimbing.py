# -*- coding: utf-8 -*-
import Auxiliary as Au


def hill_climbing_solution(current_state, nurses_number):
    """ Solve the Hill Climbing problem

    This is the function that will solve the Hill Climbing problem. It receives two parameters that will be used
    to solve the problem. Both has to be defined when called
    :parameter current_state: State that will be analyzed for a solution
    :type current_state: String composed of 0's and 1's
    :parameter nurses_number: Number of nurses that will be used to solve the problem
    :type nurses_number: Integer with the number of nurses

    :return: This algorithm will not return nothing
    :rtype: void


    Important variables
    -------------------
        current_violations              : Will save the violation value to the current state
        current_state                   : Will save the current state
        bit_position                    : Used to control which bit will be changed to generate the neighbors state
        last_violation                  : Will save the value to the violation of the last state analyzed
        last_state                      : Will save the last state analyzed
        state_loop                      : Used to control the neighbors generation

    """

    # Here is evaluated the current state and verified if is the gol state
    current_violations = Au.check_objective(current_state, nurses_number)
    if current_violations == 0:
        Au.print_output('Objective state found in first state evaluated', current_state, current_violations)
        return

    # If it isn't the gol state, we will start the loop and generate the other states to find the best solution possible
    bit_position = 0

    # Here is shown the state that is being analyzed
    Au.print_output('Root state', current_state, current_violations, nurses_number)

    # Variables that will be used to save analyzed states to be used after to comparisons or similar
    last_violation = current_violations
    last_state = current_state

    while True:
        state_loop = True

        # Search for the best state to follow as son as possible
        while state_loop:
            # If all the bit position was altered, we stop and show the last state analyzed
            if bit_position == nurses_number:
                print('There is no new operators to be applied')
                Au.print_output('Last best state found', last_state, last_violation, nurses_number)
                return

            current_state, bit_position = Au.state_generator(last_state, bit_position, nurses_number)
            current_violations = Au.check_objective(current_state, nurses_number)

            # If we found a better state, so we stop and will analyze it
            if current_violations < last_violation:
                state_loop = False
                bit_position = 0

        # If it don't have violations, we report as a gol state
        if current_violations == 0:
            Au.print_output('Objective state found', current_state, current_violations, nurses_number)
            return

        # Otherwise, we will show the state analyzed and will repeat the loop for a better state
        Au.print_output('State generated', current_state, current_violations, nurses_number)

        # Here we're updating the last violation and the last_state to be used latter
        last_violation = current_violations
        last_state = current_state


