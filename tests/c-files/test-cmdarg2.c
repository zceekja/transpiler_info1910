#include <stdio.h>

int main(int argc, char *argv[])
{
    char* firstname = argv[1];
    char* surname = argv[2];
    printf("Hello, %s %s\n",firstname, surname);
    return 0;
}
