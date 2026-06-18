import datetime

class Automobile():
    # Define a constructor
    # The constructor is a function that is called to create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        # Define class properties with the parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year
        self.color = color

    # Create a method to print automobile data
    def print_data(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine Size: {self.engine_size}")
        print(f"Owner: {self.owner}, Color: {self.color}\n")

    # Create a method to get an automobile's age
    def get_age(self):
        # Get the current year 
        the_date = datetime.datetime.now()
        this_year = the_date.year

        # Return the difference between the current year and the auto year as the age
        return this_year - self.year