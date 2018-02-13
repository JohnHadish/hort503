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

# %%
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

#I want this function to print out all of the states of the cells
    def print_grid(self):
        for y in self.grid:
            row_list2 = []
            for x in y:
                cell_stat = x.get_state()
                if cell_stat == 0:
                    row_list2.append("-")
                if cell_stat == 1:
                    row_list2.append("x")
                #else:
                #    row_list2.append("!")
            for z in row_list2:
                print(z, end = "")
            print("")


    def next_move(self):
        self.grid_New = []
        for r in range(self.rows):
            row_list = []
            for c in range(self.cols):
                #new_cell = (r, c)
                new_cell = cell(r, c)
                row_list.append(new_cell)
            self.grid_New.append(row_list)
        for y in range(self.rows):
            #print(y)
            #print("Self_R",self.rows)
            for x in range(self.cols):
                #print(x)
                #print("Self_C",self.cols)

                #Probably can make this better by putting all of these requirments on same line:
                if x >= 1 and y >=1:
                    if x + 1 < self.cols and y + 1 < self.rows:
                        neighbors_alive = 0
                        neighbors_alive += (self.grid[y-1][x-1]).get_state()
                        neighbors_alive += (self.grid[y-1][x]).get_state()
                        neighbors_alive += (self.grid[y-1][x+1]).get_state()
                        neighbors_alive += (self.grid[y][x-1]).get_state()
                        neighbors_alive += (self.grid[y][x+1]).get_state()
                        neighbors_alive += (self.grid[y+1][x-1]).get_state()
                        neighbors_alive += (self.grid[y+1][x]).get_state()
                        neighbors_alive += (self.grid[y+1][x+1]).get_state()
                        #print(neighbors_alive)
                        New_State = 0
                        #This is state of cell in question:
                        Current_Cell_State = (self.grid[y][x]).get_state()
                        #Rule 1, any live cell with fewer than 2 live neighbors dies
                        if neighbors_alive < 2 and Current_Cell_State == 1:
                            New_State = 0
                        #Rule 2, any live cell with 2 or 3 neighbors lives
                        if neighbors_alive in [2, 3] and Current_Cell_State == 1:
                            New_State = 1
                        #Rule 3, any live cell with more than 3 dies
                        if neighbors_alive > 3 and Current_Cell_State == 1:
                            New_State = 0
                        #Rule 4, any dead cell with 3 neighbors becomes alive
                        if neighbors_alive == 3 and Current_Cell_State == 0:
                            New_State = 1

                        (self.grid_New[y][x]).set_state(New_State)
        self.grid = self.grid_New




                        #state = cell_neighbor.get_state()
                        #print(state)
        #        else:
        #            pass


                #neighbors = [[x-1,x,x+1],[x-1,x+1],[x-1,x,x+1]]

                #for neighbors in self.grid:

                #neighbors = [[x-1,x,x+1],[x-1,x+1],[x-1,x,x+1]]
                #neighbor_states = []
                #    for z in neighbors_state:


            #    print(x.get_state(), end = '')
            #print('')

                #print(neighbors_state)
                #Get status of neighbors

    def set_cell(self, x, y, state):
        self.grid[x][y] = cell(x,y,state)

    def play(self, tricks):
        pass

newgrid = grid(50,85)

#OG Ficklin
#newgrid.print_grid()
#newgrid.set_cell(14,40,1)
#newgrid.set_cell(15,42,1)
#newgrid.set_cell(16,39,1)
#newgrid.set_cell(16,40,1)
#newgrid.set_cell(16,43,1)
#newgrid.set_cell(16,44,1)
#newgrid.set_cell(16,45,1)

#Trial
#newgrid.set_cell(1,1,1)
#newgrid.set_cell(2,3,1)
#newgrid.set_cell(4,4,1)

#Gliders:
newgrid.set_cell(5,1,1)
newgrid.set_cell(6,1,1)
newgrid.set_cell(5,2,1)
newgrid.set_cell(6,2,1)

newgrid.set_cell(5,11,1)
newgrid.set_cell(6,11,1)
newgrid.set_cell(7,11,1)

newgrid.set_cell(4,12,1)
newgrid.set_cell(8,12,1)

newgrid.set_cell(3,13,1)
newgrid.set_cell(9,13,1)

newgrid.set_cell(3,14,1)
newgrid.set_cell(9,14,1)

newgrid.set_cell(6,15,1)

newgrid.set_cell(4,16,1)
newgrid.set_cell(8,16,1)

newgrid.set_cell(5,17,1)
newgrid.set_cell(6,17,1)
newgrid.set_cell(7,17,1)

