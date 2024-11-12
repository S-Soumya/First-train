#include <stdio.h> 
#include <stdlib.h> 
#include <conio.h> 
#include <time.h> 
#include <stdbool.h> 
#include <windows.h> 
#include <unistd.h>

#define WIDTH 30 
#define HEIGHT 20

int i, j, k; 

typedef struct 
{ 
 	int x, y;
} P; 

typedef struct 
{ 
 	P body[WIDTH * HEIGHT]; 
 	int len; 
} S; 

void initgame(S *sn, P *food) 
{ 
    sn->len = 1; 
    sn->body[0].x = WIDTH / 2; 
    sn->body[0].y = HEIGHT / 2; 

    food->x = rand() % WIDTH; 
    food->y = rand() % HEIGHT; 
} 

void board(S sn, P food) 
{ 
    system("cls"); 
    printf("Welcome to snake game \n1.Enter w for moving upwards \n2.Enter z for moving down \n3.Enter a for moving left \n4.Enter d for moving right\n\n");

    for (i = 0; i < HEIGHT; i++) 
    { 
        for (j = 0; j < WIDTH; j++)
        { 
            if (i == 0 || i == HEIGHT - 1 || j == 0 || j == WIDTH - 1) 
            { 
                printf("#"); 
            } 
            
            else if (i == food.y && j == food.x)
            { 
                printf("*"); 
            } 
            else 
            { 
                bool isBodyPart = false; 
                for (k = 0; k < sn.len; k++) 
                { 
                    if (sn.body[k].x == j && sn.body[k].y == i) 
                    { 
                        printf("O"); 
                        isBodyPart = true; 
                        break; 
                    } 
                }
                if (!isBodyPart) 
                { 
                    printf(" "); 
                } 
            } 
        } 
 
      printf("\n"); 
    } 
} 

bool updateSn(S *sn, P *food, char dir) 
{ 
	 P nh = sn->body[0]; 
 
 	switch (dir) 
 	{ 
    	case 'w': 
    	{ 
   		nh.y--;
    	break; 
    	} 
    	case 'z': 
    	{ 
        	nh.y++;
        	break; 
    	}
    	case 'a': 
    	{ 
        	nh.x--;
        	break;
    	} 
 
    	case 'd': 
    	{ 
        	nh.x++;
        	break;
    	} 
    	case 'x':
    	{
        	break;
    	}
 
 	} 
 	if (nh.x == 0 || nh.x == WIDTH - 1 || nh.y == 0 || nh.y == HEIGHT - 1) 
 	{ 
    	return false; 
 	} 
 
 	for (i = 0; i < sn->len; i++) 
 	{ 
    	if (nh.x == sn->body[i].x && nh.y == sn->body[i].y) 
    	{ 
        	return false; 
    	}
 	} 
 
 	for (i = sn->len; i > 0; i--) 
 	{
    	sn->body[i] = sn->body[i - 1]; 
 	} 
 
 	sn->body[0] = nh; 
 
 	if (nh.x == food->x && nh.y == food->y) 
 	{ 
    	sn->len++; 
    	food->x = rand() % (WIDTH - 2) + 1; 
    	food->y = rand() % (HEIGHT - 2) + 1; 
 	} 
 
 	return true; 
} 

int main() 
{ 
 	S sn; 
 	P food; 
 
 	char dir = 'z'; 
 	bool running = true;
 
 	srand(time(NULL)); 
 
 	initgame(&sn, &food); 

 	while (running) 
 	{ 
    	board(sn, food); 
    	if (_kbhit()) 
    	{ 
        	dir = _getch(); 
    	} 
    	running = updateSn(&sn, &food, dir); 
    
    	Sleep(200); 
 	} 
 	printf("Game Over! \nFinal length: %d\n", sn.len); 
 	return 0; 
}
