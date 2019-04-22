#include<stdio.h>
#include<string.h>

// Vulnerable Test function
int vulnfunc(char * test){

	char vulnstr[16];
	strcpy(vulnstr, test); // Vulnerability is here
	if(strcmp(vulnstr, "hello"))
		return 0;
	return 1;
}

int main(int argc, char * argv[]) {

	// check for input
	if( argc != 2) {
		printf("Two args are required\n");
		return 1;
	}

	// call vulnerable function and return result
	if(vulnfunc(argv[1])) {
		printf("fail\n");
	} else {
		printf("success\n");
	}

	return 0;
}
