#include <iostream>
using namespace std;

int main () {
    int num, sum=0;
    cin>>num;

    while (num>0) {
        int lastDigit = num%10;
        sum+=lastDigit;
        num/=10;
    }

    cout<<sum;

    return 0;
}