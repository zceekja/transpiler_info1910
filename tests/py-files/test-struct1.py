import sys

class Cars:
    def __init__(self, topspeed = 0, acceleration = 0, Tier = 0):
        self.topspeed = topspeed
        self.acceleration = acceleration
        self.Tier = Tier
def main():

    benz = Cars()
    benz.topspeed = 200
    benz.acceleration = 4
    benz.Tier = 'A'
    print("Benz is {} grade and top speed is {}, will reach in {} second".format( benz.Tier,benz.topspeed,benz.acceleration))
    return 0

if __name__ == '__main__':
    main()