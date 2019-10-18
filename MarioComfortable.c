#include <stdio.h>

int main()
{
  int height;
  
  do
  {
    //input loop with validation
    printf ("Height: ");
    scanf("%d", &height);
    // flush input buffer
    while((c = getchar()) != '\n' && c != EOF);
  }
  while(height>23 || height<=0);
  
  for (int i = 0; i < height; i++)
  // base for loop to keep track of which line is being printed
  {
    for (int e = height; e > i; e--)
    {
      printf(" ");
      // prints the required amount of spaces on the left
    }
    for (int f = 0; f < height; f++)
    {
      printf("#");
      // prints the required amount of hashtags on the left
    }
    printf(" ");
    for (int t = 0; t < height; t++)
    {
      printf("#");
      // prints the required amount of hashtags on the right
    }
    for (int v = height; v > i; v--)
    {
      printf(" ");
      // prints the required amount of spaces on the right
    }
    printf("\n");
    // goes to the next line
  }
}
