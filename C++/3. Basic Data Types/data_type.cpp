#include <iostream>
#include <cstdio>
#include <iomanip> 
// using namespace std;

#define FIXED_FLOAT(x) std::fixed << std::setprecision(3) << (x)
#define FIXED_DOUBLE(x) std::fixed << std::setprecision(9) << (x)

int main() {
    int a;
    long b;
    char c;
    float d;
    double e;
    std::cin >> a >> b >> c >> d >> e;
    std::cout << a << std::endl << b << std::endl << c << std::endl;
    std::cout << FIXED_FLOAT(d) << std::endl;
    std::cout << FIXED_DOUBLE(e);

    // Complete the code.
    return 0;
}