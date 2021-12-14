from maze import maze
import problem
import matplotlib.pyplot as plt
import rso
import random as r

a = problem.MazeProblem(maze.Maze(21,21,3), 'exit')

# objective = lambda x: -(x[1] + 47) * math.sin(math.sqrt(abs(x[0] / 2 + (x[1] + 47)))) - x[0] * math.sin(math.sqrt(abs(x[0] - (x[1] + 47))))
# b = rso(100, [-512, -512], [512, 512], objective, 200)
# print(b)

# b = rso(3, [0, 0], [])

def initialization(agents, min_bound, max_bound):
    population = []
    for ag in range(agents):
        value = 1
        pos = None

        while value == 1:
            pos = [r.randint(min_bound[0], max_bound[0]-1), r.randint(min_bound[1], max_bound[1]-1)]
            value = a.maze.grid[pos[0]][pos[1]]
        
        population.append(pos)
    return population

n_agents = 3
min_bounds = [0, 0]
max_bounds = [a.maze.x_size, a.maze.y_size]
init = initialization(n_agents, min_bounds, max_bounds)
objective = lambda x: a.fitness(x)
rso= rso.rso(n_agents, min_bounds, max_bounds, objective, 10, init)