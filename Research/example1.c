#include<stdio.h>
#include<string.h>

// Vulnerable Test function
int vulnfunc(char * test){
	char vulnstr[16];
	strcpy(vulnstr, test); // Vulnerability is here
	return 0;
}

int main(int argc, char * argv[]) {
	// call vulnerable function and return result
	if(vulnfunc(argv[1])) {
	    printf("success\n"); }
	return 0;
}
