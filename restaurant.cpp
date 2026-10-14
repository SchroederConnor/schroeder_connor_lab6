#include "restaurant.h"

Restaurant::Restaurant()
{
    name = "N/A";
    numItem = 0;
}
Restaurant::Restaurant(string n, int num, MenuItem* m)
{
    name = n;
    for(int i = 0; i < num; i++)
    {
        items[i] = m[i];
    }
}
Restaurant::Restaurant(const Restaurant& rhs)
{
    name = rhs.name;
    numItem = rhs.numItem;
    for(int i; i < numItem; i++)
    {
        items[i] = rhs.items[i];
    }
}

// Implement all getter and setter methods declared in the header file.
// You may reuse the implementations from Lab 4 if needed.
void Restaurant::setName(string n)
{
    name = n;
}


void Restaurant::addItem(MenuItem m){

    if(numItem < 5)
    {
        items[numItem] = m;
        numItem++;
    }
    else
    {
        cout << "Can not add new menu item. Limit exceeded!" << endl;
    }
}

void Restaurant::operator+(const MenuItem& rh)
{
    addItem(rh);
}

ostream& operator<<(ostream& os, const Restaurant& rh)
{
    cout << "Welcome to " << rh.name << endl;
    cout << "===================" << endl;
    cout << "Menu" << endl;

    for(int i=0;i<rh.numItem;i++){
        MenuItem m = rh.items[i];
        cout << m;
    }
    return os;
}