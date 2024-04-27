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
      def read_cities(self):
        with open(self.cities_file, "r") as cities_file:
            return cities_file.read().splitlines()

    def read_states(self):
        with open(self.states_file, "r") as states_file:
            return set(line.strip() for line in states_file if line.strip())

    def read_zipcodes(self):
        with open(self.zipcodes_file, "r") as zipcodes_file:
            next(zipcodes_file)  
            return [line.strip().split('\t') for line in zipcodes_file]



    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

