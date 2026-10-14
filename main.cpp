#include "restaurant.h"



int main(){

    // Create a MenuItem object named burger using the parameterized constructor.
    // Pass "Burger" as the name and 8.5 as the price.
    MenuItem burger("Burger", 8.5);

    // Create a MenuItem object named pizza using the parameterized constructor.
    // Pass "Pizza" as the name and 18.55 as the price.
    MenuItem pizza("Pizza", 18.55);

    // Create a MenuItem object named sandwich using the parameterized constructor.
    // Pass "Sandwich" as the name and 10.5 as the price.
    MenuItem sandwich("Sandwich", 10.5);

    // Create a MenuItem object named softDrink using the parameterized constructor.
    // Pass "Soft Drink" as the name and 2.5 as the price.
    MenuItem softDrink("Soft Drink", 2.5);

    // Apply a $2.50 discount to burger using the overloaded - operator of the MenuItem class.
    burger - 2.5;

    // Create a Restaurant object named restaurant using the default constructor.
    Restaurant restaurant;

    // Set the restaurant name to "Hello World".
    restaurant.setName("Hello World");

    // Add burger to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + burger;

    // Add pizza to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + pizza;

    // Add sandwich to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + sandwich;

    // Add softDrink to the restaurant using the overloaded + operator of the Restaurant class.
    // Do not use array indexing to add menu items.
    // Using array indexing will fail the test.
    restaurant + softDrink;

    // Create a MenuItem object named combo by adding burger and
    // softDrink using the overloaded + operator of the MenuItem class.
    MenuItem combo = burger + softDrink;

    // Set the combo item's name to "Combo (Burger & Drinks)".
    combo.setName("Burger & Drinks");

    // Add combo to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + combo;

    // Create a MenuItem object named salad using the parameterized constructor.
    // Pass "Salad" as the name and 10.75 as the price.
    MenuItem salad("Salad", 10.75);

    // Display the restaurant information using the overloaded << operator of the Restaurant class.
    cout << restaurant;

    // Add salad to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + salad;

    

    // Your output must match Output.txt exactly.
    // Pay close attention to spelling, capitalization, spaces, and newlines.

    return 0;
}