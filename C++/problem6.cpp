/**
 * William Ikenna-Nwosu (wiknwo)
 *
 * The sum of the squares of the first ten natural numbers is 385
 *
 * The square of the sum of the first ten natural numbers is 3025
 * 
 * Hence the difference between the sum of the squares of the 
 * first ten natural numbers and the square of the sum is 2640
 *
 * Find the difference between the sum of the squares of the 
 * first one hundred natural numbers and the square of the sum.
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