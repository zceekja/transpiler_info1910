#include <stdio.h>

struct Cars
{
    int topspeed;
    int acceleration;
    char Tier;
};

union Result
{
    int Maths;
    char Overall_Grade;
};

int main()
{
    struct Cars benz;
    benz.topspeed = 200;
    benz.acceleration = 4;
    benz.Tier = 'A';
    printf("Benz is %c grade and top speed is %d, will reach in %d second\n", benz.Tier,benz.topspeed,benz.acceleration);



    union Result Toby;
    Toby.Maths = 50;


    printf("Toby got %d, in Math\n",Toby.Maths);
    return 0;
}
