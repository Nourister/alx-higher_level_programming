#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for count, n in enumerate(my_list):
        if n % 2 == 0:
            boolist[count] = True
        else:
            boolist[count] = False
    return(boolist)
