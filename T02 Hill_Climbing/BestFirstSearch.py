# -*- coding: utf-8 -*-
import Auxiliary as Au
from queue import PriorityQueue


def best_first_search_solution(current_state, nurses_number):
    """ Solve the Best-First Search problem

    :parameter current_state: State that will be analyzed for a solution
    :type current_state: String composed of 0's and 1's
    :parameter nurses_number: Number of nurses that will be used to solve the problem
    :type nurses_number: Integer with the number of nurses

    :return: This algorithm will not return nothing
    :rtype: void

    Important variables
    -------------------
        old_states                      : Save a list with all the stated that was generated
        list_of_generated_states        : It is a priority queue where is saved the state and his violations ordenated
                                            to be accessed after
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
        Au.print_output('Objective state found in first state evaluated', current_state, current_violations, nurses_number)
        return

    old_states = list()
    bit_position = 0
    list_of_generated_states = PriorityQueue()

    Au.print_output('Root state', current_state, current_violations, nurses_number)

    old_states.append(current_state)
    last_state = current_state
    last_violation = current_violations

    while True:
        state_loop = 0

        # Here is generated all the possibles states and compared with oldest states
        while state_loop < 21*nurses_number:
            current_state, bit_position = Au.state_generator(last_state, bit_position, nurses_number)
            current_violations = Au.check_objective(current_state, nurses_number)

            if current_state not in old_states:
                old_states.append(current_state)
                list_of_generated_states.put((current_violations, current_state))

            state_loop += 1
        bit_position = 0

        (current_violations, current_state) = list_of_generated_states.get()

        if current_violations == 0:
            Au.print_output('Objective state found', current_state, current_violations, nurses_number)
            return

        # Foram descartadoas apenas os que possuem função de avaliação maior,
        # segundo o que foi entendido da descrição (p. 5)
        # if current_violations >= last_violation:
        if current_violations > last_violation:
            Au.print_output('Best solution found', last_state, last_violation, nurses_number)
            return

        Au.print_output('State generated', current_state, current_violations, nurses_number)

        last_state = current_state
        last_violation = current_violations

