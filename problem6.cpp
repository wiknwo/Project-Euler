/**
 * William Ikenna-Nwosu (wiknwo)
 *
 * 2520 is the smallest number that can be divided by each of the 
 * numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible 
 * by all of the numbers from 1 to 20?
 **/
#include <iostream>
using namespace std;

// Function Prototypes
int sumofsquares(int number);
int squareofsum(int number);

// Function Definitions
int sumofsquares(int number){
	int sum = 0;
	for(int i = 1;i <= number;i++){
		sum += i * i;
	}
	return sum;
}

int squareofsum(int number){
	int sum = 0;
	for(int i = 1;i <= number;i++){
		sum += i;
	}
	return sum * sum;
}

int main(){
	cout << squareofsum(100) - sumofsquares(100);;
}