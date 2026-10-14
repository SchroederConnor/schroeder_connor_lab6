#ifndef RESTAURANT_H
#define RESTAURANT_H
#include "menuItem.h"
#define SIZE 5

class Restaurant{
    string name;
    int numItem;
    MenuItem items[SIZE];

    public:
        Restaurant();
        Restaurant(string,int,MenuItem*);
        Restaurant(const Restaurant&);

        string getName();
        int getNumItem();
       
        MenuItem* getItems();

        void setName(string);
        void addItem(MenuItem);

        void displayRestaurantData();
       


};

#endif