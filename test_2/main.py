import Matrix
"""
You are given a list of cities. Each direct connection between 
two cities has its transportation cost (an integer bigger than 0). 
The goal is to find the paths of minimum cost between pairs of cities. 
Assume that the cost of each path (which is the sum of costs of all direct 
connections belonging to this path) is at most 200000. The name of a city is a string 
containing characters a,...,z and is at most 10 characters long.2)
"""
while True:
    try:
        number_of_tests = int(input("Number of tests: "))
        if number_of_tests > 0:
            print(number_of_tests)
        else:
            raise
        break
    except:
        print("Please, input correct number of cities!")

while True:
    try:
        number_of_cities = int(input("Number of cities: "))
        if number_of_cities > 0:
            print(number_of_cities)
        else:
            raise
        break
    except:
        print("Please, input correct number of cities!")

matrix = Matrix.Matrix(number_of_cities)
current_city_number = 0
city_names = [number_of_cities]
for test in range(number_of_tests):
    for i in range(number_of_cities):
        while True:
            try:
                name = input("City name: ")
                city_names.append(name)
                p = int(input("Number of neighbours in " + name + ": "))
                if (p >= number_of_cities):
                    raise
                break
            except:
                print("REPIT INPUT!!!\n")
        for j in range(p):
            while True:
                try:
                    nr_cost = input("Number of city and cost: ").split(' ')
                    neighb_city_number = int(nr_cost[0]) - 1
                    transport_cost = int(nr_cost[1])
                    if (neighb_city_number == current_city_number
                            or neighb_city_number < 0
                            or transport_cost < 1):
                        raise
                    matrix[current_city_number][neighb_city_number] = transport_cost
                    break
                except:
                    print("REPIT INPUT!\n")
        current_city_number += 1

    matrix.Floyd()

    while True:
        try:
            number_of_test_travels = int(input("Number of test travels: "))
            if number_of_test_travels > 0:
                print(number_of_test_travels)
            else:
                raise
            break
        except:
            print("Please, input correct number of cities!")
    for i in range(number_of_test_travels):
        while True:
            cost_btw_cities = input("Input start and end cities of your travel: ").split(' ')
            try:
                start_city = int(city_names.index(cost_btw_cities[0])) - 1
                end_city = int(city_names.index(cost_btw_cities[1])) - 1
                break
            except:
                print("Input correct name of cities!")

        print(matrix[start_city][end_city])
