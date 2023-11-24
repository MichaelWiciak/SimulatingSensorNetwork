import random

# Might need a global variable to keep track of the number of entries
# so that id can represent the sensor id and not the entry id
# This will be useful when we want to add more sensors
# and we want to keep track of the sensor id
# This variable will be updated in the main program
# and it will be used in the function below
numberOfEntries = 0


def dataGeneration(numberOfEntries):
    # generate data for a sql entry
    # the format of that entry is:
    # (id, temperature, wind, R.Humidity, CO2)
    # id is a number between 1 and 20
    # temperature is a random number between 8 and 15
    # wind is a random number between 15 and 25
    # R.Humidity is a random number between 40 and 70
    # CO2 is a random number between 500 and 1500

    # create a list of lists
    data = []
    id = 1
    # create a list of random numbers for each entry
    for i in range(numberOfEntries):
        data.append([numberOfEntries, id, random.randint(8, 15), random.randint(15, 25), random.randint(40, 70), random.randint(500, 1500)])
        numberOfEntries += 1
        id += 1
        if id == 21:
            id = 1

    return data


# def test():
#     # test the function
#     # print each entry on a new line
#     # print the number of entries
#     data = dataGeneration(30)
#     for i in range(len(data)):
#         print(data[i])
#     print(len(data))



# test()
