#Weight_value is in weight, value
import random
from operator import itemgetter, attrgetter

weight_value = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9),
        (30, 4), (30, 5), (70, 4), (20, 9), (20, 2) ,(60, 1)]

arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#genotypes are just arrays
def cross_over(genotype1, genotype2):
    rand_index = random.randrange(1, 12)
    #print(rand_index)
    arr1 = genotype1.copy()
    arr2 = genotype2.copy()
    sub_arr1 = arr1[rand_index:len(arr1)]
    sub_arr2 = arr2[rand_index:len(arr2)]
    for i in range(len(sub_arr1)):
        arr1[rand_index] = sub_arr2[i]
        arr2[rand_index] = sub_arr1[i]
        rand_index += 1
    return arr1, arr2

def initialize_population(size):
    population = []
    for i in range(size):
        genotype = []
        for j in range(12):
            rand_num = random.randrange(0, 2)
            genotype.append(rand_num)
        population.append(genotype)
    return population

def fitness(genotype):
    assert len(genotype) == 12
    total_val = 0
    total_weight = 0
    for i in range(len(genotype)):
        if genotype[i] == 1:
            total_weight += weight_value[i][0]
            total_val += weight_value[i][1]
    if total_weight > 250:
        total_val = 0
    return total_val

def pretty_print(population):
    for i in range(len(population)):
        print(f"Genotype_{i}: ", end="")
        print(population[i])

def build_fit_map(population):
    tup_arr = []
    for i in range(len(population)):
        fit_val = fitness(population[i])
        tup = (population[i], fit_val)
        tup_arr.append(tup)
    return tup_arr

def normalize_fit(tup_arr):
    total_fit = 0
    for i in range(len(tup_arr)):
        total_fit += tup_arr[i][1]
    #total_fit is calculated
    #normalizing every fit_value
    norm_tup = []
    for j in range(len(tup_arr)):
        if tup_arr[j][1] != 0:
            tup = (tup_arr[j][0], (tup_arr[j][1] / total_fit) * 100000)
            norm_tup.append(tup)
        else:
            norm_tup.append((tup_arr[j][0], tup_arr[j][1]))
    norm_tup = sorted(norm_tup, key=itemgetter(1), reverse=True)
    return norm_tup
    
def cross_over_container(tup_arr):
    new_tup_arr = []
    for i in range(0, 500, 4):
        tup1 = tup_arr[i][0]
        tup2 = tup_arr[i + 1][0]
        tup3 = tup_arr[i + 2][0]
        tup4 = tup_arr[i + 3][0]
        new_tup1 = cross_over(tup1, tup2)
        new_tup2 = cross_over(tup3, tup4)
        new_tup3 = cross_over(tup1, tup4)
        new_tup4 = cross_over(tup2, tup3)
        new_tup_arr.append(new_tup1[0])
        new_tup_arr.append(new_tup1[1])
        new_tup_arr.append(new_tup2[0])
        new_tup_arr.append(new_tup2[1])
        new_tup_arr.append(new_tup3[0])
        new_tup_arr.append(new_tup3[1])
        new_tup_arr.append(new_tup4[0])
        new_tup_arr.append(new_tup4[1])
    return new_tup_arr

def mutation(genotype):
    rand_num = random.randrange(0, 100)
    if rand_num < 10:
        rand_index = random.randrange(0, 12)
        if genotype[rand_index] == 1:
            genotype[rand_index] = 0
        else:
            genotype[rand_index] = 1

def mutate_generation(population):
    for i in range(len(population)):
        mutation(population[i])

def start_evolution():
    population = initialize_population(1000)
    
    tup_arr = build_fit_map(population)
    normalized_tup = normalize_fit(tup_arr)
    pretty_print(normalized_tup)
    #####INITIALIZATION COMPLETE#####
    for i in range(8):
        next_gen_population = cross_over_container(normalized_tup)
        mutate_generation(next_gen_population)
        next_gen_tup = build_fit_map(next_gen_population)
        pretty_print(sorted(next_gen_tup, key=itemgetter(1), reverse=True))
        next_gen_tup = normalize_fit(next_gen_tup)
        normalized_tup = next_gen_tup

start_evolution()


