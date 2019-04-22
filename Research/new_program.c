#include<stdio.h>
#include<string.h>

void our_awesome_function(char * in)
{
	char out[20];
	strcpy(out, in);
}

int main(int argc, char * argv[])
{
	// imagine a lot of code here
	our_awesome_function(argv[1]);
	return 0;
}
