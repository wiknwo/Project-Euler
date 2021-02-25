/**
 * William Ikenna-Nwosu (wiknwo)
 *
 * A palindromic number reads the same both ways. The largest 
 * palindrome made from the product of two 2-digit numbers is 
 * 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 
 * 3-digit numbers.
 **/
#include <iostream>
#include <string>
using namespace std;

// Function Prototypes
bool isPalindrome(int number);

// Function definitions
bool isPalindrome(int number) {
	int remainder, sum = 0, n;
	n = number;
	while(n > 0) {
		remainder = n % 10;
		sum = (sum * 10) + remainder;
		n = n / 10;
	}
	
	if(number == sum) return true;
	else return false;
}

int main(){
	int maxPalindromicNumber = -1;
	
	for(int i = 100;i < 1000;i++){
		for(int j = 100;j < 1000;j++){
			int product = i * j;
			if(isPalindrome(product) && product > maxPalindromicNumber) maxPalindromicNumber = product;
		}
	}
	cout << "largest palindromic number made from the product of two 3-digit numbers is " << maxPalindromicNumber;
}