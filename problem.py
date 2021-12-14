from maze import maze
import random as r

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
    def actions(self, state):
        raise NotImplementedError
    def result(self, state, action):
        raise NotImplementedError
    def goal_test(self, state):
        raise NotImplementedError
    def path_cost(self, c, state1, action, state2):
        raise NotImplementedError
    def value(self, state):
        raise NotImplementedError

class MazeProblem(Problem):
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
            initial = r.choice(self.maze.exits_list)
            goal = r.choice(self.maze.exits_list)

            while goal == initial:
                goal = r.choice(self.maze.exits_list)
        else:
            initial = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

            while self.maze.grid[initial[0]][initial[1]] == 1:
                initial = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]
            
            goal = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

            while self.maze.grid[goal[0]][goal[1]] == 1 or goal == initial:
                goal = [r.randint(1, len(self.maze.grid)-2), r.randint(1, len(self.maze.grid[0])-2)]

        Problem.__init__(self, initial, goal)

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
        return self.manhattan(state, self.goal)
    
    def manhattan(self, state1, state2):
        return abs(state1[0]-state2[0]) + abs(state1[1]-state2[1])

    def value(self, state):
        if self.goal_test(state):
            return 0
        else:
            return 99