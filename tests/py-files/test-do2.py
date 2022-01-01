import sys

def main():

    x = 2
    while True:
    
        y = 1
        while True:
        
            print("Hello")
            y = y + 1
        
            if y < 3:
                continue
            else:
                break
        x = x * 2
    
        if x < 10:
            continue
        else:
            break
    return 0

if __name__ == '__main__':
    main()