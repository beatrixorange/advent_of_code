#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(void){

	FILE* filePointer;
	int bufferLength = 255;
	char buffer[bufferLength];
	int expenses[200];
	int i = 0;

	filePointer = fopen("/home/detmer/programming/aoc/2020/aoc_input/input_day1.txt", "r");

	while(fgets(buffer, bufferLength, filePointer)) {
    	expenses[i] = atoi(buffer);
    	i++;
	}

	fclose(filePointer);

	for(int x = 0; x < 200; x++){
		int sum = expenses[x] + expenses[x+1];
		for(int y = 1; y < 200; y++){
			int sum = expenses[x] + expenses[y];
			if(sum == 2020){
				printf("%d\n", expenses[x] * expenses[y]);
				return 0;
			}
		}
	}
    
}