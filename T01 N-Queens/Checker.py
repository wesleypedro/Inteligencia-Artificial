import numpy as np


# Definição da classe e inicializando os seus atributos que podem ser usados dentro dos seus métodos
#Os métodos listados abaixo são usados pela classe de Busca em largura para saber onde e se pode ser colocado uma rainha
#em uma dada posição
class Checkers:
    def __init__(self):
        self.matrix = []
        self.column = 0
        self.row = 0
        self.diagonal_pri = 0
        self.diagonal_sec = 0


    # Dada uma matriz e a posição de verificação atual, a mesma retorna 1 caso já exista uma rainha na linha em questão, 0 caso contrário
    def check_horizontal(self, matrix, row, col):
        self.matrix = matrix
        self.row = row
        self.column = col

        for i in range(self.column + 1):
            if self.matrix[self.row][i] == 1:
                return 1
        return 0

    # Idem anterior, porém para as diagonais
    def check_diagonal(self, matrix, row, column):
        self.matrix = matrix
        self.row = row
        self.column = column

        self.diagonal_pri = np.diag(self.matrix, (self.column - self.row))
        self.diagonal_sec = np.diag(np.rot90(self.matrix), (self.column - (len(self.matrix) - self.row - 1)))

        if 1 in self.diagonal_pri or 1 in self.diagonal_sec:
            return 1
        return 0
