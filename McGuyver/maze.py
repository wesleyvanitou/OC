class Maze:

    def __init__(self):
        self.mc_guyver = mc_guyver
        self.items = items
        self.guardian = guardian

    def grid(self):

        self.wall = "*"
        self.passage = "."
        self.grid_size = 15
        G = []

        while len(G) <= GRID_SIZE:
            row = []
            while row <= self.grid_size:
                row.append(self.wall)
            G.append(row)

    def move(self, x, y):
        self.x, self.y = x, y
        self.start = mc_guyver(start)

        while x and y == self.passage:
            #Move Mc Guyver
        #else:
            #Return error


    def main():
        Maze.grid()

Maze.main()
