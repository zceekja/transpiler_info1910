import sys

def main():

    x = 10
    y = 0
    y = x - 5
    tmp = y 
    while tmp:
    
        print("{}".format( y))
        x -= 1
        y = x - 5
        tmp = y 
    return 0

if __name__ == '__main__':
    main()