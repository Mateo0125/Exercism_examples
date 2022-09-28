EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(minutes):
    """Expected time
    """
    elapsed_bake_time = EXPECTED_BAKE_TIME - minutes
    return elapsed_bake_time


def preparation_time_in_minutes(num_layers):
    """Num layers *= prep time
    """
    num_layers *= PREPARATION_TIME
    return num_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculating time to know how much time lasagna has been baked
    """
    time_baking = elapsed_bake_time + \
        preparation_time_in_minutes(number_of_layers)
    return time_baking
