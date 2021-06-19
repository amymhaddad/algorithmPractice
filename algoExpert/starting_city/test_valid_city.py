from starting_city import validStartingCity


def test_fourth_index():
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    assert validStartingCity(distances, fuel, mpg) == 4


def test_first_index():
    distances = [10, 20, 10, 15, 5, 15, 25]
    fuel = [0, 2, 1, 0, 0, 1, 1]
    mpg = 20

    assert validStartingCity(distances, fuel, mpg) == 1
