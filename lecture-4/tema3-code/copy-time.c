// gcc -o copy-time copy-time.c
#include <time.h>
#include <stdio.h>

static long int source[2048][2048];
static long int dest[2048][2048];


void copyij(long int src[2048][2048], long int dst[2048][2048])
{
  long int i,j;
  for (i = 0; i < 2048; i++)
    for (j = 0; j < 2048; j++)
      dst[i][j] = src[i][j];
}

void copyji(long int src[2048][2048], long int dst[2048][2048])
{
  long int i,j;
  for (j = 0; j < 2048; j++)
    for (i = 0; i < 2048; i++)
      dst[i][j] = src[i][j];
}

int main()
{
	clock_t begin = clock();
	copyij(source, dest);
	clock_t end = clock();

	double time_spent = (double)(end-begin) / CLOCKS_PER_SEC;
	printf("copyij time spent: %f s\n", time_spent);
	time_spent = 0.0;

	begin = clock();
	copyji(source, dest);
	end = clock();
	time_spent = (double)(end-begin) / CLOCKS_PER_SEC;
	printf("copyji time spent: %f s\n", time_spent);
}

