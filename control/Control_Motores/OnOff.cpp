#include <bits/stdc++.h>

class OnOff
{
private:
public:
    OnOff();
    int OnOffController( int state);
};

OnOff::OnOff(){}
int OnOff::OnOffController(int state){
    if (state)
        return 1;
    else
        return 0;
}



