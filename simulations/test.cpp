#include<iostream>

class A {
    public:
        virtual int func() {
            return 0;
        }
};

class B : public A {
    int func() {
        return 1;
    }
};

struct lol {
    int d;
};

class L {
    long x;
    char str[20];
    int y[5];
    public:
        int get();
        float ca();
} l;


class one {
    public:
    one(){ std::cout << "one"; }
};

class two : public one {
    public:
    two(){ std::cout << "2"; }
};

class three : public two {
    public:
    three(){ std::cout << "3"; }
};

int main() {
    three t;
    return 0;
}