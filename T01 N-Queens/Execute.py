import BreadthFirstSearch

#Inicialisa a classe com seus atributos que serão usados pelos métodos
class Functions:
    def __init__(self):
        self.option = 0
        self.number = 0
        self.column = 0

    #Após o usuário escolher uma opção na Main, aqui é feito o controle do que será realmente executado no programa
    def controller(self, opt=1, num=8, col=0):
        self.option = opt
        self.number = num
        self.column = col
        print('option: ', self.option, '\nqueens: ', self.number)

        if self.option == 1:
            print('Executing Breadth-First Search to 8 queens')
            bf = BreadthFirstSearch.BreadthFirst(8)
            bf.bfs()

        elif self.option == 2:
            print('Executing Breadth-First Search to %d queens' % self.number)
            bf = BreadthFirstSearch.BreadthFirst(self.number)
            bf.bfs()