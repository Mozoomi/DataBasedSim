from population_init.prereq import SystemSettings

new_data = int(input("Would  you like to use past data? 1 for yes, 2 for no"))

if new_data == 1:
  pop_size = int(input("Enter population size: "))
  gender_dist = float(input("Enter gender distribution (percentage of males): "))
  age_min = int(input("Enter the minimum age: "))
  age_max = int(input("Enter the max age: "))
  settings = SystemSettings(pop_size, gender_dist, age_max, age_min)
  settings.saveData()

