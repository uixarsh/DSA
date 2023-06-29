#include <iostream>
using namespace std;


// the loops helps us to print the pattern!

int main () {
    int noOfChar = 9;
    for (int j=0; j<noOfChar; j++){
    char ch = (char)('A'+j);
    cout<<ch;
    }
    return 0;
}