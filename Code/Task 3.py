class task3:

    def __init__(self, board):
        self.board = board
        self.numberofsteps = 0

    def position(self, k):
        board = self.board
        for i in board:
            if i[1] == k:
                return i[0]

        return 0

    def move(self, k, destination):
        pos = self.position(k)
        if pos == 1:
            if destination not in (6, 8):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 2:
            if destination not in (9, 7):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 3:
            if destination not in (8, 4):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 4:
            if destination not in (3, 9, 11):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 5:
            if destination not in (10, 12):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 6:
            if destination not in (1, 7, 11):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 7:
            if destination not in (2, 6, 12):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 8:
            if destination not in (1, 3):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 9:
            if destination not in (2, 4, 10):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 10:
            if destination not in (5, 9):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 11:
            if destination not in (4, 6):
                print('move failed : ' + k + ' to ' + str(destination))
                return False
        if pos == 12:
            if destination not in (5, 7):
                print('move failed : ' + k + ' to ' + str(destination))
                return False

        if self.board[destination][1] == 'null':
            self.board[pos] = (pos, 'null')
            self.board[destination] = (destination, k)
            print('knight ' + k + ' was moved to ' + str(destination))
            self.numberofsteps += 1
            return True
        else:
            print('move failed (not empty) : ' + k + ' to ' + str(destination))
            return False

    def divide1(self):
        self.move('w2', 6)
        anticlk = [9, 4, 11, 6, 7, 2]
        for i in anticlk:
            if self.position('b2') == 11:
                break
            self.move('b2', i)
        for i in anticlk:
            if self.position('w2') == 2:
                break
            else:
                self.move('w2', i)
                   
        print(self.board)

    def divide2(self):
        anticlk = [1, 6, 7, 12, 5, 10, 9, 4, 3, 8, 1, 6]
        for i in anticlk:
            if self.position('b1') == 7:
                break
            self.move('b1', i)
        for i in anticlk:
            if self.position('b3') == 6:
                break
            self.move('b3', i)
        for i in anticlk:
            if self.position('w1') == 1:
                break
            self.move('w1', i)
        for i in anticlk:
            if self.position('w3') == 3:
                break
            self.move('w3', i)
        for i in anticlk:
            if self.position('b1') == 10:
                break
            self.move('b1', i)
        for i in anticlk:
            if self.position('b3') == 12:
                break
            self.move('b3', i)
        print(self.board)

    

brd = [(0, 'null'), (1, 'b1'), (2, 'b2'), (3, 'b3'), (4, 'null'), (5, 'null'), (6, 'null'), (7, 'null'), (8, 'null'),
       (9, 'null'), (10, 'w1'), (11, 'w2'), (12, 'w3')]
chess = task3(brd)
print(chess.board)
chess.divide1()
chess.divide2()
print(chess.numberofsteps)
