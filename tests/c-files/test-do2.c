#include <stdio.h>

int main()
{
    int x = 2;
    do
    {
        int y = 1;
        do
        {

            printf("Hello\n");

            y = y + 1;

        } while (y < 3);

        x = x * 2;

    } while (x < 10);

    return 0;
}
