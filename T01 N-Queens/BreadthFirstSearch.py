import Checker
import numpy as np
from collections import deque


#Instancia a classe e inincialisa os seus atributos
class BreadthFirst:
    def __init__(self, number):
        self.number = number
        self.column = 0
        self.row = 0
        self.ma = [0] * self.number * self.number
        self.matrix = np.array(self.ma).reshape(self.number, self.number)
        self.queue = deque()

        print('Inited')

        self.check = Checker.Checkers()

#Algoritmo para efetuar a busca em largura
    def bfs(self):
        self.queue.append(self.matrix)
        q_column = deque()
        q_column.append(0)

        while self.queue:
            matrix_from_queue = self.queue.popleft()
            column = q_column.popleft()
            print(matrix_from_queue)
            if self.verify_queens(matrix_from_queue) == self.number:
                print('Found one solution')
                print('\n\nSolution\n')
                print(matrix_from_queue)
                return

            children_ = self.children(matrix_from_queue, column)
            while children_:
                child = children_.popleft()
                self.queue.append(child)
                q_column.append(column+1)
            print(len(self.queue))
            print(self.queue)

    #Retorna os "filhos" de um determinado nó. No caso, verifica se um dado estado possui continuação, e se sim, retorna-os
    def children(self, matrix, column):
        child_queue = deque([])

        for i in range(len(matrix)):
            if self.check.check_horizontal(matrix, i, column) != 1 and \
                    self.check.check_diagonal(matrix, i, column) != 1:
                child_matrix = np.copy(matrix)
                child_matrix[i][column] = 1
                child_queue.append(child_matrix)

        return child_queue

    #Verifica se dado uma matriz, a mesma já contém todas as rainhas que foram solicitadas
    def verify_queens(self, matrix):
        queens = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    queens = queens + 1

        return queens


#Versão 0.9
# Observar que a versão 1.0 está completa e corrigida