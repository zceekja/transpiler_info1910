#include <stdio.h>

int main()
{
    int x = 10;
    int y;
    while (y = x - 5)
    {
        printf("%d\n", y);
        x -= 1;
    }

    return 0;
}
