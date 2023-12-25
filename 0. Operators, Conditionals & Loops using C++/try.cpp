#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void sum_of_four(int &a, int &b, int &c, int &d)
{
    int x= max(a, b);
    int y = max(c, d);
    if (x>y){cout<<x;}
    else { cout<<y;}
}

int main()
{
    int x,y,z,w;
    cin>>x>>z>>y>>w;
    sum_of_four(x,z,w,y);
    return 0;
}
