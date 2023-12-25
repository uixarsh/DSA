#include<iostream>
using namespace std; 

int factorial (int num){
    cout << "The function is called for " << num << " Iteration"<<endl;
    // BASE CASE 
    if (num ==1 || num==0)
        return 1;
    else 
        return num * factorial(num-1);
}


int main () {
    int num=10;
    cout<<factorial(num);
    return 0;
}