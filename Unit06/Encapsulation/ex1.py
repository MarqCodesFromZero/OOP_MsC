class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent
    
    # Single getter method that returns all info
    def get_info(self):
        print(f"""
name {self._name} 
capital: {self._capital} 
population: {self._population}
continent: {self._continent}\n""")


# Initialize an object of the Country class
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Access all attributes using single getter method
my_country.get_info()