import numpy as np
import random as r

class Rat:
    def __init__(self, x, y):
        self.fitness = 0
        self.pos = np.array([x, y])

class RSOptimizer:
    def __init__(self, agents, problem, max_steps):
        self.agents = agents
        self.problem = problem
        self.population = [
            Rat(
                float(r.randint(self.problem.min_bounds[0], self.problem.max_bounds[0])),
                float(r.randint(self.problem.min_bounds[1], self.problem.max_bounds[1])))
            for i in range(agents)]
        self.step = 1
        self.problem.max_steps = max_steps

        print("uuu", problem.goal, self.problem.goal)
    
    def search_step(self):
        self.C = 2 * r.random()
        self.R = r.random() * 4 + 1
        self.A = self.R - self.step * (self.R / self.problem.max_steps)

        if self.step == 1:
            self.best_rat = None
            self.best_fitness = np.Infinity

            for rat in self.population:
                rat.fitness = self.problem.fitness(rat.pos)
                if rat.fitness < self.best_fitness:
                    self.best_fitness = rat.fitness
                    self.best_rat = rat

            self.started = True

        for rat_index in range(self.agents):
            print(type(self.A), type(self.population[rat_index].pos), type(self.C), type(self.best_rat.pos), type(self.best_rat.pos[0]))
            informed_position = self.A * self.population[rat_index].pos + abs(self.C * (self.best_rat.pos - self.population[rat_index].pos))
            self.population[rat_index].pos = np.around((self.best_rat.pos - informed_position), 0)
            self.population[rat_index].fitness = self.problem.fitness(self.population[rat_index].pos)

            for i in range(len(self.problem.min_bounds)):
                if self.population[rat_index].pos[i] < self.problem.min_bounds[i]:
                    self.population[rat_index].pos[i] = self.problem.min_bounds[i]
                elif self.population[rat_index].pos[i] > self.problem.max_bounds[i]:
                    self.population[rat_index].pos[i] = self.problem.max_bounds[i]
        
        self.step += 1
    
    def get_population(self):
        pop = []

        for rat in self.population:
            pop.append(rat.pos)
        
        return pop
            
            



