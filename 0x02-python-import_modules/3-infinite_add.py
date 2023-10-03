#!/usr/bin/python3
def add_arg(argv):
    c = len(argv) - 1
    if c == 0:
        print("{:d}".format(c))
        return
    else:
        n = 1
        add = 0
        while n <= c:
            add += int(argv[n])
            n += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
