#include <iostream>
#include <string>

// A friendly class.
class hello
{
  public:
    hello(const std::string& country) { this->country = country; }
    std::string greet() const { return "Hello from " + country; }
  private:
    std::string country;
};

// A function taking a hello object as an argument.
std::string invite(const hello& w) {
  return w.greet() + "! Please come soon!";
}