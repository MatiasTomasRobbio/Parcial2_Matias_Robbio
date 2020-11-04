class TaTeTi():
    def __init__(self):
        self.board = self.definir_board()
        self.valid = self.definir_valid()
        self.piece = ' x '

    def __str__(self):
        tablero = str('1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n---+---+---\n'
                      '3.1|3.2|3.3')
        return tablero

    def definir_board(self):
        board = dict()
        board['1.1'] = '1.1'
        board['1.2'] = '1.2'
        board['1.3'] = '1.3'
        board['2.1'] = '2.1'
        board['2.2'] = '2.2'
        board['2.3'] = '2.3'
        board['3.1'] = '3.1'
        board['3.2'] = '3.2'
        board['3.3'] = '3.3'
        return board

    def definir_valid(self):
        valid = []
        for key in self.definir_board():
            valid.append(key)
        return valid

    def input_position(self):
        validos = self.valid
        flag = False
        while flag is False:
            posicion = input(str('Posicion'))
            if posicion in validos:
                flag = True
        self.valid.remove(posicion)
        return posicion

    def win(self):
        # verificar filas
        for f in range(1, 4):
            primer_valor = '{}.1'.format(f)
            comparador1 = '{}.{}'.format(f, 2)
            comparador2 = '{}.{}'.format(f, 3)
            if (self.board[primer_valor] == self.board[comparador1] and
               self.board[primer_valor] == self.board[comparador2]):
                return True
        # verficiar columnas
        for f in range(1, 3):
            primer_valor = '1.{}'.format(f)
            comparador1 = '{}.{}'.format(2, f)
            comparador2 = '{}.{}'.format(3, f)
            if (self.board[primer_valor] == self.board[comparador1] and
               self.board[primer_valor] == self.board[comparador2]):
                return True
        # verificar diagonales
        if (self.board['1.1'] == self.board['2.2'] and
           self.board['1.1'] == self.board['3.3']):
            return True
        if (self.board['1.3'] == self.board['2.2'] and
           self.board['1.3'] == self.board['3.1']):
            return True
        return False

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner


if __name__ == '__main__':
    game = TaTeTi()
    print(game.valid)
    print('Ganó ' + game.game())
