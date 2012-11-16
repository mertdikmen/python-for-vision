#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(getting_started2)
{
    // Create the Python type object for our extension class and define __init__ function.
    class_<hello>("hello", init<std::string>())
        .def("greet", &hello::greet)  // Add a regular member function.
        .def("invite", invite)  // Add invite() as a regular function to the module.
    ;

    def("invite", invite); // Even better, invite() can also be made a member of module!!!
}