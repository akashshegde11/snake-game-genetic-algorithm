from Genetic_Algorithm import *
from Snake_Game import *

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
sol_per_pop = 30
num_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

# Defining the population size.
pop_size = (sol_per_pop,num_weights)
#Creating the initial population.
new_population = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)

num_generations = 5
f = open("D:\\MTech\\AA Assignment\\Snake_Game\\Fittest_Chromosome.txt", "w")
num_parents_mating = 12
for generation in range(num_generations):
    print('--------------        GENERATION ' + str(generation)+ '  --------------' )
    # Measuring the fitness of each chromosome in the population.
    fitness = cal_pop_fitness(new_population)
    print('-------  Fittest Chromosome in Generation ' + str(generation) +' has a fitness value of:  ', np.max(fitness))
	# f = open("Fittest_Chromosome.txt", "a")
    max = str(np.max(fitness))
    f.write("Fittest Chromosome in Generation " + str(generation) + " has a fitness value of: " + max)
    f.write("\n")
    # Selecting the best parents in the population for mating.
    parents = select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

f.close()