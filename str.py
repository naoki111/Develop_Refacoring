import numpy
def print_string(str ,height_number ,width_number):
    height_number = int(height_number)
    width_number = int(width_number)
    for i in range(height_number):
        for i in range(width_number):
            return str

if __name__ == "__main__":
    print_string('abc', numpy.random.randint(0,10), numpy.random.randint(0,10))