import sys

def main():

    x = 5
    x-=1
    tmp = x
    while tmp:
    
        print("{}".format( x))
        x-=1
        tmp = x
    return 0

if __name__ == '__main__':
    main()