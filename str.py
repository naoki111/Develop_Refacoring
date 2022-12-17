import random
def print_string(str ,height_number ,width_number):
    str = "aaa"
    height_number = random.randint(0,10)
    width_number  = random.randint(0,10)
    for i in height_number:
        for i in width_number:
            print (str)

if __name__ == "__main__":
    print_string('abc', 1 , 2)