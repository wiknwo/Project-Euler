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

int main(){
	int divisibleCount = 0;
	int number = 1;
	
	while (divisibleCount != 20) {
		for(int i = 1;i <= 20;i++){
			if(number % i == 0) {
				divisibleCount++;
			}
		}
		
		if(divisibleCount == 20) break;
		else {
			divisibleCount = 0;
			number++;
		}
	}
	cout << "Smallest multiple of numbers 1 to 20 is " << number;
}