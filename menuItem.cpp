#include "menuItem.h"

MenuItem ::MenuItem(){
    name = "N/A";
    price = 0.0;
}
MenuItem ::MenuItem  (string n,double p){
    name = n;
    price = p;
}
MenuItem::MenuItem  (const MenuItem& rhs){
    name = rhs.name;
    price = rhs.price;
}   

void MenuItem::setName(string n){
    name = n;
}
void MenuItem::setPrice(double p){
    price = p;
}

string MenuItem::getName(){
    return name;
}
double MenuItem::getPrice(){
    return price;
}

void MenuItem::displayMenuItemData(){
    cout  << name << ": " << price << endl;
}

void MenuItem::operator-(double d)
{
    price -= d;
    if(price < 0) {price = 0;}
}
MenuItem MenuItem::operator+(const MenuItem& rh)
{
    double sum = price + rh.price;
    MenuItem m("N/A", sum);
    return m;
}

ostream& operator<<(ostream& os, const MenuItem& rh)
{
    cout << rh.name << ": $" << rh.price << endl;
    return os;
}