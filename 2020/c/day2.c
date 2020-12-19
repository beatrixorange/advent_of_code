#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void){

	FILE* filePointer;
	int bufferLength = 255;
	char buffer[bufferLength];
	char* pol;
	char* minimum;
	char* maximum;
	char* rest;
	char* letter;
	char* password;
	int valid_pass = 0;
	int valid_pass_two = 0;

	filePointer = fopen("/home/detmer/programming/aoc/2020/aoc_input/input_day2.txt", "r");

	while(fgets(buffer, bufferLength, filePointer)) {
		pol = strtok(buffer, ":");
		password = strtok(NULL, ":");
		minimum = strtok(pol,"-");
		rest = strtok(NULL,"-");
		maximum = strtok(rest, " ");
		letter = strtok(NULL," ");
		int count = 0;
		for(int i=0; i < strlen(password); i++){
			if(password[i] == letter[0]){
				count++;
			}
		}

		int min = atoi(minimum);
		int max = atoi(maximum);

		if(count >= min && count <= max){
			valid_pass++;
		}

		//part two
		if(password[min] != letter[0] && password[max] == letter[0] || password[min] == letter[0] && password[max] != letter[0]){
			valid_pass_two++;
		}

	}
	printf("The amount of valid passwords is part one : %d\n", valid_pass );
	printf("The amount of valid passwords is part two : %d\n", valid_pass_two );

	fclose(filePointer);
}