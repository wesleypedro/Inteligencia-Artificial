# -*- coding: utf-8 -*-
import Auxiliary as Au


def steepest_ascent_hill_climbing_solution(current_state, nurses_number):
    """ Solve the Steepest-Ascent Hill Climbing problem

    This is the function that will solve the Steepest-Ascent Hill Climbing problem. It receives two parameters that
    will be used to solve the problem. Both has to be defined when called
    :parameter current_state: State that will be analyzed for a solution
    :type current_state: String composed of 0's and 1's
    :parameter nurses_number: Number of nurses that will be used to solve the problem
    :type nurses_number: Integer with the number of nurses

    :return current_state: The last state that was analyzed
    :rtype current_state: String
    :return current_violations: The number of violations of the last state evaluated
    :rtype current_violations Int

    Important variables
    -------------------
        current_violations              : Will save the violation value to the current state
        current_state                   : Will save the current state
        bit_position                    : Used to control which bit will be changed to generate the neighbors state
        last_violation                  : Will save the value to the violation of the last state analyzed
        best_violation_found            : Will save the best violation found
        last_state                      : Will save the last state analyzed
        best_state_found                : Will save the best state that was found
        state_loop                      : Used to control the neighbors generation
    """

    # Here is evaluated the current state and verified if is the gol state
    current_violations = Au.check_objective(current_state, nurses_number)
    if current_violations == 0:
        Au.print_output('Objective state found in first state evaluated', current_state,
                        current_violations, nurses_number)
        return current_state, current_violations

    # If it isn't the gol state, we will start the loop and generate the other states to find the best solution possible
    bit_position = 0

    # Here is shown the state that is being analyzed
    Au.print_output('Root state', current_state, current_violations, nurses_number)

    # Variables that will be used to save analyzed states to be used after to comparisons or similar
    last_violation = current_violations
    best_violation_found = current_violations
    last_state = current_state
    best_state_found = current_state

    while True:
        state_loop = 0

        # Search for the best state to follow inside all the possible states generated
        while state_loop < 21*nurses_number:
            # Will get the possible states and verify if it is the best found at this loop
            current_state, bit_position = Au.state_generator(last_state, bit_position, nurses_number)
            current_violations = Au.check_objective(current_state, nurses_number)

            # If the best state than the saved, so the saved is updated
            if current_violations < best_violation_found:
                best_violation_found = current_violations
                best_state_found = current_state

            state_loop += 1
        bit_position = 0

        # The current state and the current_violations are updated
        current_state = best_state_found
        current_violations = best_violation_found

        # If the current violation great equals the last best violation, so the best possible was found
        if current_violations >= last_violation:
            Au.print_output('Best solution found', current_state, current_violations, nurses_number)
            return current_state, current_violations

        # If current violations equals 0, so the gol state was found
        if current_violations == 0:
            Au.print_output('Objective state found', current_state, current_violations, nurses_number)
            return current_state, current_violations

        # Otherwise, we will show the state analyzed and will repeat the loop for a better state
        Au.print_output('State generated', current_state, current_violations, nurses_number)

        # Here we're updating the last violation and the last_state to be used latter
        last_violation = current_violations
        last_state = current_state


def steepest_ascent_hill_climbing_n_times(nurses_number, n_times):
    """ Solve the Steepest-Ascent Hill Climbing problem to n random states

    :parameter nurses_number: Number of nurses that will be used to solve the problem
    :type nurses_number: Integer with the number of nurses
    :parameter n_times: Number of random states that will be evaluated
    :type n_times: Int

    :return current_state: The last state that was analyzed
    :rtype current_state: String
    :return current_violations: The number of violations of the last state evaluated
    :rtype current_violations Int

    Important variables
    -------------------
        best_state_generated            : Will save the best state generated
        best_violation_found            : Will save the best violation found
        random_states_generated         : Will save a list with the random states generated to don't be used a
                                            state equals to a other state used
        state                           : Save a random state generated
        current_state                   : Save the current state
        current_violations              : Save the current violations
    """

    print('Executing...')

    best_state_generated = ''
    best_violations_found = 0

    random_states_generated = list()

    off_list = True

    # Will execute a loop for the number of random states passed
    for i in range(0, n_times):

        # Will generate the random states
        while off_list:
            state = Au.random_generator(nurses_number)
            if state not in random_states_generated:
                random_states_generated.append(state)
                off_list = False

        # Will save the values returned of steepest_ascent_hill_climbing_solution
        current_state, current_violations = steepest_ascent_hill_climbing_solution(state, nurses_number)
        if best_state_generated == '' or best_violations_found > current_violations:
            best_state_generated = current_state
            best_violations_found = current_violations

        off_list = True

    # Here, we are show the best state found
    print('\n===========================================')
    Au.print_output('Best state found to '+str(n_times)+' random states run', best_state_generated,
                    best_violations_found, nurses_number)
    print('===========================================\n')




