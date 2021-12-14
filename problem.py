from maze import maze
import random as r


class MazeProblem():
    def __init__(self, maze=None, modality='exit'):
        if modality not in ['exit', 'random']:
            raise ValueError('Invalid modality')
        else:
            self.modality = modality

        if maze == None:
            self.maze = maze.Maze(10,10,3)
        else:
            self.maze = maze

        if self.modality == 'exit':
            if self.maze.exits < 2:
                raise ValueError('Maze must have at least 2 exits')
            self.initial = r.choice(self.maze.exits_list)
            self.goal = r.choice(self.maze.exits_list)

            while self.goal == self.initial:
                self.goal = r.choice(self.maze.exits_list)
        else:
            self.initial = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

            while self.maze.grid[self.nitial[0]][self.initial[1]] == 1:
                self.initial = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]
            
            self.goal = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

            while self.maze.grid[self.goal[0]][self.goal[1]] == 1 or self.goal == self.initial:
                self.goal = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

        self.min_bounds = [0, 0]
        self.max_bounds = [self.maze.x_size-1, self.maze.y_size-1]

    def actions(self, state):
        actions = []

        if self.maze.grid[state[0]-1][state[1]] == 0:
            actions.append('up')
        if self.maze.grid[state[0]+1][state[1]] == 0:
            actions.append('down')
        if self.maze.grid[state[0]][state[1]-1] == 0:
            actions.append('left')
        if self.maze.grid[state[0]][state[1]+1] == 0:
            actions.append('right')

        return actions

    def result(self, state, action):
        if action == 'up':
            return [state[0]-1, state[1]]
        elif action == 'down':
            return [state[0]+1, state[1]]
        elif action == 'left':
            return [state[0], state[1]-1]
        elif action == 'right':
            return [state[0], state[1]+1]
        else:
            raise ValueError('Invalid action')

    def goal_test(self, state):
        return state == self.goal
    
    def path_cost(self, c, state1, action, state2):
        return c + 1
    
    def fitness(self, state):
        print(self.goal)
        return self.manhattan(state, self.goal)
    
    def manhattan(self, state1, state2):
        return abs(state1[0]-state2[0]) + abs(state1[1]-state2[1])

    def value(self, state):
        if self.goal_test(state):
            return 0
        else:
            return 99