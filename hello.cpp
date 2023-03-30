#include <iostream>
using std::cout;
using std::endl;
extern "C"{
    void say() {
        cout << "hello world!"<< endl;
    }
}


