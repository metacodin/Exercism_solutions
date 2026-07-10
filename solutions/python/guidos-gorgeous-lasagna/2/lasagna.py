EXPECTED_BAKE_TIME=40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
        
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 40-elapsed_bake_time
    


def preparation_time_in_minutes(number_of_layers):
    """ Calculate the preparation time in minutes.

    Parameters:
        number_of_layers(int): The wanted amount of layers for the lasagna
    
    Returns:
        int: The preparation time in minutes using the number of layers time the preparaion time of each layer
    
    Function that calculate the preparation time of the lasagna based on the amount of layer and the time to prepare each one.
    It returns an int.
    """

    return number_of_layers*2




def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed time in minutes
    
    Parameters: 
        number_of_layers(int): The wanted amount of layers for the lasagna
        elapsed_bake_time(int): The amount of time it took to bake the lasagna
    
    Returns:
    int: The total time spent baking and preparing the lasagna use the number of layer time the amount to make each + the baking time.
    
    This function calculate the amount of time spent making the lasagna."""

    return number_of_layers*2 + elapsed_bake_time




