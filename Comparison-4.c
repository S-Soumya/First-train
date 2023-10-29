// To print the largest among 4 numbers at run time
#include <stdio.h>
int main()
{
	int d, e, f, g;
	int A, B, max;
	printf("Enter first intrger: ");
	scanf("%d", &d);
	printf("Enter second integer: ");
	scanf("%d", &e);
	printf("Enter third integer: ");
	scanf("%d", &f);
	printf("Enter fourth integer: ");
	scanf("%d", &g);
	A= ((d > e) && (d > f) && (d > g) );
	B= (( e > f) && (e > g));
	max= ( ( A||B ) ? ((A > B) ? d : e) : (f > g) ? f : g);
	printf("The largest integer is: %d", max);
	return 0;
} 
