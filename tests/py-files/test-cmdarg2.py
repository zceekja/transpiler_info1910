import sys

def main():

    firstname = sys.argv[1]
    surname = sys.argv[2]
    print("Hello, {} {}".format(firstname, surname))
    return 0

if __name__ == '__main__':
    main()