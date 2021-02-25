/**
 * William Ikenna-Nwosu (wiknwo)
 * 
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, 
 * and 13, we can see that the 6th prime is 13.
 *
 * What is the 10,001st prime number?
 **/
#include <iostream>
#include <vector> 
using namespace std;

// Function Prototypes
int isPrime(int number);

// Function Definitions
int isPrime(int number){
    for(int i = 2;i < number;i++){
        if(number % i == 0){
            return false;
        }
    }
    return true;
}

int main(){
    cout << "Enter value for n being the nth prime you want: ";
    int n = 0;
    cin >> n;
    vector<int> primenumbers;
    int number = 2;

    while(primenumbers.size() != n){
        if(isPrime(number)){
            primenumbers.push_back(number);
        }
        number++;
    }
    cout << "The 10001st prime number is " << primenumbers.at(primenumbers.size() - 1);
}