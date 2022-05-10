#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{

    // String production rule
    cout << "Enter the production rule line-by-line. (for eg. for A -> $ B | $ D, enter A, then $, then B, then | , then $, then D \n";
    char a, alpha1, b, pipe1, alpha2, d;
    cin >> a;
    cin >> alpha1;
    cin >> b;
    cin >> pipe1;
    cin >> alpha2;
    cin >> d;

    cout << "Production is : " << a << " -> " << alpha1 << " " << b << " " << pipe1 << " " << alpha2 << " " << d << endl;

    if (alpha1 != alpha2)
    {
        cout << "Production rule : " << a << " -> " << alpha1 << " " << b << " " << pipe1 << " " << alpha2 << " " << d << endl;
        cout << "No left Factoring here!" << endl;
    }
    else
    {
        cout << "Production Rule (after eliminating left factoring): \n";
        if (pipe1 == '|')
        {
            cout << a << " -> " << alpha1 << "" << a << "'" << endl;
            cout << a << "'"
                 << " -> " << b << "" << pipe1 << "" << d << "" << pipe1 << "epsilon" << endl;
        }
    }

    return 0;
}