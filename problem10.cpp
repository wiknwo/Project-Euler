/**
 * William Ikenna-Nwosu (wiknwo)
 * 
 * 
 */
#include <iostream>
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
    long sum = 0;

    for(int i = 2;i < 2000000;i++)
        if(isPrime(i)) {
            sum += i;
        }
    cout << sum;
}