import sys

def main():

    x = 0
    while True:
    
        print("Hello")
        x += 1
    
        if x < 3:
            continue
        else:
            break
    return 0

if __name__ == '__main__':
    main()