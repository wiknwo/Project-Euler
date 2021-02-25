/**
 * William Ikenna-Nwosu (wiknwo)
 *
 * Problem 3: Largest Prime Factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 *
 **/
#include <vector> 
#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;

// Function Prototypes
vector<int> primefactorization(int number);

// Function Definitions
vector<int> primefactorization(int number){
	int prime = 2;
	int n = number;
	vector<int> primefactors;
	
	// Get the number of 2s that divide n
	while(n % 2 == 0){
		primefactors.push_back(prime);
		n /= prime;
	}
	prime++;
	
	// prime must now be odd so we can skip the even numbers
	for(prime;prime <= sqrt(n);prime = prime + 2) {
		while (n % prime == 0) {
			primefactors.push_back(prime);
			n /= prime;
		} 
	} 
	
	// Handle edge case where n is a prime number
	if(n > 2) primefactors.push_back(n);
	
	return primefactors;
}

int main(){
	cout << "Enter a number greater than 1: ";
	int number = 0;
	cin >> number;
	vector<int> primefactors = primefactorization(number);
	cout << *max_element(primefactors.begin(), primefactors.end()) << endl;
}