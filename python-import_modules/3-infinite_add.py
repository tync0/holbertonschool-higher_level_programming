#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    sum = 0
    if n < 2:
        print("0")
    else:
        for i in range(1, n + 1):
            sum += int(sys.argv[i])
        print("{}".format(sum))
