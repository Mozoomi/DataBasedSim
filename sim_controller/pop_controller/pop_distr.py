import json

class Population_Distributor:
   def readFile(file_path):
      with open(file_path, 'r') as file:
         data = json.load(file)
         return data

   def divideData(age_distribution, colonies_num):
      total_population = sum(age_distribution.values())
      population_per_colony = total_population // colonies_num
        
      divided_data = {}
      for age_group, count in age_distribution.items():
         divided_count = count // colonies_num
         divided_data[age_group] = divided_count
      
      return divided_data


   #def distribute():
#make section to count amount of colonies
colonies_num = 5
json_data = Population_Distributor.readFile("population_init\data\sim_data\system.json")
age_distribution = json_data.get("age_distribution", {})
divided_data = Population_Distributor.divideData(age_distribution, colonies_num)
print(divided_data)
#distribute the data to the camps 
