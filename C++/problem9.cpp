/** William Ikenna-Nwosu (wiknwo)
 * 
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 * 
 **/
#include <iostream>
using namespace std;

int main(){
    int a = 0;
    int b = 0;
    int c = 0;

    for(a = 1;a < 1000;a++){
        for(b = a + 1;b < 1000;b++){
            c = 1000 - a - b;
            if((a * a) + (b * b) == (c * c)) cout << "a: " << a << " b: " << b << " c: " << c << endl; 
        }
    }  

    double product = a * b;

    cout << product << endl;
}
