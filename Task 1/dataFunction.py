import dataGeneration
import sys


def dataFunction(x):
    # generate data for a sql entry 
    data = dataGeneration(x);

    # now need to prepare data for sql entry
    # and connect to the database
    # and write the data to it



# if we called this file directly, run the data function and pass the first parameter, x, to it
if __name__ == '__main__':
    x = sys.argv[1]
    dataFunction(x)
