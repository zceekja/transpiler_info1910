#include <stdio.h>

struct Cars
{
    int topspeed;
    int acceleration;
    char Tier;
};


int main()
{
    struct Cars benz;
    benz.topspeed = 200;
    benz.acceleration = 4;
    benz.Tier = 'A';
    printf("Benz is %c grade and top speed is %d, will reach in %d second\n", benz.Tier,benz.topspeed,benz.acceleration);

    return 0;
}
