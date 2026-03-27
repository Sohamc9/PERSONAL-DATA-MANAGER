def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")




def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            print("Invalid input. Please enter an integer.")