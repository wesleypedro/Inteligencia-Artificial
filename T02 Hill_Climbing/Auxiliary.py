# -*- coding: utf-8 -*-
# Used to generate the random state with 0's and 1's
from random import randrange


def random_generator(nurses_number):
    """ Random Generator

    Used to generate a random state with the number of nurses received
    :param nurses_number: Number of nurses
    :return: A new random state to be used

    Important variables
    -------------------
        state       : Variable used to save the random state
    """

    # For each possible shift of all the nurses, is generated randomly a value to define as allocated or not
    state = ''

    # The range goes from 0 to 21*nurses_number. This happens because we every time have 21 shifts to n nurses
    for i in range(0, 21*nurses_number):
        state = state + str(randrange(0, 2))

    # Return the new state generated
    return state


def check_objective(state, nurses_number=10):
    """ Check Objective

    This function will verify if the state that is received is a objective state, through the state and the number of
    nurses to knows where the algorithm has to stop
    :param state: State to be verified
    :param nurses_number: Number of nurses
    :return: number of violations

    Important varables
    ------------------
        violation_count     : Used to save the number of violations to each state evaluated
        location_count      : Used to verify for each nurse if he is allocated in 5 shift by week
        before              : Used to evaluate the third restriction counting the number of consecutive allocation for
                              each nurse
        shift_count         : Used to evaluate the first restriction counting the number of nurses for each shift
        line_count          : Used to verify which shifts the nurse is allocated

    """
    violations_count = 0
    location_count = 0
    before = 0

    # Evaluate the second and third restrictions
    # If the value of location_count is other than 5, we have a restriction violation in the first rule
    # Here, for each 21 shifts we have a nurse. So we evaluate for each nurse if there is any restriction violation
    for i in range(0, 21*nurses_number, 21):
        for j in range(i, (i+21)):
            if state[j] == '1':
                location_count += 1

                # Here and in the following 'if' we are evaluating the third restriction, counting the number of
                # allocations and verifying if we have three consecutive allocations using the 'before' variable
                if before > 3:
                    violations_count += 1

                if before <= 3:
                    before += 1

            # When we are in a state where the nurse isn't allocated, we set the value of before to zero
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
        for j in range(i, 21*nurses_number, 21):
            if state[j] == '1':
                shift_count += 1

        # If the number of nurses allocated is out of this interval, we have a violation
        if (shift_count < 1) or (shift_count > 3):
            violations_count += 1
        shift_count = 0

    # Here we are evaluating the fourth restriction for each nurse
    # When an allocation is found it is checked if the following allocations are on the same shift
    line_count = 0
    for i in range(0, 21*nurses_number, 21):
        j = i
        # First, we look for an allocation
        while j < 210 and state[j] != '1' and (j <= (i + 21)):
            j += 1

        # When we meet, we check if the next ones are on the same shift
        for k in range(j, i + 21, 3):
            if state[k] == '1':
                line_count += 1

        # If the number of allocations in the same shift is different of five, we have a violation
        if line_count != 5:
            violations_count += 1

        line_count = 0

    # After each verification, it is returned the number of restrictions violated
    return violations_count


# Will return a state with modified to the neighbors generator
def state_generator(state, bit, nurses_number=10):
    """ State Generator

    This function is used to generate another state based on the past state and the bit to be modified, there is,  it
    will generate a neighbor state for the problem.
    :param state: The past state to be used to generate the neighbor state
    :param bit: The bit that has to be modified
    :param nurses_number: The number of nurses to know how big the state is

    :return: A new state

    Important variables
    -------------------
        new_state       : The new state that was generated and the next bit to be modified
    """

    # Here we're taking the first part of the state before the bit that will be modified
    new_state = state[0:bit]

    # Here is modified the bit
    if state[bit] == '0':
        new_state += '1'
    else:
        new_state += '0'

    # Here we're taking the last part of the state passed
    new_state += state[bit+1:21*nurses_number]

    # Here is returned the new state and the next bit to be modified
    return new_state, (bit + 1)


# Used to print a state, to reduce code in others functions
def print_output(title, state, violations, nurses_number=10):
    """ Print Output

    This function is used to show to the user a state. It is used to reduce lines of code in other parts of the program.
    Here is received the state, the title, the number of violation and the number of nurses to the size of our state
    :param title: The title of state to be shown
    :param state: The state to be shown
    :param violations: The number of violations to be shown
    :param nurses_number: The number of nurses to know the size of the state
    """

    # Here is shown the title
    print(title)
    # For each nurse their allocations are checked and shown
    for i in range(0, 21*nurses_number, 21):
        output_line = ''
        line = state[i:(i+21)]
        for j in range(0, 21):
            output_line += '|' + line[j]
        output_line += '|'
        print(output_line)
    # Here is shown the number of restrictions of the current state
    print('Number of violated restrictions: ', violations, '\n')

