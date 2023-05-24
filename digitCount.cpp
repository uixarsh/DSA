#include <iostream>
using namespace std; 

int main () {
    int num, digits=0;
    cin>> num;

    while (num>0) {
        num/=10;
        digits++;
    }
    cout<<digits;
    return 0;
}