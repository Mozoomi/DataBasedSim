import json
import pandas as pd

class SystemSettings:
    def __init__(self, pop_size, gender_dist, age_max, age_min):
        self.pop_size = pop_size
        self.gender_dist = gender_dist
        self.age_max = age_max
        self.age_min = age_min
        self.age_distr = {}

    def populationData(self):
        # Calculate male and female population based on gender distribution
        male = round((self.gender_dist / 100) * self.pop_size)
        female = round(self.pop_size - male)
        
        # Read the average percentages from the CSV file
        average_percentages = pd.read_csv('population_init/data/age/nycAgeData.csv', index_col=0)

        # Adjust percentages based on age range
        total_population = 0
        for age_group, percent in average_percentages.iterrows():
            smallest, largest = map(int, age_group.split('-'))
            if smallest >= self.age_min and largest <= self.age_max:
                age_range = min(largest, self.age_max) - max(smallest, self.age_min) + 1
                if age_range > 0:
                    total_population += age_range * percent['percent'] / 100
                self.age_distr[age_group] = 0  # Initialize all age groups with value 0

        # Calculate the scaling factor to adjust the percentages
        scaling_factor = self.pop_size / total_population if total_population > 0 else 0
        
        # Distribute population among age groups
        remaining_population = self.pop_size
        for age_group, percent in average_percentages.iterrows():
            smallest, largest = map(int, age_group.split('-'))
            if smallest >= self.age_min and largest <= self.age_max:
                age_range = min(largest, self.age_max) - max(smallest, self.age_min) + 1
                if age_range > 0:
                    age_population = round(age_range * percent['percent'] / 100 * scaling_factor)
                    self.age_distr[age_group] = age_population
                    remaining_population -= age_population
        
        # Distribute remaining population to age groups
        if remaining_population > 0:
            age_groups = list(self.age_distr.keys())
            while remaining_population > 0:
                for age_group in age_groups:
                    self.age_distr[age_group] += 1
                    remaining_population -= 1
                    if remaining_population == 0:
                        break

        # Update gender distribution
        self.gender_dist = {
            "male": male,
            "female": female
        }

        # Return the updated system settings data
        return {
            "population_size": self.pop_size,
            "gender_distribution": self.gender_dist,
            "age_distribution": self.age_distr,
        }

    def saveData(self):
        # Save the system settings to JSON file
        data = self.populationData()
        with open('population_init/data/sim_data/system.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully!")