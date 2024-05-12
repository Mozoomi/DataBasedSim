from population_init.prereq import SystemSettings


pop_size = int(input("Enter population size: "))
gender_dist = float(input("Enter gender distribution (percentage of males): "))
age_min = int(input("Enter the minimum age: "))
age_max = int(input("Enter the max age: "))
settings = SystemSettings(pop_size, gender_dist, age_max, age_min)
settings.saveData()