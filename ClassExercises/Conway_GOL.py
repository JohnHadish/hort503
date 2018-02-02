class cell():
    def __init__(self, x = 0, y = 0, state = 0):
        self.x = x
        self.y = y
        self.state = state

    def get_state(self):
        #print(self.state)
        return self.state

    def set_state(self, state):
        self.state = state

#t_cell = cell()
#def test_cell(state):
#    t_cell.get_state()
#    t_cell.set_state(state)
#    t_cell.get_state()

#test_cell(45)
#test_cell(0)


class grid():

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for r in range(self.rows):
            row_list = []
            for c in range(self.cols):
                #new_cell = (r, c)
                new_cell = cell(r, c)
                row_list.append(new_cell)
            self.grid.append(row_list)

    def print_grid(self):
        for r in self.grid:
            new_row = []
            for c in r:
                if c.get_state() == 0:
                    new_row.append("-")
                else:
                    new_row.append("x")
                #new_row.append(c.get_state())
            print(new_row)



    def next_move(self):
        pass
    def set_cell(self, x, y, state):
        new_row[]


        for y in self.grid:
            for x in y:
                x.state = state
    def play(self, tricks):
        pass

newgrid = grid(10,5)

#newgrid.__init__(2, 2)
newgrid.print_grid()
newgrid.set_cell(2,2,1)
newgrid.print_grid()
