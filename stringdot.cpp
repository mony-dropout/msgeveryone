#include <bits/stdc++.h>
using namespace std;
int main()
{
    
    getline(cin,s);
    int tot=0;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' '){s[i]='.';}
    }
    cout<<s;
}