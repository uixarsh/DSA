#include <iostream>
using namespace std;

int main () {
    int num, reverse;
    cin>>num;

    while (num>0) {
        int lastDigit=0;
        lastDigit=num%10;
        reverse = reverse*10 + lastDigit;
        num/=10;
    }
    cout<<reverse;
    
    return 0;
}