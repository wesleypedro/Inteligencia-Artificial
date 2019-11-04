import Execute

#Arquivo princial que será executado para saber o que o usuário quer executar.
if __name__ == '__main__':
    option = 1
    e = Execute.Functions()

    print('N-QUEENS PROBLEM')

    while option != 0:
        print('Choose an option:')
        print('1 - Use instance for eight queens')
        print('2 - Use instance for n queens')
        print('3 - Quit')

        option = int(input())

        if option == 1:
            print('Running problem to eight queens')
            e.controller(1, 8)

        elif option == 2:
            number = int(input('Choose a number of queens\n'))
            print('Running problem to ', number, ' queens')
            e.controller(2, number)

        elif option == 3:
            print('Exiting')
            option = 0
        else:
            print('Wrong answer. Please, choose a valid option')

'''
Um ponto importante  é que o tabuleiro será representada como sendo uma matriz, onde inicialmente está zerada
e que a cada rainha inserida em uma determinada posição, o valor dessa posição será 1.
'''