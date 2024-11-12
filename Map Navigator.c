#include<stdio.h> 
#include<limits.h> 
#include<stdbool.h> 
#define stations 5  // Number of stations 

//Vertex with min distance
 
int dist(int d[], bool s[]) 
{ 
	int min = INT_MAX, mi; 
	int v; 
	for(v = 0; v < stations; v++) 
	{ 
		if(s[v] == false && d[v] <= min) 
		{
			min = d[v]; 
			mi = v;
		}
	} 
	return mi; 
}
 
void sol(int d[]) 
{
	printf("Station: \t Distance: \n"); 
	int i; 
	for(i = 0; i < stations; i++) 
	{ 
		printf("%d \t %d\n", i, d[i]);  //Prints distance array with min distance from the source 
	} 
}

//Implementation of Dijkstra's algorithm 

void djk(int g[stations][stations], int c) 
{
	int d[stations], i; 
	bool s[stations]; 
	for(i = 0; i < stations; i++)
	{
		d[i] = INT_MAX; 
  		s[i] = false;
	}
	
	d[c] = 0; 
  
 	int n, v; 
  
	for(n = 0; n < stations-1; n++) 
 	{ 
  		int x = dist(d, s); 
   
  		s[x] = true; 
   
  		for(v = 0; v < stations; v++) 
  		{ 
   			if(!s[v] && g[x][v] && d[x] != INT_MAX && d[x] + g[x][v] < d[v]) 
   			{
   				d[v] = d[x] + g[x][v];
   			}
  		} 
 	} 
  
 	sol(d); 
} 
 
int main() 
{
	int g[stations][stations] = {{0, 10, 15, 0, 8}, {10, 0, 5, 20, 0}, {20, 5, 0, 2, 1}, {0, 16, 2, 0, 4}, {0, 0, 1, 4, 8}}; 
	
	int src = 0; 
	
	djk(g, src); 
	
	return 0;
}
