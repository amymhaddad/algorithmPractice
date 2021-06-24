"""
https://www.algoexpert.io/questions/Valid%20Starting%20City
"""


def validStartingCity(distances, fuel, mpg):

    for start_index in range(len(distances)):
        miles_left_in_tank = 0

        for curr_index in range(start_index, start_index + len(distances)):
            if miles_left_in_tank < 0:
                continue

            curr_index = curr_index % len(distances)

            fuel_recd = fuel[curr_index]
            dist = distances[curr_index]
            miles_left_in_tank += (fuel_recd * mpg) - dist

        if miles_left_in_tank >= 0:
            return start_index
