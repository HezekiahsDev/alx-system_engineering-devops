#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop to overload the program
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int i = 0;
	pid_t z_process;

	while (i < 5)
	{
		z_process = fork();
		if (!z_process)
			return (0);
		printf("Zombie process created, PID: %d\n", z_process);
		i++;
	}

	infinite_while();
	return (0);
}
