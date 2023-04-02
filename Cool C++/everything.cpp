#include <iostream>

int main() {
  
  // This is a comment

  std::cout << "Hello World!\n"; // This line prints "Hello World!" to the screen

  int score; // This declares a variable that is an integer called score

  score = 0; // This assigns the value 0 to the variable score

  int number = 0; // This declares a variable that is an integer called score and initializes it to 0

  number = 5+5; // This assigns the sum of 5+5 to the variable number

  std::cout << "The value of number is: " << number << "\n"; // This line prints "The value of number is: 10" to the screen

  std::cout << "Enter a number: "; // This line prints "Enter a number: " to the screen

  std::cin >> number; // This line waits for the user to enter a number and assigns it to the variable number

  std::cout << "The sum of " << number << " + 10 is: " << number+10 << "\n"; // This line prints "The new value of 5 is: 5" to the screen

  int hour = 0;
  std::cout << "input an hour (1-3)";
  std::cin >> hour;

  switch (hour) { // This is a switch statement that will execute the code in the case that matches the value of hour
    case 1: // This is the case that will execute if hour is 1
      std::cout << "It is 1 o'clock\n"; // This line prints "It is 1 o'clock" to the screen
      break; // This break statement will exit the switch statement
    case 2:
      std::cout << "It is 2 o'clock\n";
      break;
    case 3:
      std::cout << "It is 3 o'clock\n";
      break;
    default: // This is the case that will execute if hour is not 1, 2, or 3
      std::cout << "It is not 1, 2, or 3 o'clock\n";
  } // This is the end of the switch statement
}