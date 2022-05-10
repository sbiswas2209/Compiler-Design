#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    // string production_rule;
    cout << "Enter the production rule line-by-line. (for eg. for A -> A + B | C, enter A, then A, then +, then B, then |, then C): \n";
    char a, b, c, d, e, f;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    cin >> e;
    cin >> f;
    if (a != b)
    {
        cout << endl
             << "Production rule: " << a << " -> " << b << " " << c << " " << d << " " << e << " " << f << endl;
        cout << "No left recursion here!" << endl;
    }
    else
    {
        cout << "Production rule (after eliminating left recursion): \n";
        if (e == '|')
        {
            cout << a << " -> " << f << "" << a << "'" << endl;
            cout << a << "' -> ɛ " << e << " " << c << d << a << "'" << endl;
        }
        else
        {
            cout << "Incorrect formatting!" << endl;
        }
    }
    return 0;
}