newgrid.set_cell(6,18,1)

newgrid.set_cell(3,21,1)
newgrid.set_cell(4,21,1)
newgrid.set_cell(5,21,1)

newgrid.set_cell(3,22,1)
newgrid.set_cell(4,22,1)
newgrid.set_cell(5,22,1)

newgrid.set_cell(2,23,1)
newgrid.set_cell(6,23,1)

newgrid.set_cell(1,25,1)
newgrid.set_cell(2,25,1)
newgrid.set_cell(6,25,1)
newgrid.set_cell(7,25,1)

newgrid.set_cell(3,35,1)
newgrid.set_cell(4,35,1)

newgrid.set_cell(3,36,1)
newgrid.set_cell(4,36,1)



    #Pulsar
def Pulsar(MoveX, MoveY):
    newgrid.set_cell(13 + MoveY,79 + MoveX,1)
    newgrid.set_cell(14 + MoveY,79 + MoveX,1)
    newgrid.set_cell(15 + MoveY,79 + MoveX,1)
    newgrid.set_cell(19 + MoveY,79 + MoveX,1)
    newgrid.set_cell(20 + MoveY,79 + MoveX,1)
    newgrid.set_cell(21 + MoveY,79 + MoveX,1)

    newgrid.set_cell(11 + MoveY,77 + MoveX,1)
    newgrid.set_cell(16 + MoveY,77 + MoveX,1)
    newgrid.set_cell(18 + MoveY,77 + MoveX,1)
    newgrid.set_cell(23 + MoveY,77 + MoveX,1)

    newgrid.set_cell(11 + MoveY,76 + MoveX,1)
    newgrid.set_cell(16 + MoveY,76 + MoveX,1)
    newgrid.set_cell(18 + MoveY,76 + MoveX,1)
    newgrid.set_cell(23 + MoveY,76 + MoveX,1)

    newgrid.set_cell(11 + MoveY,75 + MoveX,1)
    newgrid.set_cell(16 + MoveY,75 + MoveX,1)
    newgrid.set_cell(18 + MoveY,75 + MoveX,1)
    newgrid.set_cell(23 + MoveY,75 + MoveX,1)

    newgrid.set_cell(13 + MoveY,74 + MoveX,1)
    newgrid.set_cell(14 + MoveY,74 + MoveX,1)
    newgrid.set_cell(15 + MoveY,74 + MoveX,1)
    newgrid.set_cell(19 + MoveY,74 + MoveX,1)
    newgrid.set_cell(20 + MoveY,74 + MoveX,1)
    newgrid.set_cell(21 + MoveY,74 + MoveX,1)

    newgrid.set_cell(13 + MoveY,72 + MoveX,1)
    newgrid.set_cell(14 + MoveY,72 + MoveX,1)
    newgrid.set_cell(15 + MoveY,72 + MoveX,1)
    newgrid.set_cell(19 + MoveY,72 + MoveX,1)
    newgrid.set_cell(20 + MoveY,72 + MoveX,1)
    newgrid.set_cell(21 + MoveY,72 + MoveX,1)

    newgrid.set_cell(11 + MoveY,71 + MoveX,1)
    newgrid.set_cell(16 + MoveY,71 + MoveX,1)
    newgrid.set_cell(18 + MoveY,71 + MoveX,1)
    newgrid.set_cell(23 + MoveY,71 + MoveX,1)

    newgrid.set_cell(11 + MoveY,70 + MoveX,1)
    newgrid.set_cell(16 + MoveY,70 + MoveX,1)
    newgrid.set_cell(18 + MoveY,70 + MoveX,1)
    newgrid.set_cell(23 + MoveY,70 + MoveX,1)

    newgrid.set_cell(11 + MoveY,69 + MoveX,1)
    newgrid.set_cell(16 + MoveY,69 + MoveX,1)
    newgrid.set_cell(18 + MoveY,69 + MoveX,1)
    newgrid.set_cell(23 + MoveY,69 + MoveX,1)

    newgrid.set_cell(13 + MoveY,67 + MoveX,1)
    newgrid.set_cell(14 + MoveY,67 + MoveX,1)
    newgrid.set_cell(15 + MoveY,67 + MoveX,1)
    newgrid.set_cell(19 + MoveY,67 + MoveX,1)
    newgrid.set_cell(20 + MoveY,67 + MoveX,1)
    newgrid.set_cell(21 + MoveY,67 + MoveX,1)
Pulsar(-11,16)
Pulsar(-50,20)
for i in range(1000):
    newgrid.print_grid()

    newgrid.next_move()

newgrid.print_grid()

newgrid.next_move()

newgrid.print_grid()
