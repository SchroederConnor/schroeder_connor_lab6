#include "restaurant.h"


Restaurant::Restaurant(){
    //implement the default constructor
    // You may reuse the implementations from Lab 4 if needed.
}
Restaurant::Restaurant(string na,int n,MenuItem* it){
    //implement the parameterized constructor
    // You may reuse the implementations from Lab 4 if needed.
}
Restaurant::Restaurant(const Restaurant& rhs){
    //implement the copy constructor
    // You may reuse the implementations from Lab 4 if needed.
}

// Implement all getter and setter methods declared in the header file.
// You may reuse the implementations from Lab 4 if needed.



void Restaurant::addItem(MenuItem mI){

    // Implement the addItem() method.
    // You may reuse the implementations from Lab 4 if needed.
    
}

void Restaurant::displayRestaurantData(){
    cout << "Welcome to Hello World" << endl;
    cout << "===================" << endl;
    cout << "Menu" << endl;

    for(int i=0;i<numItem;i++){
        items[i].displayMenuItemData();
    }

}

