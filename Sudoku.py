# Sudoku Solver


class Sudoku:
    def __init__(self, val, row, column):
        self.val = val
        self.row = row
        self.cl = column
        self.r = row // 3 * 3  # first row of square room
        self.c = column // 3 * 3   # first column of square room

    @property
    def cell(self):             # get probability numbers for current empty cell
        s_ = S_row[self.row] + S_cl[self.cl] + self.room
        rs = [x for x in range(1, 10) if x not in s_]
        return rs

    def check_cell(self):       # check if the cell contains only 1 number
        if len(self.cell) == 1:
            self.val = self.cell[0]
            self.set_list_values()
            del self

    def check_room(self):            # check probability numbers of all the room members' cell
        for v in self.cell:          # check if a number in the current cell that does not exist in any member cell
            if room_cells[str(self.r) + str(self.c)].count(v) == 1:
                self.val = v
                self.set_list_values()
                del self

    def check_row_clmn(self):
        for v in self.cell:       # check if a number in the current cell that does not exist in any row cell
            if room_rows[self.row].count(v) == 1:
                # print(self.row,self.cl,'room_row_cl',v,self.val)
                self.val = v
                self.set_list_values()
                del self
                                    # check if a number in the current cell that does not exist in any column cell
            if room_cl[self.cl].count(v) == 1:
                # print(self.row,self.cl,'room_row_cl',v,self.val)
                self.val = v
                self.set_list_values()
                del self

    def set_list_values(self):     # change original row and column lists with current value
        S_cl[self.cl][self.row] = self.val
        S_row[self.row][self.cl] = self.val

    @property
    def room(self):                 # create room
        room_members = []
        for i in range(self.r, self.r + 3):
            for j in range(self.c, self.c + 3):
                # get number of members if it is not equal to 0
                if S_row[i][j] != 0:
                    room_members.append(S_row[i][j])
        return room_members


def check_1():
    for key in Sud.keys():
        Sud[key].check_cell()      # look through rooms, rows and columns to check if probability is only 1


def create_room_cell():           # create cells of all rooms
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            key = str(i) + str(j)
            room_cells[key] = []
            for k in range(3):
                for l in range(3):
                    if S_row[i + k][j + l] == 0:
                        room_cells[key] += Sud[str(i + k) + str(j + l)].cell


def create_row_cl_cell():           # create cells of all rows and columns
    for i in range(9):
        room_rows[i] = []
        room_cl[i] = []
        for j in range(9):
            if S_row[i][j] == 0:
                room_rows[i] += Sud[str(i) + str(j)].cell
            if S_cl[i][j] == 0:
                room_cl[i] += Sud[str(j) + str(i)].cell


def check_2():                      # look through cells of rooms, rows and columns to check if probability is only 1
    create_room_cell()
    create_row_cl_cell()
    for key in Sud.keys():
        Sud[key].check_room()
        Sud[key].check_row_clmn()


def get_Sudoku():                   # store unsolved sudoku
    global S_cl
    for i in range(9):
        a = list(map(int, input().split()))
        S_row.append(a)
        clm = 0
        for val in a:
            if val == 0:
                Sud[str(i) + str(clm)] = Sudoku(val, i, clm)
            clm += 1

    S_cl = list(zip(*S_row))
    S_cl = list(map(list, S_cl))


def check(n):
    for i in range(n):
        for j in range(9):
            check_1()
        check_2()


S_row = []
Sud = {}
neighbor = {}
neighbor_row = {}
neighbor_cl = {}
room_rows = {}
room_cl = {}
room_cells = {}
S_cl = []

get_Sudoku()

pow = input('Enter easy, medium, hard')

if pow == 'easy':
    check(1)
elif pow == 'medium':
    check(4)
elif pow == 'hard':
    check(8)

print(*S_row, sep='\n')
input()