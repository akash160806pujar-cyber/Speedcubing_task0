#include <stdio.h>
int main()
{
    int curr, moves = 0;
    char prev = ' ';
    while ((curr = getchar()) != EOF)
    {
        if (prev == ' ' && curr != ' ')
            moves++;
        prev = curr;
    }
    printf("%d", moves);
    return 0;
}