import time

"""
  Homework#5

  Add your name here: Payson Briggs

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.
"""

if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    
    # write your code here
  class Thing:
    def __init__(self, cities_file, states_file, zipcodes_file, zips_file):
        self.cities_file = cities_file
        self.states_file = states_file
        self.zipcodes_file = zipcodes_file
        self.zips_file = zips_file

    #read cities
      def read_cities(self):
        with open(self.cities_file, "r") as cities_file:
            return cities_file.read().splitlines()
# read states
    def read_states(self):
        with open(self.states_file, "r") as states_file:
            return set(line.strip() for line in states_file if line.strip())
#read zipcodes
    def read_zipcodes(self):
        with open(self.zipcodes_file, "r") as zipcodes_file:
            next(zipcodes_file)  
            return [line.strip().split('\t') for line in zipcodes_file]
          #read zips
          def read_zips(self):
        with open(self.zips_file, "r") as zips_file:
            return zips_file.read().splitlines()
#extracting common cities in states
    def extract_common_cities(self, cities, states, zipcodes):
        city_states = {}
        for line in zipcodes:
            _, _, _, city, state, *_ = line
            if state in states:
                city_states.setdefault(city, set()).add(state)
        common_cities = filter(lambda city: city_states[city] == states, city_states.keys())
        return sorted(common_cities)
#finding long and lat
def extract_lat_lon(self, zipcodes):
        zip_lat_lon = {}
        for line in zipcodes:
            _, zipcode, _, _, _, _, lat, lon, *_ = line
            if zipcode not in zip_lat_lon:
                zip_lat_lon[zipcode] = (lat, lon)
        return zip_lat_lon
  
#making output file and writing the lat and lon
    def write_lat_lon(self, zips, zip_lat_lon, output_file):
        with open(output_file, "w") as output_file:
            for zipcode in zips:
                zipcode = zipcode.strip()
                if zipcode in zip_lat_lon:
                    lat, lon = zip_lat_lon[zipcode]
                    output_file.write(f"{zipcode} {lat} {lon}\n")
                else:
                    output_file.write(f"{zipcode.strip()} Not Found\n")
                  
                   def extract_city_states(self, cities, zipcodes):
        unique_cities = set(city.lower() for city in cities)
        city_states = {}
        for line in zipcodes:
            _, _, _, city, state, *_ = line
            city = city.strip().lower()
            if city in unique_cities:
                city_states.setdefault(city, set()).add(state)
        return city_states

    def write_city_states(self, city_states, output_file):
        with open(output_file, "w") as output_file:
            for city, states in city_states.items():
                states_str = ' '.join(sorted(states)) if states else "Not Found"
                output_file.write(f"{city}: {states_str}\n")
              
    def process(self):
        cities = self.read_cities()
        states = self.read_states()
        zipcodes = self.read_zipcodes()
        zips = self.read_zips()

        common_cities = self.extract_common_cities(cities, states, zipcodes)
        lat_lon_data = self.extract_lat_lon(zipcodes)
        city_states = self.extract_city_states(cities, zipcodes)

        self.write_lat_lon(zips, lat_lon_data, "LatLon.txt")
        self.write_city_states(city_states, "CityStates.txt")
        with open("CommonCityNames.txt", "w") as output_file:
            for city in common_cities:
                output_file.write(f"{city}\n")


def main(*args):
    processor = Thing(*args)
    processor.process()

if __name__ == "__main__":
    main("cities.txt", "states.txt", "zipcodes.txt", "zips.txt")



    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

