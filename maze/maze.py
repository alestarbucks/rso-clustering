import random as r
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, height, width, exits=2):
        if height%2 == 0:
            print("Warning: x_size must be odd. Adding 1.")
            self.x_size = height + 1
        else: self.x_size = height

        if width%2 == 0:
            print("Warning: y_size must be odd. Adding 1.")
            self.y_size = width + 1
        else: self.y_size = width

        self.exits = exits

        self.grid = self.__generate()
        self.grid = self.__open()
    
    def __expand(self, state, maze):
        nodes = []
        x = state[0]
        y = state[1]
        x_size = len(maze)
        y_size = len(maze[0])

        # arriba
        if x-2 > 0:
            if maze[x-2][y] < 1: nodes.append((x-2, y, maze[x-2][y]))
        # izquierda
        if y-2 > 0:
            if maze[x][y-2] < 1: nodes.append((x,y-2, maze[x][y-2]))
        # abajo
        if x+2 < x_size:
            if maze[x+2][y] < 1: nodes.append((x+2,y, maze[x+2][y]))
        # derecha
        if y+2 < y_size:
            if maze[x][y+2] < 1: nodes.append((x,y+2, maze[x][y+2]))

        return nodes

    def __center(self, maze):
        fixed_maze = maze
        if sum(fixed_maze[0])+sum(fixed_maze[1]) == 0:
            for row in range(1, len(maze)-1):
                next_row = row + 1
                fixed_maze[row] = fixed_maze[next_row]
            fixed_maze[len(fixed_maze)-1] = [0 for _ in range(len(fixed_maze[0]))]
        if sum(row[0] for row in fixed_maze)+sum(row[1] for row in fixed_maze) == 0:
            for row in range(1, len(fixed_maze)):
                for column in range(len(fixed_maze[row])-1):
                    fixed_maze[row][column] = fixed_maze[row][column+1]

                    if column == len(fixed_maze[row])-2:
                        fixed_maze[row][column+1] = 0
        return fixed_maze

    def __generate(self):
        stack = []
        x_start, y_start = r.randint(1, self.x_size-2), r.randint(1, self.y_size-2)

        maze = [[0 for _ in range(self.y_size)] for _ in range(self.x_size)]

        maze[x_start][y_start] = 1
        
        
        current_state = (x_start , y_start, maze[x_start][y_start])
        options = self.__expand(current_state, maze)

        chosen = r.choice(options)

        stack.append(current_state)

        maze[chosen[0]][chosen[1]] = 1
        maze[int((chosen[0]+current_state[0])/2)][int((chosen[1]+current_state[1])/2)] = 1
        current_state = chosen
        end = False
        ii = 0
        while True:
            options = self.__expand(current_state, maze)
            while len(options) == 0:
                if len(stack) == 0:
                    end = True
                    break
                current_state = stack.pop()
                options = self.__expand(current_state, maze)
            if len(stack) == 0 and end: break

            # print(stack)

            chosen = r.choice(options)

            if len(options) - 1 > 0:
                stack.append(current_state)

            maze[chosen[0]][chosen[1]] = 1
            maze[int((chosen[0]+current_state[0])/2)][int((chosen[1]+current_state[1])/2)] = 1
            current_state = chosen

            ii +=1

        return self.__center(maze)

    def __open(self):
        new_maze = self.grid
        
        for _ in range(self.exits):
            side = r.randint(0,3)

            if side == 0: # arriba
                x, y = 0, r.randint(1, len(self.grid[0])-2)
                while self.grid[x+1][y] == 0 or new_maze[x][y] == 1:
                    y = r.randint(1, len(self.grid[0])-2)
            elif side == 1: # dcha
                x, y = r.randint(1, len(self.grid)-2), len(self.grid[0])-1
                while self.grid[x][y-1] == 0 or new_maze[x][y] == 1:
                    x = r.randint(1, len(self.grid)-2)
            elif side == 2: # abajo
                x, y = len(self.grid)-1, r.randint(1, len(self.grid[0])-2)
                while self.grid[x-1][y] == 0 or new_maze[x][y] == 1:
                    y = r.randint(1, len(self.grid[0])-2)
            else: # izq
                x, y = r.randint(1, len(self.grid)-2), 0
                while self.grid[x][y+1] == 0 or new_maze[x][y] == 1:
                    x = r.randint(1, len(self.grid)-2)
            
            new_maze[x][y] = 1

        return new_maze

    def save_csv(self, path, id):
        f = open(path + "/maze{}.csv".format(id), "w+")
        for row in self.grid:
            for column in row:
                f.write(str(column) + ',')
            f.write('\n')
        f.close()

    def display(self):
        plt.imshow(self.grid, cmap='gray')
        plt.axis('off')
        plt.show()
    
    def save_image(self, path, id):
        plt.axis('off')
        plt.imsave(path+'/maze{}.png'.format(id),self.grid,cmap='gray',dpi=200)
    
    def __str__(self):
        return str(self.grid)


